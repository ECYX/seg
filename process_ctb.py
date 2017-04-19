#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
process data into trainform or testform
Copyright 2017 Yanxu Chen
"""
w = open('CTB_all_integration.txt')
temp=[]
t=0
www=open('ctb.txt','a')
for line in w:
	index = 0
	index2=0
	newdata=''
	# print line 
	if t % 1000==0:
		print t
	t+=1
	line=line.decode('utf8')
	temp=line.split(' ')
	for index in range(len(temp)-1):
		if len(temp[index]) == 1:
			newdata += temp[index]+'\tS\n'
		else:
			newdata += temp[index][0] +'\tB\n'
			for index2 in range(1,len(temp[index])-1):
				newdata += temp[index][index2] +'\tI\n'
			newdata += temp[index][-1] +'\tE\n'

	www.write(newdata.encode('utf8'))
	www.write('\n')