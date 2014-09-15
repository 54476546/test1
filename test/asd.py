#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2014-9-1

@author: Administrator
'''
createVar = locals()
listTemp = range(1,10)
for i,s in enumerate(listTemp):
    createVar['a'+ str(i)] = s
print a1,a2,a3


b = [1, 2, 3, 4, 5]
print b[:len(b) - (5 - 2)]