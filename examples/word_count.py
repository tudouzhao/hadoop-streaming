# -- coding: utf-8 --

import os
import sys
from core import context

func = lambda x: x+1
print func(1)

#第一步，读取输入:
hc = context.HadoopContext()
input_path = 'input'

#根据job名称，会自行在本地生成一个存储自身mapper和job的目录
def func1(x):
    line = str(x)
    if len(line.split('\t')) == 4:
        return line.split('\t')
    else :
        return [line]


hc.text(input_path).map(lambda x : func1(x)).reduce()






