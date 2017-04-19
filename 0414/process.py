w1=open('1_1.txt')
w2=open('1_2.txt')
w3=open('1_3.txt')
ww1=open('PHA_COM_BASEINFO_pinyin.txt','a')
ww2=open('PHA_COM_BASEINFO_wubi.txt','a')

# temp1 = []
# temp2 = []
# i=0
# for line in w1:
# 	temp1.append(line)
# for line in w2:
# 	temp2.append(line)
# for i in range(len(temp1)):
# 	temp = []
# 	temp = temp1[i].split('"')
# 	tempdata = ''
# 	if temp[-2]!='REGULAR_NAME':
# 		tempdata += temp[-2] + '\t'
# 		temp = []
# 		temp = temp2[i].split('"')
# 		tempdata += temp[-2] + '\n'
# 		ww1.write(tempdata)




temp1 = []
temp2 = []
i=0
for line in w1:
	temp1.append(line)
for line in w3:
	temp2.append(line)
for i in range(len(temp1)):
	temp = []
	temp = temp1[i].split('"')
	tempdata = ''
	if temp[-2]!='REGULAR_NAME':
		tempdata += temp[-2] + '\t'
		temp = []
		temp = temp2[i].split('"')
		tempdata += temp[-2] + '\n'
		ww2.write(tempdata)