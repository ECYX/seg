#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
process data into trainform or testform
Copyright 2017 Yanxu Chen
"""
def conver_data(i,quesdata,templates):
	result=''
	for line in range(len(templates)):
		u1 = templates[line].split('\t\t')
		if len(u1) > 1:
			u2 = u1[0].split('\t')
			result +=  'f'+str(line)+'=' + quesdata[(i +int(u2[0])+1)%len(quesdata)][int(u2[1])]+ '/'
			for t in range(1, len(u1)-1):
				u2 = u1[t].split('\t')
				result +=quesdata[(i + int(u2[0])+1)%len(quesdata)][int(u2[1])] + '/'
			u2 = u1[-1].split('\t')
			result += quesdata[(i + int(u2[0])+1)%len(quesdata)][int(u2[1])]+'\t'
		else:
			u2 = u1[-1].split('\t')
			result +=  'f'+str(line)+'=' + quesdata[(i +int(u2[0])+1)%len(quesdata)][int(u2[1])]+'\t'
	return result[:-1]


def apply_templates(X, templates,type,w):
	"""
	type = 'r' means that this is for traindata
	type = 'w' means that this is for testdata
	"""
	result = ''
	quesdata = []
	quesdata.append(['_BOS_'])
	quesdata.append(['_BOS_'])
	for line in X:
		if line == '\n':
			quesdata.append(['_EOS_'])
			quesdata.append(['_EOS_'])
			for i in range(1,len(quesdata)-3):
				if type == 'w':
					result += str(quesdata[i+1][-1])+'\t'
				result += conver_data(i, quesdata, templates) + '\n'
			result += '\n'
			quesdata = []
			quesdata.append(['_BOS_'])
			quesdata.append(['_BOS_'])
			continue
		tempdata = line.split('\t')
		temp_ques=[]
		for tt in range(len(tempdata)):
			temp_ques.append(tempdata[tt].replace('\n',''))
		quesdata.append(temp_ques)
		w.write(result)
		result=''
	quesdata.append(['_EOS_'])
	quesdata.append(['_EOS_'])
	for i in range(1,len(quesdata)-3):
		if type == 'w':
			result += str(quesdata[i+1][-1])+'\t'
		result += conver_data(i, quesdata, templates) + '\n'
	w.write(result)
	result=''
def process_ctb(w1,w2,code):
	w = open(w1)
	temp=[]
	t=0
	www=open(w2,'w')
	www.close()
	www=open(w2,'a')
	for line in w:
		index = 0
		index2=0
		newdata=''
		# print line 
		if t % 1000==0:
			print t
		t+=1
		line = line.decode(code)
		temp = line.split(' ')
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
# w=open('template','w')
# w.write('-2\t0\n-1\t0\n0\t0\n1\t0\n2\t0\n-2\t0\t\t-1\t0\t\t0\t0\n-1\t0\t\t0\t0\t\t1\t0\n0\t0\t\t1\t0\t\t2\t0\n-2\t0\t\t-1\t0\n-1\t0\t\t0\t0\n0\t0\t\t1\t0\n1\t0\t\t2\t0\n-2\t0\t\t0\t0\n-1\t0\t\t1\t0\n0\t0\t\t2\t0\n')
# w.close()
# w=open('data.txt','w')
# w.write('我\n爱\n北\n京\n天\n安\n门\n，\n天\n安\n门\n是\n我\n家\n\n我\n是\n一\n个\n大\n好\n人\n')
# w.close()
# w=open('data1.txt','w')
# w.write('我\t0\n爱\t0\n北\t0\n京\t0\n天\t0\n安\t0\n门\t0\n，\t0\n天\t0\n安\t0\n门\t0\n是\t0\n我\t0\n家\t0\n\n我\t0\n是\t0\n一\t0\n个\t0\n大\t0\n好\t0\n人\t0\n')
# w.close()
if __name__ == '__main__':
	templates_paw = open('template')
	templates = []
	for line in templates_paw:
		templates.append(line)
	process.process_ctb('CTB_all_integration.txt','ctb.txt','utf8')
	X = open('ctb.txt')
	w = open('traindata.txt','w')
	apply_templates(X, templates, 'w',w)
	w.close()

# crfsuite learn -m train_ctb.model -a lbfgs traindata.txt