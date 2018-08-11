from job_context import hadoop_job
class dag_scheduler():
    def __init__(self):
        self._job_list = []
    def add(self,job):
        self._job_list.append(job)

    def summit_job(self):
        for job in self._job_list:
            if type(job) is job :
                #提交一次任务：
                hadoop_job.Hadoop_job(job).submit()



