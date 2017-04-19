#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
process data into trainform or testform
Copyright 2017 Yanxu Chen
"""
import process
# testdata='患者：男26，右手小母指有水泡，发复发作，用药效果不明显。用啥药能行？？医生：你好！就这一个手指吗？患者：就这一点医生：你好，你这个可以先查查真菌看看是否是手气？也就是手癣'
# w=open('test.txt','w')
# w.write(testdata)
templates_paw = open('template')
templates = []
for line in templates_paw:
	templates.append(line)
process.process_ctb('199801.txt','199801_fm.txt','gbk')

X = open('199801_fm.txt')
w = open('traindata_199801.txt','w')
process.apply_templates(X, templates, 'w',w)
w.close()

# crfsuite tag -m train_ctb.model testfm.txt ->123.txt
# nohup crfsuite learn -m train1.model -a lbfgs traindata.txt > ctb0.log 2>&1 &
# nohup crfsuite learn -m train2.model -a lbfgs ctb1998.txt > ctb1998.log 2>&1 &
 