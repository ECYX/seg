#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
process data into trainform or testform
Copyright 2017 Yanxu Chen
"""

# import process
# # testdata='患者：男26，右手小母指有水泡，发复发作，用药效果不明显。用啥药能行？？医生：你好！就这一个手指吗？患者：就这一点医生：你好，你这个可以先查查真菌看看是否是手气？也就是手癣'
# # w=open('test.txt','w')
# # w.write(testdata)

# templates_paw = open('template')
# templates = []
# for line in templates_paw:
# 	templates.append(line)
# X = open('test1.txt')
# ww = open('testtemp.txt','a')
# for line in X:
# 	line = line.decode('utf8')
# 	for i in range(len(line)):
# 		ww.write((line[i]+'\n').encode('utf8'))
# ww.close()
# X = open('testtemp.txt')
# w = open('testfm.txt','w')
# process.apply_templates(X, templates, 'r',w)
# w.close()

# crfsuite tag -m train_ctb.model testfm.txt ->123.txt

w1 = open('testtemp.txt').readlines()
w2 = open('123.txt').readlines()
w = open('result.txt','a')
# print len(w1)
# print len(w2)
for i in range(len(w1)):
	w.write(w1[i][:-1]+w2[i])
