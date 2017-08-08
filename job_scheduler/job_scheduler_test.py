import unittest
import job_scheduler
from job_input import JobInput




class JobSchedulerTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def CreateJobInput(self, job_name, childs, expected_time, deadline):
        job_input = JobInput()
        job_input.name = job_name
        job_input.expected_time = expected_time
        job_input.child_names = set()
        for c in childs:
            job_input.child_names.add(c)
        return job_input


    def testReadInput(self):
        scheduler = job_scheduler.JobScheduler(1, 1)
        scheduler.ReadInput('job_input.txt')

    def testDuplicateJobInput(self):
        # Verify that job scheduler takes care of duplciate jobs.
        job_input = self.CreateJobInput('J1', ['J2', 'J3'], 5 , 10)

        scheduler = job_scheduler.JobScheduler(3, 1)

        scheduler.ScheduleJob(job_input)
        self.assertEqual(scheduler.NumJobs(), 1)
        # Insert the same job again and verify number of jobs are still 1.
        scheduler.ScheduleJob(job_input)
        self.assertEqual(scheduler.NumJobs(), 1)

    # Tests to check _child_to_parents dict() functionality.
    def testChildToParents(self):
        job_input = self.CreateJobInput('J1', ['J2', 'J3'], 5, 10)
        scheduler = job_scheduler.JobScheduler(3, 1)
        scheduler.ScheduleJob(job_input)

        # Verify that there is only parent of J2
        parent = scheduler._child_to_parents['J2']
        self.assertEqual(len(parent), 1)

        # Verify that there is only parent of J3
        parent = scheduler._child_to_parents['J3']
        self.assertEqual(len(parent), 1)

    def testChildToParentsDuplicate(self):
        job_input1 = self.CreateJobInput('J1', ['J2', 'J3'], 5, 10)
        job_input2 = self.CreateJobInput('J1', ['J2', 'J3'], 5, 10)

        scheduler = job_scheduler.JobScheduler(3, 1)
        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)

        # Verify that there is only parent of J2
        parent = scheduler._child_to_parents['J2']
        self.assertEqual(len(parent), 1)

        # Verify that there is only parent of J3
        parent = scheduler._child_to_parents['J3']
        self.assertEqual(len(parent), 1)

    def testChildToParentsMultiple(self):
        job_input1 = self.CreateJobInput('J1', ['J2', 'J3'], 5, 10)
        job_input2 = self.CreateJobInput('J4', ['J2', 'J3'], 5, 10)

        scheduler = job_scheduler.JobScheduler(3, 1)
        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)

        # Verify that there are two parents of J2
        parent = scheduler._child_to_parents['J2']
        self.assertEqual(len(parent), 2)

        # Verify that there are two parents of J3
        parent = scheduler._child_to_parents['J3']
        self.assertEqual(len(parent), 2)

    # Tests to verify Jobs parent-child pointers.
    def testNoChildCreated(self):
        job_input1 = self.CreateJobInput('J1', ['J2', 'J3'], 5, 10)
        job_input2 = self.CreateJobInput('J4', ['J2', 'J3'], 5, 10)

        scheduler = job_scheduler.JobScheduler(3, 1)
        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)

        # Verify that no child pointers are created because childs job never came as input.
        job1 = scheduler._jobs['J1']
        self.assertEqual(len(job1._childs), 0)

        job2 = scheduler._jobs['J4']
        self.assertEqual(len(job2._childs), 0)


    def testNoEmptyChildList(self):
        job_input1 = self.CreateJobInput('J1', [], 5, 10)
        job_input2 = self.CreateJobInput('J4', [], 5, 10)

        scheduler = job_scheduler.JobScheduler(3, 1)
        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)

        # Verify that no child pointers are created because childs job never came as input.
        job1 = scheduler._jobs['J1']
        self.assertEqual(len(job1._childs), 0)

        job2 = scheduler._jobs['J4']
        self.assertEqual(len(job2._childs), 0)


    def testAllChildCreatedFirst(self):
        job_input1 = self.CreateJobInput('J1', [], 5, 10)
        job_input2 = self.CreateJobInput('J2', [], 5, 10)

        job_input3 = self.CreateJobInput('J3', ['J1', 'J2'], 5, 10)


        scheduler = job_scheduler.JobScheduler(3, 1)
        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)
        scheduler.ScheduleJob(job_input3)

        # Verify that no child pointers are created because childs job never came as input.
        job1 = scheduler._jobs['J1']
        self.assertEqual(len(job1._childs), 0)

        job2 = scheduler._jobs['J2']
        self.assertEqual(len(job2._childs), 0)

        job3 = scheduler._jobs['J3']
        self.assertEqual(len(job3._childs), 2)

    def testFewChildCreatedFirst(self):
        job_input1 = self.CreateJobInput('J1', [], 5, 10)
        job_input2 = self.CreateJobInput('J2', [], 5, 10)

        job_input3 = self.CreateJobInput('J3', ['J1', 'J10'], 5, 10)

        scheduler = job_scheduler.JobScheduler(3, 1)
        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)
        scheduler.ScheduleJob(job_input3)

        # Verify that no child pointers are created because childs job never came as input.
        job1 = scheduler._jobs['J1']
        self.assertEqual(len(job1._childs), 0)

        job2 = scheduler._jobs['J2']
        self.assertEqual(len(job2._childs), 0)

        job3 = scheduler._jobs['J3']
        self.assertEqual(len(job3._childs), 1)

    def testMoreThanOneParent(self):
        job_input1 = self.CreateJobInput('J1', [], 5, 10)
        job_input2 = self.CreateJobInput('J2', ['J1'], 5, 10)

        job_input3 = self.CreateJobInput('J3', ['J1', 'J4'], 5, 10)

        scheduler = job_scheduler.JobScheduler(3, 1)
        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)
        scheduler.ScheduleJob(job_input3)

        # Verify that no child pointers are created because childs job never came as input.
        job1 = scheduler._jobs['J1']
        self.assertEqual(len(job1._childs), 0)

        job2 = scheduler._jobs['J2']
        self.assertEqual(len(job2._childs), 1)

        job3 = scheduler._jobs['J3']
        self.assertEqual(len(job3._childs), 1)

    def testLazyChildCreation(self):
        job_input1 = self.CreateJobInput('J1', ['J2'], 5, 10)
        job_input2 = self.CreateJobInput('J2', [], 5, 10)

        job_input3 = self.CreateJobInput('J3', ['J1', 'J2'], 5, 10)

        scheduler = job_scheduler.JobScheduler(3, 1)
        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)
        scheduler.ScheduleJob(job_input3)

        # Verify that no child pointers are created because childs job never came as input.
        job1 = scheduler._jobs['J1']
        self.assertEqual(len(job1._childs), 1)

        job2 = scheduler._jobs['J2']
        self.assertEqual(len(job2._childs), 0)

        job3 = scheduler._jobs['J3']
        self.assertEqual(len(job3._childs), 2)

    # Bucket tests
    def testOneBucketTwoJobs(self):
        job_input1 = self.CreateJobInput('J1', ['J2'], 5, 10)
        job_input2 = self.CreateJobInput('J2', [], 5, 10)

        scheduler = job_scheduler.JobScheduler(1, 10)

        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)

        self.assertEqual(len(scheduler._priority_bucket), 1)
        self.assertEqual(len(scheduler._priority_bucket[0]), 1)


    # Run Tests
    def testSimpleOneJobRun(self):
        job_input1 = self.CreateJobInput('J1', [], 6, 10)
        scheduler = job_scheduler.JobScheduler(1, 1)

        scheduler.ScheduleJob(job_input1)

        scheduler.Run()

        self.assertEqual(scheduler.total_time_elapsed, 6)


    def testSimpleTwoJobRun(self):
        job_input1 = self.CreateJobInput('J1', [], 6, 10)
        job_input2 = self.CreateJobInput('J2', [], 6, 10)

        scheduler = job_scheduler.JobScheduler(1, 1)

        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)

        scheduler.Run()

        self.assertEqual(scheduler.total_time_elapsed, 12)


    def testSimpleJobWithChildren(self):
        job_input1 = self.CreateJobInput('J1', [], 6, 10)
        job_input2 = self.CreateJobInput('J2', ['J1'], 6, 10)

        scheduler = job_scheduler.JobScheduler(1, 1)

        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)

        scheduler.Run()

        self.assertEqual(scheduler.total_time_elapsed, 12)

    def testSimpleJobWithLazyChildren(self):
        job_input1 = self.CreateJobInput('J1', ['J2'], 2, 10)
        job_input2 = self.CreateJobInput('J2', [], 6, 10)

        scheduler = job_scheduler.JobScheduler(1, 1)

        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)

        scheduler.Run()

        self.assertEqual(scheduler.total_time_elapsed, 8)
        self.assertEqual(scheduler.NumJobs(), 0)


    def testDependencyNotMet(self):
        job_input1 = self.CreateJobInput('J1', ['J3'], 2, 10)
        job_input2 = self.CreateJobInput('J2', [], 6, 10)

        scheduler = job_scheduler.JobScheduler(1, 1)

        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)

        scheduler.Run()

        self.assertEqual(scheduler.total_time_elapsed, 6)
        self.assertEqual(scheduler.NumJobs(), 1)

    """
    def testDeadlock(self):
        job_input1 = self.CreateJobInput('J1', ['J2'], 2, 10)
        job_input2 = self.CreateJobInput('J2', ['J1'], 6, 10)

        scheduler = job_scheduler.JobScheduler(1, 1)

        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)

        scheduler.Run()

        self.assertEqual(scheduler.total_time_elapsed, 0)
        self.assertEqual(scheduler.NumJobs(), 2)
    """

    def testSimpleMultiCPU(self):
        job_input1 = self.CreateJobInput('J1', [], 6, 10)
        job_input2 = self.CreateJobInput('J2', [], 6, 10)

        scheduler = job_scheduler.JobScheduler(1, 2)

        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)

        scheduler.Run()

        self.assertEqual(scheduler.total_time_elapsed, 6)
        self.assertEqual(scheduler.NumJobs(), 0)

    def testSimpleMultiCPUButDifferentDuration(self):
        job_input1 = self.CreateJobInput('J1', [], 6, 10)
        job_input2 = self.CreateJobInput('J2', [], 2, 10)

        scheduler = job_scheduler.JobScheduler(1, 2)

        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)

        scheduler.Run()

        self.assertEqual(scheduler.total_time_elapsed, 6)
        self.assertEqual(scheduler.NumJobs(), 0)


    def testMultiCPUDependentJobs(self):
        job_input1 = self.CreateJobInput('J1', [], 6, 10)
        job_input2 = self.CreateJobInput('J2', ['J1'], 2, 10)

        scheduler = job_scheduler.JobScheduler(1, 2)

        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)

        scheduler.Run()
        #Verify that two cpu's won't be of any use because of dependency.
        self.assertEqual(scheduler.total_time_elapsed, 8)
        self.assertEqual(scheduler.NumJobs(), 0)

    def testMultiCpuLazyChilder(self):
        job_input1 = self.CreateJobInput('J1', [], 6, 10)
        job_input2 = self.CreateJobInput('J2', ['J1'], 2, 10)
        job_input3 = self.CreateJobInput('J3', ['J4'], 2, 10)

        scheduler = job_scheduler.JobScheduler(1, 2)

        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)
        scheduler.ScheduleJob(job_input3)

        scheduler.Run()
        #Verify that two cpu's won't be of any use because of dependency.
        self.assertEqual(scheduler.total_time_elapsed, 8)
        self.assertEqual(scheduler.NumJobs(), 1)

    #Buckets and priority tests
    def testSequenceJobsPriority(self):
        job_input1 = self.CreateJobInput('J1', ['J2'], 6, 10)
        job_input2 = self.CreateJobInput('J2', ['J3'], 2, 10)
        job_input3 = self.CreateJobInput('J3', [], 6, 10)

        scheduler = job_scheduler.JobScheduler(2, 1)

        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)
        scheduler.ScheduleJob(job_input3)

        job1 = scheduler._jobs['J1']
        job2 = scheduler._jobs['J2']
        job3 = scheduler._jobs['J3']

        self.assertEqual(job1.priority, 1)
        self.assertEqual(job2.priority, 2)
        self.assertEqual(job3.priority, 3)


    def testSequenceJobsReversePriority(self):
        job_input1 = self.CreateJobInput('J1', ['J2'], 6, 10)
        job_input2 = self.CreateJobInput('J2', ['J3'], 2, 10)
        job_input3 = self.CreateJobInput('J3', [], 6, 10)

        scheduler = job_scheduler.JobScheduler(2, 1)

        scheduler.ScheduleJob(job_input3)
        scheduler.ScheduleJob(job_input2)
        scheduler.ScheduleJob(job_input1)

        job1 = scheduler._jobs['J1']
        job2 = scheduler._jobs['J2']
        job3 = scheduler._jobs['J3']

        self.assertEqual(job1.priority, 1)
        self.assertEqual(job2.priority, 2)
        self.assertEqual(job3.priority, 3)

    def testSimpleTwoBucket(self):
        job_input1 = self.CreateJobInput('J1', [], 6, 10)
        job_input2 = self.CreateJobInput('J2', [], 2, 10)

        scheduler = job_scheduler.JobScheduler(2, 1)

        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)

        job1 = scheduler._jobs['J1']
        job2 = scheduler._jobs['J2']

        self.assertEqual(job1.priority, 1)
        self.assertEqual(job2.priority, 1)

        scheduler.Run()

        self.assertEqual(scheduler.total_time_elapsed, 8)
        self.assertEqual(scheduler.NumJobs(), 0)

    def testSimpleTwoBucketWithDifferentPriority(self):
        job_input1 = self.CreateJobInput('J100', ['J200'], 6, 10)
        job_input2 = self.CreateJobInput('J200', [], 2, 10)

        scheduler = job_scheduler.JobScheduler(2, 1)

        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)

        job1 = scheduler._jobs['J100']
        job2 = scheduler._jobs['J200']

        self.assertEqual(job1.priority, 1)
        self.assertEqual(job2.priority, 2)

        self.assertEqual(scheduler.FindBucketId(job1), 0)
        self.assertEqual(scheduler.FindBucketId(job2), 1)

    def testSimpleThreeBucketWithDifferentPriority(self):
        job_input1 = self.CreateJobInput('J100', ['J200'], 6, 10)
        job_input2 = self.CreateJobInput('J200', [], 2, 10)
        job_input3 = self.CreateJobInput('J300', ['J200'], 2, 10)

        scheduler = job_scheduler.JobScheduler(2, 1)

        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)
        scheduler.ScheduleJob(job_input3)

        job1 = scheduler._jobs['J100']
        job2 = scheduler._jobs['J200']
        job3 = scheduler._jobs['J300']



        self.assertEqual(job1.priority, 1)
        self.assertEqual(job2.priority, 3)
        self.assertEqual(job3.priority, 1)

        self.assertEqual(scheduler.FindBucketId(job1), 0)
        self.assertEqual(scheduler.FindBucketId(job2), 1)
        self.assertEqual(scheduler.FindBucketId(job3), 0)

    def testBucket(self):
        job_input1 = self.CreateJobInput('J100', ['J200'], 6, 10)

        scheduler = job_scheduler.JobScheduler(3, 1)

        scheduler.ScheduleJob(job_input1)

        job1 = scheduler._jobs['J100']

        scheduler.highest_priority = 1
        job1.priority = 1
        self.assertEqual(scheduler.FindBucketId(job1), 0)

        scheduler.highest_priority = 10
        job1.priority = 3

        # Verify that with highest priority of 10, 3 blocks are created of size 4 i.e. [0-3], [4-7] [8-11]
        self.assertEqual(scheduler.FindBucketId(job1), 0)

        job1.priority = 5
        self.assertEqual(scheduler.FindBucketId(job1), 1)

        job1.priority = 8
        self.assertEqual(scheduler.FindBucketId(job1), 2)

        # Verify for highest priority job, we get right bucket.
        scheduler.highest_priority = 10
        job1.priority = 10
        self.assertEqual(scheduler.FindBucketId(job1), 2)

    # Multi bucket & Multi CPU
    def testSimpleMultipleBucketMultipleCPU(self):
        job_input1 = self.CreateJobInput('J100', ['J200'], 6, 10)
        job_input2 = self.CreateJobInput('J200', [], 12, 10)
        job_input3 = self.CreateJobInput('J300', ['J200'], 2, 10)

        scheduler = job_scheduler.JobScheduler(2, 2)

        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)
        scheduler.ScheduleJob(job_input3)

        scheduler.Run()

        # Verify that J200 is in higher bucket and other job couldn't execute because J200 needs to complete first.
        self.assertEqual(scheduler.total_time_elapsed, 18)
        self.assertEqual(scheduler.NumJobs(), 0)


    def testSimpleMultipleBucketMultipleCPU(self):
        job_input1 = self.CreateJobInput('J100', ['J200'], 6, 10)
        job_input2 = self.CreateJobInput('J200', [], 12, 10)
        job_input3 = self.CreateJobInput('J300', ['J200'], 2, 10)

        scheduler = job_scheduler.JobScheduler(2, 2)

        scheduler.ScheduleJob(job_input1)
        scheduler.ScheduleJob(job_input2)
        scheduler.ScheduleJob(job_input3)

        job1 = scheduler._jobs['J100']
        job2 = scheduler._jobs['J200']
        job3 = scheduler._jobs['J300']

        scheduler.Run()

        # Verify that J200 is in higher bucket and other job couldn't execute because J200 needs to complete first.
        self.assertEqual(scheduler.total_time_elapsed, 18)
        self.assertEqual(scheduler.NumJobs(), 0)


# suite = unittest.TestLoader().loadTestsFromTestCase(JobSchedulerTest)
# unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    unittest.main()
