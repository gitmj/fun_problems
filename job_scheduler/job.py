"""Job class to incorporate all data related to new job.

This class has unique job id, set of parent jobs, set
"""

import job_id
import logging
from job_input import JobInput

class Job:
    def __init__(self, job_input):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='./job.log',
                            filemode='w')

        self.name = job_input.name
        self._parents = set()
        self._childs = set()
        self._childs_name = set()
        # New id will be assinged in UpdatePriority
        self.job_id = 0
        # This will be set to True if all childs jobs are done.
        # Two conditios: 1) _childs set is empty 2) This job does not have any future childs.
        self.ready_to_run = False
        # It gets updated at each tick.
        self.run_time = 0
        self.is_done = False
        self.expected_time_to_finish_secs = job_input.expected_time
        self._deadline_secs = job_input.deadline

        self.priority = 0

    def UpdatePriority(self):
        """
        Based on job dependency set priority of job.
        Note: If this job is child job of any other job then this function should get called.
        If this is new job then self.priority = parent.priority + 1
        if this it's existing job then self.priority + 1.
        Also, check if deadlock before setting the priority.

        :return: True if success, false otherwise.
        """
        return
        if self.job_id == 0:
            # New job
            self.job_id = job_id.NextJobId()
            # Go through all parents and sum it up.
            priority = 1
            if not self._parents:
                self.priority = 1
                return

            # If there are list of parents then sum it up so that this job becomes important than parent jobs.
            for p in self._parents:
                priority = priority + p.priority
            self.priority = priority
        else:
            # if it's existing job then update the priority by 1.
            self.priority = self.priority + 1

        return

    #def Update(self, job_desc):
        # Update childs of this job.
        """for child_job in job_desc.child_ptrs:
            self.AddChild(child_job)
            # Update parents of all child jobs.
            child_job.AddParent(self)
        """
        # Update Priorities.
     #   self.UpdatePriority()
     #   return

    def Clear(self):
        # Clear all job parameters.
        self._parents.clear()
        self._childs_name.clear()
        self._childs.clear()

    def AddParent(self, parent_job):
        self._parents.add(parent_job)

    def RemoveParent(self, parent_job):
        self._parents.remove(parent_job)

    def AddChild(self, name, child_job):
        self._childs_name.add(name)
        self._childs.add(child_job)

    def AddChildName(self, name):
        self._childs_name.add(name)

    def RemoveChild(self, name, child_job):
        self._childs_name.remove(name)
        if child_job:
            self._childs.remove(child_job)

    def NumChilds(self):
        return len(self._childs_name)

    def UpdateRunTime(self, time_elapsed):
        self.run_time += time_elapsed




