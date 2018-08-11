# -- coding: utf-8 --

import dag_scheduler
#for every job,defines an HadoopContext:
class HadoopContext():
    def __init__(self):
        self.dag = dag_scheduler()
    #two functions to load input path
    def text(self,input_path):
        self.input_path = input_path
        print input_path
        return self
    def parallelize(self,iterable):
        self.input_list = iterable
        print iterable
        return self

#每次遇到一个map操作，都会生成一个mapper
    def map(self,func):
        pass


#每次遇到一个reducer，都会生成一个reducer：
#加载下来之后，后面会继续计算和生成job














    #here,must produce an mapper.py according your files
    #of courese, an reduce.py will be produced at the same time







