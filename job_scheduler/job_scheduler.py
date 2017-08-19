"""
Main Job scheduler class which takes jobs as input and schedule it on available CPU's.
"""
from job import Job
from job_input import JobInput

import logging


_TIME_TICK_SECS = 2
_MAX_BUCKET_TIME = 10

class JobScheduler:
    def __init__(self, B, N):
        """
        Initialize system level parameters for JobScheduler.

        :param B: Number of priority buckets for various jobs.
            Higher the index, higher the priority of bucket.
        :param N: Number of CPU's.
        """
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='./job_scheduler.log',
                            filemode='w')

        self._priority_bucket = [[]]
        if B == 0:
            # Atleast one bucket please.
            assert(False)

        #for i in range(B - 1):
        #    self._priority_bucket.append([])

        # self._num_buckets = B
        self._num_cpu = N
        # To hold all active jobs.
        # Key is name and value is Job pointer.
        self._jobs = dict()
        # Maintains the list of all parents in value so that they could be updated when job gets created.
        self._child_to_parents = dict()
        # To keep all dependencies.
        # TODO: Delete childs and parents from job scheduler.
        # Key is Job node ptr and value is list of childs.
        self._childs = dict()
        # Key is Job node ptr and value is list of parents.
        self._parents = dict()

        # Total time elapsed by system.
        self.total_time_elapsed = 0

        # self.highest_priority = 0


    def ExecuteJobs(self, bucket_num):
        finished_jobs = set()
        cpu_assigned = 0
        bucket_start_time = self.total_time_elapsed

        for job_ptr in self._priority_bucket[bucket_num]:
            if self._num_cpu > 1:
                # Multi-cpu calculation
                cpu_assigned += 1
                if cpu_assigned == len(self._priority_bucket[bucket_num]):
                    self.total_time_elapsed += _TIME_TICK_SECS
                    cpu_assigned = 0
            else:
                self.total_time_elapsed += _TIME_TICK_SECS
            logging.debug('Total time: %d' % self.total_time_elapsed)

            job_ptr.UpdateRunTime(_TIME_TICK_SECS)
            logging.debug(
                'Job ' + job_ptr.name + ' run time %d' % job_ptr.run_time
                + ' expected time: %d' % job_ptr.expected_time_to_finish_secs)

            if job_ptr.run_time >= job_ptr.expected_time_to_finish_secs:
                finished_jobs.add(job_ptr)

            # If bucket time is over then break the loop.
            if self.total_time_elapsed - bucket_start_time >= _MAX_BUCKET_TIME:
                break

        # Remove finished jobs from bucket.
        for job_ptr in finished_jobs:
            # TODO: What happens if there are two job_ptr in list.
            self._priority_bucket[bucket_num].remove(job_ptr)
            job_ptr.is_done = True
            # TODO:
            # 1. Update parents of job about finished status so that more jobs gets eligible to run.
            # 2. Remove finished jobs from system.
            self.JobDone(job_ptr)

        finished_jobs.clear()

    def Run(self):
        """
        Run the main loop of Job Scheduler to schedule all input jobs. This imitates CPU fetch when next CPU is
        available. It sleeps for given time of job and then removes it from queue and fetches next job, untill all jobs
        are finished.

        In real life, this function will run in separate thread and continues to fetch jobs from queue. Here, we call it
        once on demand to show how jobs are being executed.
        :return:
        """

        while(True):
            all_buckets_empty = True
            # for bucket_num in xrange(self._num_buckets - 1, -1, -1):
            for bucket_num, _ in reversed(list(enumerate(self._priority_bucket))):
                self.ExecuteJobs(bucket_num)
                # if all buckets are empty then return.
                if len(self._priority_bucket[bucket_num]):
                    all_buckets_empty = False
            if all_buckets_empty:
                return

    def JobDone(self, job_ptr):
        # Remove itself from it's parent dependency so that it could be scheduled.
        self.RemoveChildToParentsMap(job_ptr)

        # There shouldn't by any child
        assert(self._jobs[job_ptr.name].NumChilds() == 0)

        del self._jobs[job_ptr.name]

    def _IsDeadlock(self, job):
        """
        Check if there is circular dependency with jobs.

        :param job: job of type Job class with dependent jobs listed.

        :return: True if Deadlock detected, false otherwise.
        """
    def NumJobs(self):
        return len(self._jobs)

    def ScheduleJob(self, job_input):
        """

        :param job_input: Details of job. It must be unique otherwise existing job will be updated with new parameters.

        :return: True if job successfully added to scheduling queue, false otherwise.
        """
        job_ptr = None
        if job_input.name in self._jobs:
            # Existing jobs. Job may be updated in terms if it's dependencies, time etc.
            # Update all checks and update the job.
            job_ptr = self._jobs[job_input.name]
            logging.debug('Clearing existing job: ' + job_input.name)
            job_ptr.Clear()
            return True
        else:
            # Create new job.
            job_ptr = Job(job_input)
            self._jobs[job_input.name] = job_ptr
            logging.debug('New job created: ' + job_input.name)

        # Maintains the map from child to all its parents.
        self.AddChildToParentsMap(job_input)

        # Update childs of this job.
        # It updates the pointer nodes if job exists.
        self.UpdateChilds(job_input)

        # Update parents of this job
        self.UpdateParents(job_ptr)

        # Update Priority
        self.UpdatePriority(job_ptr)

        # Put the job in appropriate bucket based on priority.
        self.PutOnBucket(job_ptr)
        return True

    def CheckReadiness(self, job_ptr):
        if job_ptr.NumChilds() == 0:
            job_ptr.ready_to_run = True

    def FindBucketId(self, job_ptr):

        if len(self._priority_bucket) > job_ptr.priority:
            return job_ptr.priority - 1
        else:
            while(len(self._priority_bucket) < job_ptr.priority):
                self._priority_bucket.append([])
            return job_ptr.priority - 1

        """
        
        :param job_ptr: 
        :return: 
        # Last block will cover any uneven distributions.
        block_size = self.highest_priority / self._num_buckets

        if self._num_buckets == 1 or block_size == 0:
            # Put all jobs in same bucket
            return 0

        if self.highest_priority % self._num_buckets:
            block_size += 1

        bucket_id = job_ptr.priority / block_size

        if block_size == 1:
            bucket_id -= 1
        """

        return bucket_id

    def PutOnBucket(self, job_ptr):
        self.CheckReadiness(job_ptr)
        if job_ptr.ready_to_run:
            bucket_num = self.FindBucketId(job_ptr)
            """
            if bucket_num >= self._num_buckets:
                logging.debug(job_ptr.priority)
                logging.debug(self.highest_priority)
                logging.debug(self._num_buckets)
                logging.error(
                    'bucket num: %d' % bucket_num + ' came out beyond configured size %d' % len(self._priority_bucket)
                    + 'job priority: %d' % job_ptr.priority + 'higest: %d' % self.highest_priority
                    + 'bucket %d' % self._num_buckets)
                assert(False)
                return
            """

            logging.debug('Adding job: ' + job_ptr.name + ' to bucket # ' + str(bucket_num))
            self._priority_bucket[bucket_num].append(job_ptr)


    def AddChildToParentsMap(self, job_input):
        for child in job_input.child_names:
            parent_jobs = self._child_to_parents.get(child)
            if parent_jobs:
                logging.debug('Adding to existing parent set : ' + job_input.name + ' child: ' + child)
                parent_jobs.add(job_input.name)
            else:
                logging.debug('Creating new parent set : ' + job_input.name + ' child: ' + child)
                self._child_to_parents[child] = set([job_input.name])

    def RemoveChildToParentsMap(self, job_ptr):
        parent_jobs = self._child_to_parents.get(job_ptr.name)
        if parent_jobs == None:
            # This is valid for jobs with no children.
            return
        for parent in parent_jobs:
            parent_job_ptr = self._jobs[parent]
            if not parent_job_ptr:
                logging.error('Unexpected parent ptr missing, name: ' + parent)
                return
            parent_job_ptr.RemoveChild(job_ptr.name, job_ptr)
            logging.debug('Removed parent ' + parent + ' child ' + job_ptr.name + ' Num childs %d' % parent_job_ptr.NumChilds())
            # Check if parent is ready to run.
            self.PutOnBucket(parent_job_ptr)


    # Find out parents of this job and update their pointers.
    def UpdateParents(self, job_ptr):
        # Update all parents of this job
        parent_jobs = self._child_to_parents.get(job_ptr.name)
        if not parent_jobs:
            # This is valid for jobs with no children.
            return
        for parent in parent_jobs:
            # Update parent with this new child job.
            parent_job_ptr = self._jobs.get(parent)
            if parent_job_ptr:
                parent_job_ptr.AddChild(job_ptr.name, job_ptr)
                logging.debug(
                    'Update Parents: ' + parent_job_ptr.name + ' child: ' + job_ptr.name)

    def UpdatePriority(self, job_ptr):
        old_priority = job_ptr.priority
        # Have to start with 1 because if priority starts with 0 and then this.priority(0) + parent.priority(0) becomes 0.
        # If you start with 1, then this.priority(1) + parent.priority(1)
        # Basically, inheriting from parent would become complicated.
        job_ptr.priority = 1

        # First inherits priority from parents.
        parent_jobs = self._child_to_parents.get(job_ptr.name)
        if parent_jobs:
            # This is valid for jobs with no children.
            for parent in parent_jobs:
                parent_job_ptr = self._jobs.get(parent)
                # UpdatePriority
                job_ptr.priority = job_ptr.priority + parent_job_ptr.priority
                # Update highest priority job so that jobs could be scheduled in appr. bucket.
                # if self.highest_priority < job_ptr.priority:
                #    self.highest_priority = job_ptr.priority
                #    logging.debug('highest priority: %d' % self.highest_priority)
                logging.debug(
                    'Inherit priority from parent: ' + parent_job_ptr.name + ' priority: %d' % parent_job_ptr.priority + ' child: ' + job_ptr.name + ' priority: %d' % job_ptr.priority)

        # Now, update priority of childs.
        if old_priority != job_ptr.priority:
            for child in job_ptr._childs:
                self.UpdatePriority(child)
                # if self.highest_priority < child.priority:
                #    self.highest_priority = child.priority
                #    logging.debug('highest priority: %d' % self.highest_priority)
                logging.debug('Updating priority of ' + child.name + ' priority %d' % child.priority)

    def UpdateChilds(self, job_input):
        job_ptr = self._jobs[job_input.name]
        assert(job_ptr != None)
        for child_name in job_input.child_names:
            # Update child pointers.
            child_ptr = self._jobs.get(child_name)
            if child_ptr:
                logging.debug('Adding child: ' + child_ptr.name + ' to parent: ' + job_input.name)
                job_ptr.AddChild(child_ptr.name, child_ptr)
            else:
                logging.debug('Adding child without pointer: ' + child_name)
                job_ptr.AddChildName(child_name)

    def ReadInput(self, input_file_name):
        """Input format
        First Job Name, expected time, deadline
        followed by child Jobs.

        In case of no dependencies, there won't be any child jobs after deadline.
        """
        file = open(input_file_name, 'r')
        for line in file:
            arr = line.strip().split()
            job_input = JobInput()
            job_input.name = arr[0]
            job_input.expected_time = arr[1]
            job_input.deadline = arr[2]
            job_input.child_names = set()
            if len(arr) > 3:
                for dep in arr[2:]:
                    job_input.child_names.add(dep)
            self.ScheduleJob(job_input)
