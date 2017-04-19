import re
import os 
def finds(str,b):
        i=0
        a=[]
        a.append(b.index(str))
        i=1
        m=-1
        while a[-1]<len(b):
            try:
                a.append(b.index(str,a[i-1]+1))
                i+=1
            except ValueError:
                break    
        return a
def filterTerm(term):
	tag = 0
	# 长度小于2则过滤
	if len(term) < 2:
		tag = 1
	# 匹配汉字，无则过滤
	cw = re.compile(u'[\u4e00-\u9fa5]')
	matches = re.findall(cw, term)
	if len(matches) == 0:
		tag = 1
	return tag
def delblank(file_name):
    lines=open(file_name,encoding='utf8').readlines()
    g=''
    for line in lines:
	    if len(line)==0:
	        break
	    if line.count('\n')==len(line):
	        continue
	    g+=line
    return g
kb_with=open('kb_with_link_temp.txt','w',encoding='utf8')
kb_with_link=''
kb_without=open('kb_without_link_temp.txt','w',encoding='utf8')
kb_without_link=''
tempdata=''
homepath = os.getcwd()
path1=r'F:\python work\crawler\disease'
fns=[os.path.join(fn) for root,dirs,files in os.walk(path1) for fn in files]
for f in fns:
	os.chdir(path1)
	html_doc=open(f,encoding='utf8').read()
	label='<h3><a style="color: blue;" name="gs">概述:</a></h3>'
	lable_list=[]
	try:
		lable_list.append(html_doc.index(label))
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass    
	label='<h3><a style="color: blue;" name="lxbx">流行病学:</a></h3>'
	try:
		lable_list.append(html_doc.index(label))
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	label='<h3><a style="color: blue;" name="by">病因:</a></h3>'
	try:
		lable_list.append(html_doc.index(label))
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	label='<h3><a style="color: blue;" name="fbjz">发病机制:</a></h3>'
	try:
		lable_list.append(html_doc.index(label))
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	label='<h3><a style="color: blue;" name="lcbx">临床表现:</a></h3>'
	try:
		lable_list.append(html_doc.index(label))
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	label='<h3><a style="color: blue;" name="bfz">并发症:</a></h3>'
	try:
		lable_list.append(html_doc.index(label))
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	label='<h3><a style="color: blue;" name="sysjc">实验室检查:</a></h3>'
	try:
		lable_list.append(html_doc.index(label))
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	label='<h3><a style="color: blue;" name="qtfzjc">其他辅助检查:</a></h3>'
	try:
		lable_list.append(html_doc.index(label))
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	label='<h3><a style="color: blue;" name="zd">诊断:</a></h3>'
	try:
		lable_list.append(html_doc.index(label))
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	label='<h3><a style="color: blue;" name="jbzd">鉴别诊断:</a></h3>'
	try:
		lable_list.append(html_doc.index(label))
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	label='<h3><a style="color: blue;" name="zl">治疗:</a></h3>'
	try:
		lable_list.append(html_doc.index(label))
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	label='<h3><a style="color: blue;" name="yh">预后:</a></h3>'
	try:
		lable_list.append(html_doc.index(label))
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass
	label='<h3><a style="color: blue;" name="yf">预防:</a></h3>'
	try:
		lable_list.append(html_doc.index(label))
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	os.chdir(homepath) 
	new9=open('temp.txt','w',encoding='utf8') 
	tempdata=''
	for i in range(int(len(lable_list)/2)):
		if i==int(len(lable_list)/2-1):
			tempdata+=html_doc[int(lable_list[2*i+1]):]
		else:
			tempdata+=html_doc[int(lable_list[2*i+1]):int(lable_list[2*i+2])]
	tempdata=tempdata.replace('DIV','div',tempdata.count('DIV'))
	tempdata=tempdata.replace('<div>','',tempdata.count('<div>'))
	tempdata=tempdata.replace('</div>','',tempdata.count('</div>'))
	tempdata=tempdata.replace('<sub>','_',tempdata.count('<sub>'))
	tempdata=tempdata.replace('</sub>','',tempdata.count('</sub>'))
	tempdata=tempdata.replace('<sup>','^',tempdata.count('<sup>'))
	tempdata=tempdata.replace('</sup>','',tempdata.count('</sup>'))	
	tempdata=tempdata.replace('\t','',tempdata.count('\t'))
	tempdata=tempdata.replace('&nbsp;','',tempdata.count('&nbsp;'))
	tempdata=tempdata.replace(' ','',tempdata.count(' '))
	tempdata=tempdata.replace('<i>','',tempdata.count('<i>'))
	tempdata=tempdata.replace('</i>','',tempdata.count('</i>'))
	tempdata=tempdata.replace('&#8226;','',tempdata.count('&#8226;'))
	tempdata=tempdata.replace('&micro;','',tempdata.count('&micro;'))
	new9.write(tempdata)
	new9.close()
	print(f)
	tempdata=delblank('temp.txt')
	tempdata=tempdata[:tempdata.index('</td>')]
	# new9=open('temp.txt','w',encoding='utf8') 
	# new9.write(tempdata)
	# new9.close()
	tempstr=''
	tempcount=-1
	tempmarkstr=''
	temp_entity_type=''
	temp_entity=''
	tempmark=0
	mark=0
	noway=0
	tempcountmark=0
	temp_entity_count=0
	for i in range (len(tempdata)):
		if tempdata[i]=='>' :
			tempmark=2
			if noway==1:
				noway=0
				continue
			if tempdata[i-2]=='/':
				if mark==1:
					if temp_entity_type.replace('"','',temp_entity_type.count('"')) !='disease'and temp_entity_type.replace('"','',temp_entity_type.count('"'))!= 'laboratory' and temp_entity_type.replace('"','',temp_entity_type.count('"'))!='medicine' and temp_entity_type.replace('"','',temp_entity_type.count('"'))!='medicare' :
						continue
					elif len(temp_entity)>25:
						continue
					else:
						if filterTerm(temp_entity)==0:
							tempcountmark=0
							tempmarkstr=tempmarkstr[:-1]+'\t\t'+temp_entity+'\t'+str(begin_place)+'\t'+str(end_place)+'\t'+temp_entity_type.replace('"','',temp_entity_type.count('"'))+'\n'
							temp_entity_type=''
							temp_entity=''
							mark=1
				else:
					if temp_entity_type.replace('"','',temp_entity_type.count('"')) !='disease'and temp_entity_type.replace('"','',temp_entity_type.count('"'))!= 'laboratory' and temp_entity_type.replace('"','',temp_entity_type.count('"'))!='medicine' and temp_entity_type.replace('"','',temp_entity_type.count('"'))!='medicare':
						continue
					else:
						if filterTerm(temp_entity)==0:
							tempcountmark=0
							tempmarkstr+='\t\t\t'+temp_entity+'\t'+str(begin_place)+'\t'+str(end_place)+'\t'+temp_entity_type.replace('"','',temp_entity_type.count('"'))+'\n'
							temp_entity_type=''
							temp_entity=''
							mark=1
			else:
				tempcountmark=1
			continue
		if tempmark==1:
			if temp_entity_count==1:
				if tempdata[i]!='/':
					temp_entity_type+=tempdata[i]
			if tempdata[i]=='=' and tempdata[i-1]=='f':
				temp_entity_count=1
			if tempdata[i]=='/':
				temp_entity_count=0
			continue
		if tempmark==2:
			if tempcountmark==1:
				if tempdata[i]!='<'and tempdata[i]!='>' and tempdata[i]!='。'and tempdata[i]!='；':
					temp_entity+=tempdata[i]
					tempstr+=tempdata[i]
					tempcount+=1
		if tempdata[i]=='<' :
			if tempcountmark==1:
				end_place=tempcount
				begin_place=tempcount-len(temp_entity)
			elif tempdata[i+1]!='a' or tempdata[i+2]!='h' and tempdata[i+3]!='r':
				noway=1
			tempmark=1
			continue
		if tempdata[i]=='；'or tempdata[i]=='。'or tempdata[i]=='\n'or tempdata[i]==';':
			if tempdata[i]!='\n':
				tempstr+=tempdata[i]
				tempcount+=1
			if mark==1:
				if tempstr!=';\n':
					kb_with_link+=tempstr+tempmarkstr
					tempstr=''
					tempmarkstr=''
					mark=0
					tempcount=0
			if mark==0:
				if tempstr!=';\n':
					kb_without_link+=tempstr+'\n'
					tempstr=''
					mark=0
					tempcount=0
		else:
			if tempcountmark!=1:
				tempstr+=tempdata[i]
				tempcount+=1
path2=r'F:\python work\crawler\laboratory'
fns=[os.path.join(fn) for root,dirs,files in os.walk(path2) for fn in files]
for f in fns:
	os.chdir(path2)
	print(f)
	html_doc=open(f,encoding='utf8').read()
	label='<h3><a style="color: blue;" name="gs">概述:</a></h3>'
	lable_list=[]
	try:
		lable_list.append(html_doc.index(label))
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try: 
		label='<h3><a style="color: blue;" name="yl">原理:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n概述:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try: 
		label='<h3><a style="color: blue;" name="shiji">试剂:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n原理:\n'
		tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:    
		label='<h3><a style="color: blue;" name="czff">操作方法:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n试剂:\n'
		tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:    
		label='<h3><a style="color: blue;" name="zcz">正常值:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n操作方法:\n'
		tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:    
		label='<h3><a style="color: blue;" name="lcyy">临床意义:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n正常值:\n'
		tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:    
		label='<h3><a style="color: blue;" name="fz">附注:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n临床意义:\n'
		tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	tempdata+='\n附注:\n'
	tempdata+=html_doc[int(lable_list[-1]):]
	os.chdir(homepath) 
	new9=open('temp.txt','w',encoding='utf8') 
	tempdata=''
	for i in range(int(len(lable_list)/2)):
		if i==int(len(lable_list)/2-1):
			tempdata+=html_doc[int(lable_list[2*i+1]):]
		else:
			tempdata+=html_doc[int(lable_list[2*i+1]):int(lable_list[2*i+2])]
	tempdata=tempdata.replace('DIV','div',tempdata.count('DIV'))
	tempdata=tempdata.replace('<div>','',tempdata.count('<div>'))
	tempdata=tempdata.replace('</div>','',tempdata.count('</div>'))
	tempdata=tempdata.replace('<sub>','_',tempdata.count('<sub>'))
	tempdata=tempdata.replace('</sub>','',tempdata.count('</sub>'))
	tempdata=tempdata.replace('<sup>','^',tempdata.count('<sup>'))
	tempdata=tempdata.replace('</sup>','',tempdata.count('</sup>'))
	tempdata=tempdata.replace('\t','',tempdata.count('\t'))
	tempdata=tempdata.replace('&nbsp;','',tempdata.count('&nbsp;'))
	tempdata=tempdata.replace('<i>','',tempdata.count('<i>'))
	tempdata=tempdata.replace('</i>','',tempdata.count('</i>'))
	tempdata=tempdata.replace(' ','',tempdata.count(' '))
	tempdata=tempdata.replace('&#8226;','',tempdata.count('&#8226;'))
	tempdata=tempdata.replace('&micro;','',tempdata.count('&micro;'))
	tempdata=tempdata.replace('&ouml;','',tempdata.count('&ouml;'))
	new9.write(tempdata)
	new9.close()
	tempdata=delblank('temp.txt')
	tempdata=tempdata[:tempdata.index('</td>')]
	# new9=open('temp.txt','w',encoding='utf8') 
	# new9.write(tempdata)
	# new9.close()
	tempstr=''
	tempcount=-1
	tempmarkstr=''
	temp_entity_type=''
	temp_entity=''
	tempmark=0
	mark=0
	tempcountmark=0
	temp_entity_count=0
	for i in range (len(tempdata)):
		if tempdata[i]=='>' :
			tempmark=2
			if noway==1:
				noway=0
				continue
			if tempdata[i-2]=='/':
				if mark==1:
					if temp_entity_type.replace('"','',temp_entity_type.count('"')) !='disease'and temp_entity_type.replace('"','',temp_entity_type.count('"'))!= 'laboratory' and temp_entity_type.replace('"','',temp_entity_type.count('"'))!='medicine' and temp_entity_type.replace('"','',temp_entity_type.count('"'))!='medicare':
						continue
					else:
						if filterTerm(temp_entity)==0:
							tempcountmark=0
							tempmarkstr=tempmarkstr[:-1]+'\t\t'+temp_entity+'\t'+str(begin_place)+'\t'+str(end_place)+'\t'+temp_entity_type.replace('"','',temp_entity_type.count('"'))+'\n'
							temp_entity_type=''
							temp_entity=''
							mark=1
						elif filterTerm(temp_entity)==1:
							continue
				else:
					if temp_entity_type.replace('"','',temp_entity_type.count('"')) !='disease'and temp_entity_type.replace('"','',temp_entity_type.count('"'))!= 'laboratory' and temp_entity_type.replace('"','',temp_entity_type.count('"'))!='medicine' and temp_entity_type.replace('"','',temp_entity_type.count('"'))!='medicare':
						continue
					else:
						if filterTerm(temp_entity)==0:
							tempcountmark=0
							tempmarkstr+='\t\t\t'+temp_entity+'\t'+str(begin_place)+'\t'+str(end_place)+'\t'+temp_entity_type.replace('"','',temp_entity_type.count('"'))+'\n'
							temp_entity_type=''
							temp_entity=''
							mark=1
						else:
							continue
			else:
				tempcountmark=1
			continue
		if tempmark==1:
			if temp_entity_count==1:
				if tempdata[i]!='/':
					temp_entity_type+=tempdata[i]
			if tempdata[i]=='=' and tempdata[i-1]=='f':
				temp_entity_count=1
			if tempdata[i]=='/':
				temp_entity_count=0
			continue
		if tempmark==2:
			if tempcountmark==1:
				if tempdata[i]!='<'and tempdata[i]!='>' and tempdata[i]!='。'and tempdata[i]!='；':
					temp_entity+=tempdata[i]
					tempstr+=tempdata[i]
					tempcount+=1
		if tempdata[i]=='<' :
			if tempcountmark==1:
				end_place=tempcount
				begin_place=tempcount-len(temp_entity)
			elif tempdata[i+1]!='a' or tempdata[i+2]!='h' and tempdata[i+3]!='r':
				noway=1
			tempmark=1
			continue
		if tempdata[i]=='；'or tempdata[i]=='。'or tempdata[i]=='\n'or tempdata[i]==';':
			if tempdata[i]!='\n':
				tempstr+=tempdata[i]
				tempcount+=1
			if mark==1:
				if tempstr!=';\n':
					kb_with_link+=tempstr+tempmarkstr
					tempstr=''
					tempmarkstr=''
					mark=0
					tempcount=0
			if mark==0:
				if tempstr!=';\n':
					kb_without_link+=tempstr+'\n'
					tempstr=''
					mark=0
					tempcount=0
		else:
			if tempcountmark!=1:
				tempstr+=tempdata[i]
				tempcount+=1
path3=r'F:\python work\crawler\medicare'
fns=[os.path.join(fn) for root,dirs,files in os.walk(path3) for fn in files]
for f in fns:
	os.chdir(path3)
	print(f)
	html_doc=open(f,encoding='utf8').read()
	label='<h3><a style="color: blue;" name="ylzy">药理作用:</a></h3>'
	lable_list=[]
	tempdata=''
	try:
		lable_list.append(html_doc.index(label))
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:    
		label='<h3><a style="color: blue;" name="ydx">药动学:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n药理作用:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:    
		label='<h3><a style="color: blue;" name="syz">适应证:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n药动学:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:    
		label='<h3><a style="color: blue;" name="jjz">禁忌证:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n适应证:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:    
		label='<h3><a style="color: blue;" name="zysx">注意事项:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n禁忌证:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:    
		label='<h3><a style="color: blue;" name="blfy">不良反应:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n注意事项:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:    
		label='<h3><a style="color: blue;" name="yfyl">用法用量:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n不良反应:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:  
		label='<h3><a style="color: blue;" name="ywxyzy">药物相应作用:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n用法用量:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:   
		label='<h3><a style="color: blue;" name="zjdp">专家点评:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n药物相应作用:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass
	try:     
		tempdata+='\n专家点评:\n'
		tempdata+=html_doc[int(lable_list[-1]):]
	except:
		pass
	os.chdir(homepath)
	new9=open('temp.txt','w',encoding='utf8') 
	# tempdata=''
	# for i in range(int(len(lable_list)/2)):
	# 	if i==int(len(lable_list)/2-1):
	# 		tempdata+=html_doc[int(lable_list[2*i+1]):]
	# 	else:
	# 		tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
	tempdata=tempdata.replace('DIV','div',tempdata.count('DIV'))
	tempdata=tempdata.replace('<div>','',tempdata.count('<div>'))
	tempdata=tempdata.replace('</div>','',tempdata.count('</div>'))
	tempdata=tempdata.replace('<sub>','_',tempdata.count('<sub>'))
	tempdata=tempdata.replace('</sub>','',tempdata.count('</sub>'))
	tempdata=tempdata.replace('<sup>','^',tempdata.count('<sup>'))
	tempdata=tempdata.replace('</sup>','',tempdata.count('</sup>'))
	tempdata=tempdata.replace('\t','',tempdata.count('\t'))
	tempdata=tempdata.replace('&nbsp;','',tempdata.count('&nbsp;'))
	tempdata=tempdata.replace('<i>','',tempdata.count('<i>'))
	tempdata=tempdata.replace('</i>','',tempdata.count('</i>'))
	tempdata=tempdata.replace(' ','',tempdata.count(' '))
	tempdata=tempdata.replace('&#8226;','',tempdata.count('&#8226;'))
	tempdata=tempdata.replace('&micro;','',tempdata.count('&micro;'))
	tempdata=tempdata.replace('&ouml;','',tempdata.count('&ouml;'))
	new9.write(tempdata)
	new9.close()
	tempdata=delblank('temp.txt')
	try:
		tempdata=tempdata[:tempdata.index('</td>')]
	except:
		pass
	# new9=open('temp.txt','w',encoding='utf8') 
	# new9.write(tempdata)
	# new9.close()
	tempstr=''
	tempcount=-1
	tempmarkstr=''
	temp_entity_type=''
	temp_entity=''
	tempmark=0
	mark=0
	tempcountmark=0
	temp_entity_count=0
	for i in range (len(tempdata)):
		if tempdata[i]=='>' :
			tempmark=2
			if noway==1:
				noway=0
				continue
			if tempdata[i-2]=='/':
				if mark==1:
					if temp_entity_type.replace('"','',temp_entity_type.count('"')) !='disease'and temp_entity_type.replace('"','',temp_entity_type.count('"'))!= 'laboratory' and temp_entity_type.replace('"','',temp_entity_type.count('"'))!='medicine' and temp_entity_type.replace('"','',temp_entity_type.count('"'))!='medicare':
						continue
					else:
						if filterTerm(temp_entity)==0:
							tempcountmark=0
							tempmarkstr=tempmarkstr[:-1]+'\t\t'+temp_entity+'\t'+str(begin_place)+'\t'+str(end_place)+'\t'+temp_entity_type.replace('"','',temp_entity_type.count('"'))+'\n'
							temp_entity_type=''
							temp_entity=''
							mark=1
						elif filterTerm(temp_entity)==1:
							continue
				else:
					if temp_entity_type.replace('"','',temp_entity_type.count('"')) !='disease'and temp_entity_type.replace('"','',temp_entity_type.count('"'))!= 'laboratory' and temp_entity_type.replace('"','',temp_entity_type.count('"'))!='medicine' and temp_entity_type.replace('"','',temp_entity_type.count('"'))!='medicare':
						continue
					else:
						if filterTerm(temp_entity)==0:
							tempcountmark=0
							tempmarkstr+='\t\t\t'+temp_entity+'\t'+str(begin_place)+'\t'+str(end_place)+'\t'+temp_entity_type.replace('"','',temp_entity_type.count('"'))+'\n'
							temp_entity_type=''
							temp_entity=''
							mark=1
						else:
							continue
			else:
				tempcountmark=1
			continue
		if tempmark==1:
			if temp_entity_count==1:
				if tempdata[i]!='/':
					temp_entity_type+=tempdata[i]
			if tempdata[i]=='=' and tempdata[i-1]=='f':
				temp_entity_count=1
			if tempdata[i]=='/':
				temp_entity_count=0
			continue
		if tempmark==2:
			if tempcountmark==1:
				if tempdata[i]!='<'and tempdata[i]!='>' and tempdata[i]!='。'and tempdata[i]!='；':
					temp_entity+=tempdata[i]
					tempstr+=tempdata[i]
					tempcount+=1
		if tempdata[i]=='<' :
			if tempcountmark==1:
				end_place=tempcount
				begin_place=tempcount-len(temp_entity)
			elif tempdata[i+1]!='a' or tempdata[i+2]!='h' and tempdata[i+3]!='r':
				noway=1
			tempmark=1
			continue
		if tempdata[i]=='；'or tempdata[i]=='。'or tempdata[i]=='\n'or tempdata[i]==';':
			if tempdata[i]!='\n':
				tempstr+=tempdata[i]
				tempcount+=1
			if mark==1:
				if tempstr!=';\n':
					kb_with_link+=tempstr+tempmarkstr
					tempstr=''
					tempmarkstr=''
					mark=0
					tempcount=0
			if mark==0:
				if tempstr!=';\n':
					kb_without_link+=tempstr+'\n'
					tempstr=''
					mark=0
					tempcount=0
		else:
			if tempcountmark!=1:
				tempstr+=tempdata[i]
				tempcount+=1
path4=r'F:\python work\crawler\medicine'
fns=[os.path.join(fn) for root,dirs,files in os.walk(path4) for fn in files]
for f in fns:
	print(f)
	os.chdir(path4)
	html_doc=open(f,encoding='utf8').read()
	label='<h3><a style="color: blue;" name="ywbm">药物别名:</a></h3>'
	lable_list=[]
	tempdata=''
	try:
		lable_list.append(html_doc.index(label))
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:   
		label='<h3><a style="color: blue;" name="ywjx">药物剂型:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n药物别名:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:    
		label='<h3><a style="color: blue;" name="ylzy">药理作用:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n药物剂型:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:    
		label='<h3><a style="color: blue;" name="ydx">药动学:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n药理作用:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:    
		label='<h3><a style="color: blue;" name="syz">适应证:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n药动学:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:    
		label='<h3><a style="color: blue;" name="jjz">禁忌证:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n适应证:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:    
		label='<h3><a style="color: blue;" name="zysx">注意事项:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n禁忌证:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:  
		label='<h3><a style="color: blue;" name="blfy">不良反应:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n注意事项:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:  
		label='<h3><a style="color: blue;" name="yfyl">用法用量:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n不良反应:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:  
		label='<h3><a style="color: blue;" name="ywxyzy">药物相应作用:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n用法用量:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass   
	try:  
		label='<h3><a style="color: blue;" name="zjdp">专家点评:</a></h3>'
		lable_list.append(html_doc.index(label))
		tempdata+='\n药物相应作用:\n'
		if len(lable_list)>2:
			tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
		lable_list.append(html_doc.index(label)+len(label))
	except ValueError:
		pass
	try:     
		tempdata+='\n专家点评:\n'
		tempdata+=html_doc[int(lable_list[-1]):]
	except:
		pass
	os.chdir(homepath)
	new9=open('temp.txt','w',encoding='utf8') 
	# tempdata=''
	# for i in range(int(len(lable_list)/2)):
	# 	if i==int(len(lable_list)/2-1):
	# 		tempdata+=html_doc[int(lable_list[2*i+1]):]
	# 	else:
	# 		tempdata+=html_doc[int(lable_list[-2]):int(lable_list[-1])]
	tempdata=tempdata.replace('DIV','div',tempdata.count('DIV'))
	tempdata=tempdata.replace('SUB','sub',tempdata.count('SUB'))
	tempdata=tempdata.replace('SUP','sup',tempdata.count('SUP'))
	tempdata=tempdata.replace('<div>','',tempdata.count('<div>'))
	tempdata=tempdata.replace('</div>','',tempdata.count('</div>'))
	tempdata=tempdata.replace('<sub>','_',tempdata.count('<sub>'))
	tempdata=tempdata.replace('</sub>','',tempdata.count('</sub>'))
	tempdata=tempdata.replace('<sup>','^',tempdata.count('<sup>'))
	tempdata=tempdata.replace('</sup>','',tempdata.count('</sup>'))
	tempdata=tempdata.replace('\t','',tempdata.count('\t'))
	tempdata=tempdata.replace('&nbsp;','',tempdata.count('&nbsp;'))
	tempdata=tempdata.replace('<i>','',tempdata.count('<i>'))
	tempdata=tempdata.replace('</i>','',tempdata.count('</i>'))
	tempdata=tempdata.replace(' ','',tempdata.count(' '))
	tempdata=tempdata.replace('&#8226;','',tempdata.count('&#8226;'))
	tempdata=tempdata.replace('&micro;','',tempdata.count('&micro;'))
	new9.write(tempdata)
	new9.close()
	tempdata=delblank('temp.txt')
	tempdata=tempdata[:tempdata.index('</td>')]
	# new9=open('temp.txt','w',encoding='utf8') 
	# new9.write(tempdata)
	# new9.close()
	tempstr=''
	tempcount=-1
	tempmarkstr=''
	temp_entity_type=''
	temp_entity=''
	tempmark=0
	mark=0
	tempcountmark=0
	temp_entity_count=0
	for i in range (len(tempdata)):
		if tempdata[i]=='>' :
			tempmark=2
			if noway==1:
				noway=0
				continue
			if tempdata[i-2]=='/':
				if mark==1:
					if temp_entity_type.replace('"','',temp_entity_type.count('"')) !='disease'and temp_entity_type.replace('"','',temp_entity_type.count('"'))!= 'laboratory' and temp_entity_type.replace('"','',temp_entity_type.count('"'))!='medicine' and temp_entity_type.replace('"','',temp_entity_type.count('"'))!='medicare':
						continue
					else:
						if filterTerm(temp_entity)==0:
							tempcountmark=0
							tempmarkstr=tempmarkstr[:-1]+'\t\t'+temp_entity+'\t'+str(begin_place)+'\t'+str(end_place)+'\t'+temp_entity_type.replace('"','',temp_entity_type.count('"'))+'\n'
							temp_entity_type=''
							temp_entity=''
							mark=1
						elif filterTerm(temp_entity)==1:
							continue
				else:
					if temp_entity_type.replace('"','',temp_entity_type.count('"')) !='disease'and temp_entity_type.replace('"','',temp_entity_type.count('"'))!= 'laboratory' and temp_entity_type.replace('"','',temp_entity_type.count('"'))!='medicine' and temp_entity_type.replace('"','',temp_entity_type.count('"'))!='medicare':
						continue
					else:
						if filterTerm(temp_entity)==0:
							tempcountmark=0
							tempmarkstr+='\t\t\t'+temp_entity+'\t'+str(begin_place)+'\t'+str(end_place)+'\t'+temp_entity_type.replace('"','',temp_entity_type.count('"'))+'\n'
							temp_entity_type=''
							temp_entity=''
							mark=1
						else:
							continue
			else:
				tempcountmark=1
			continue
		if tempmark==1:
			if temp_entity_count==1:
				if tempdata[i]!='/':
					temp_entity_type+=tempdata[i]
			if tempdata[i]=='=' and tempdata[i-1]=='f':
				temp_entity_count=1
			if tempdata[i]=='/':
				temp_entity_count=0
			continue
		if tempmark==2:
			if tempcountmark==1:
				if tempdata[i]!='<'and tempdata[i]!='>' and tempdata[i]!='。'and tempdata[i]!='；':
					temp_entity+=tempdata[i]
					tempstr+=tempdata[i]
					tempcount+=1
		if tempdata[i]=='<' :
			if tempcountmark==1:
				end_place=tempcount
				begin_place=tempcount-len(temp_entity)
			elif tempdata[i+1]!='a' or tempdata[i+2]!='h' and tempdata[i+3]!='r':
				noway=1
			tempmark=1
			continue
		if tempdata[i]=='；'or tempdata[i]=='。'or tempdata[i]=='\n'or tempdata[i]==';':
			if tempdata[i]!='\n':
				tempstr+=tempdata[i]
				tempcount+=1
			if mark==1:
				if tempstr!=';\n':
					kb_with_link+=tempstr+tempmarkstr
					tempstr=''
					tempmarkstr=''
					mark=0
					tempcount=0
			if mark==0:
				if tempstr!=';\n':
					kb_without_link+=tempstr+'\n'
					tempstr=''
					mark=0
					tempcount=0
		else:
			if tempcountmark!=1:
				tempstr+=tempdata[i]
				tempcount+=1
kb_with.write(kb_with_link)
kb_without.write(kb_without_link)
kb_with.close()
kb_without.close()
kb_with=open('kb_with_link.txt','w',encoding='utf8')
kb_with_link=delblank('kb_with_link_temp.txt')
kb_without=open('kb_without_link.txt','w',encoding='utf8')
kb_without_link=delblank('kb_without_link_temp.txt')
kb_with.write(kb_with_link)
kb_without.write(kb_without_link)
kb_with.close()
kb_without.close()
			

