# #coding=utf-8
# w1=open('test_text.txt')
# w2=open('test.txt','a')
# temp1 = []
# temp2 = []
# i=0
# for line in w1:
# 	temp1.append(line)
# for i in range(len(temp1)):

# 	temp = []
# 	temp = temp1[i].split('"')
# 	tempdata = temp[3]+'\n'
# 	w2.write(tempdata)

w3 = open('test.txt')
w4 = open('test100.txt','a')
i = 0
for line in w3:
	if i != 100:
		w4.write(line)
		i += 1
	else:
		break