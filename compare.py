import sys
import re
class A:
	def __init__(self):
		v1=sys.argv[1]
		v2=sys.argv[2]
		lis1=[]
		lis2=[]
		a1lis=[]
		b1lis=[]
		t=[]
		t1=[]
		dict_ok={'ok':[]}
		dict_fail={'FAIL':[]}
		dict3={'!okFAIL':[]}
		dict_ok1={'ok':[]}
		dict_fail1={'FAIL':[]}
		dict6={'!okFAIL':[]}
		count=0
		count1=0
		count2=0
		count3=0
		count4=0
		countl=0
		with open(v1,'r')as file1,open(v2,'r')as file2:
			f1=file1.readlines()
			for i in f1:
				a=re.match("tempest",i)
				if a:
					count=count+1
					lis1.append(i)
			print count	
			f2=file2.readlines()
			for j in f2:
				b=re.match("tempest",j)
				if b:
					count1=count1+1
					lis2.append(j)
				#print b
			print count1
			#for i in lis2:
			#	print i
		for i in lis1:
			a1=re.findall(r'\s(\w+)$',i)
			#print "+++",i,"+++"
			s1= ''.join(a1) 
			a1lis.append(s1)
			if s1=='ok':
				count2=count2+1
				t.append(i)
				dict_ok['ok'].append(i)
			elif s1=='FAIL':
				dict_fail['FAIL'].append(i)
				countl=countl+1
				#print s1
			else:
				dict3['!okFAIL'].append(i)
		
		dict_ok={'ok':t}
		for j in lis2:
		#	j = j.strip(" ")
		#	b1=re.findall(r'\s(\w+.*)\s*$',j)
		#	print "+++",j,"+++"
			s=j.split()
		#	print s[-1] 
			#b1lis.append(s[-1])
			#print s
			if s[-1]=='ok':
				#print s[-1]
				count3=count3+1
				dict_ok1['ok'].append(j)
				t1.append(j)
			elif s[-1]=='FAIL':
				count4=count4+1
				#print s[-1]
				dict_fail1['FAIL'].append(j)
			else:
				dict6['!okFAIL'].append(j)
		#for i in dict_ok1['ok']:
			#print i
		print count2
		#print count3
		print count4
		#print countl
		#k=0
		#print type(dict_ok['ok'])
		s=set(dict_ok['ok'])-set(dict_ok1['ok'])
		#print len(s)
		s1=set(dict_fail['FAIL'])-set(dict_fail1['FAIL'])
		#print len(s1)	
		s2=set(dict_ok['ok'])-set(dict_fail1['FAIL'])
		print len(s2)
		#print k
		
		
	
a=A()
