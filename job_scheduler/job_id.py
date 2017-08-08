"""Creates globally unique id for each new job.

Maintains a bank of incrementing job id assigned to new jobs.
"""

" Global job id which is continusualy incrementing"
job_id = 0


def NextJobId():
    global job_id
    job_id += 1
    return job_id