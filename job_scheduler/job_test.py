import unittest
from job import Job
from job_input import JobInput

def CreateJobInput(name):
    job_input = JobInput()
    job_input.name = name
    return job_input

class JobTest(unittest.TestCase):
    def testJobId(self):
        """
        Test that newly created jobs get incremental ids.

        :return: None
        """
        job1 = Job(CreateJobInput('J1'))
        job1.UpdatePriority()
        job2 = Job(CreateJobInput('J2'))
        job2.UpdatePriority()

        self.assertEqual(job1.job_id + 1, job2.job_id)

    def testPriorityOfNewJob(self):
        """
        Test that priority of new job without any dependency get set to 1.
        :return: None
        """
        job1 = Job(CreateJobInput('J1'))
        job1.UpdatePriority()
        self.assertEqual(job1.priority, 1)

    def testPriorityOfExistingJob(self):
        job1 = Job(CreateJobInput('J1'))
        job1.UpdatePriority()
        self.assertEqual(job1.priority, 1)
        job1.UpdatePriority()
        self.assertEqual(job1.priority, 2)

    def testPriorityOfJobWithParents(self):
        parent_job1 = Job(CreateJobInput('J1'))
        parent_job1.UpdatePriority()
        self.assertEqual(parent_job1.priority, 1)
        job1 = Job(CreateJobInput('J1'))
        job1.AddParent(parent_job1)
        job1.UpdatePriority()
        self.assertEqual(job1.priority, 2)
        # Add another parent and verify priority.
        parent_job2 = Job(CreateJobInput('J2'))
        parent_job2.UpdatePriority()
        self.assertEqual(parent_job2.priority, 1)
        job1.AddParent(parent_job2)
        job1.UpdatePriority()
        self.assertEqual(job1.priority, 3)


if __name__ == '__main__':
    unittest.main()