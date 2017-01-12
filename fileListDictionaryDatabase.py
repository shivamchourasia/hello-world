import re
import MySQLdb
dict1={}
mac1=[];ipv4_1=[];ipv6_1=[];psk1=[];name1=[];state1=[];mesh_role1=[];timer1=[];tunnel1=[];
sec_mode1=[];sw1=[];hw1=[];model1=[];serial_num1=[]
with open("diag.out","r")as inpu:
	list1=[]
	for line in inpu:
		matchObj=re.match("----- APmgr info: apmgrinfo -a",line,re.M|re.I)
		if matchObj:
			for line in inpu:
				list1.append(line)
				matchObj2=re.match("----- Disconnected APs: wlaninfo --all-disc-ap -l 3",line,re.M|re.I)
				if matchObj2:
					break
for lin in list1:
	ipv4=re.findall(r'(?:[\d][1-9]{2,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',lin)
	if ipv4:
		i1=ipv4
		ipv4_1.append(ipv4)
	mac=re.findall(r'[0-9a-f][0-9a-f][:-][0-9a-f][0-9a-f][:-][0-9a-f][0-9a-f][:-][0-9a-f][0+-9a-f][:-][0-9a-f][0-9a-f][:-][0-9a-f][0-9a-f]',lin)
	if mac:
		m1=mac
		mac1.append(mac)
#		print mac1
	psk=re.findall(r'\s*PSK\s*:\s*(.*)',lin)
	if psk:
		p=psk
		psk1.append(psk)
	name=re.findall(r'\s*Name\s*:\s*(.*)',lin)
	if name:
		n=name
		name1.append(name)
	state=re.findall(r'\s*State\s*:\s*(.*)',lin)
	if state:
		st=state
		state1.append(state)
	mesh_role=re.findall(r'\s*Mesh Role\s*:\s*(.*)',lin)
	if mesh_role:
		me=mesh_role
		mesh_role1.append(mesh_role)
	timer=re.findall(r'\s*Timer\s*:\s*(.*)',lin)
	if timer:
		ti=timer
		timer1.append(timer)
	tunnel=re.findall(r'\s*Tunnel/Sec Mode\s*:\s*(.*)/',lin)
	if tunnel:
		tu=tunnel
		tunnel1.append(tunnel)
	l=re.match(r'\s*Tunnel/Sec Mode\s*:(\s*(.*))',lin)
#	print "j"
	if l:
		sec_mode=l.group(2)
		sec_mode=sec_mode.split("/")
		sec_mode1.append(sec_mode)
		se=sec_mode[1]
	hw=re.findall(r'\s*HW/SW Version\s*:\s*(.*)/',lin)
	if hw:
		h=hw
		hw1.append(hw)	
	l1=re.match(r'\s*HW/SW Version\s*:(\s*(.*))',lin)
	if l1:
		sw=l1.group(2)
		sw=sw.split("/")
		sw1.append(sw)
		s=sw[1]
	model=re.findall(r'\s*Model/Serial Num\s*:\s*(.*)/',lin)
	if model:
		mo=model
		model1.append(model)
	l2=re.match(r'\s*Model/Serial Num\s*:(\s*(.*))',lin)
	if l2:
		serial_num=l2.group(2)
		serial_num=serial_num.split("/")
		ser=serial_num[1]
		serial_num1.append(serial_num)
#		print ser
#		print 'kkkkkk'
#		print serial_num[1]
#		print name1[-1]
#		print 'llll'
#	n=re.findall(r'([A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}',lin)
#	if n:
#		print 'l3'
#		ipv6=l3.group(2)
#		ipv6=ipv6.split("/")
#		print i1,'ipv6',m1,p,n,s,m,t,tu,se,h,s,mo,ser
#		i=0
		
		# dict1={m1[0]:[i1[0],'ipv6',m1[0],p[0],n[0],s[0],m[0],t[0],tu[0],se[0],h[0],s[0],mo[0],ser[0]]}#assigning value for the same key,it will copy and we will get the last assigned value
		dict1[m1[0]]= [i1[0],'ipv6',m1[0],p[0],n[0],st[0],me[0],ti[0],tu[0],se[0],h[0],s[0],mo[0],ser[0]]#assigning value for each key

db=MySQLdb.connect('localhost','root','asm123','dialog')
cur=db.cursor()
#cur.execute("create table Description(MACAddress varchar(50),IPv4Address varchar(50),IPv6Address varchar(50),Name varchar(50),State varchar(50),Tunnel varchar(50),Sec_Mode varchar(50),Mesh_Role varchar(50),PSK varchar(50),Timer varchar(50),HW_Version varchar(50),SW_Version varchar(50),Model varchar(50),Serial_Number varchar(50))")
for i in mac1:
	e=i[0]
	if e in dict1:
		l=dict1[e]
		cur.execute("""insert into Description values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13]))
db.commit()
cur.execute("select * from Description")
rows=cur.fetchall()
for row in rows:
	print row
