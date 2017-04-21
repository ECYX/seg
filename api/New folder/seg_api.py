#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
process data into trainform or testform
Copyright 2017 Yanxu Chen
"""
import os
import process
import crfsuite

def contemp2result(w1,w2,w3):
	x1 = open(w1)
	word_list=[]
	for line in x1:
		word_list.append(line[:-1])
	x2 = open(w2)
	tag_list=[]
	for line in x2:
		tag_list.append(line[:-1])
	x3 = open(w3,'w')
	x3.close()
	x3 = open(w3,'a')
	result = ''
	print len(word_list) 
	print len(tag_list)
	for i in range(len(word_list)):
		x3.write(word_list[i])
		if tag_list[i] == 'E' or tag_list[i] == 'S':
			x3.write('\t')
	x3.close()

def get_temp_result(w1,w2):
	templates_paw = open('template')
	templates = []
	for line in templates_paw:
		templates.append(line)
	X = open(w1)
	ww = open('test0temp.txt','a')
	for line in X:
		line = line.decode('utf8')
		for i in range(len(line)):
			ww.write((line[i]+'\n').encode('utf8'))
	ww.close()
	X = open('test0temp.txt')
	w = open('test0fm.txt','w')
	process.apply_templates(X, templates, 'r',w)
	w.close()
	os.system('crfsuite tag -m train_0419.model test0fm.txt > result.txt')
	contemp2result('test0temp.txt', 'result.txt', w2)
	os.system('rm *.txt')
def main():
	w1 = 'test'
	w2 = 'result'
	get_temp_result(w1,w2)
if __name__ == '__main__':
	main()