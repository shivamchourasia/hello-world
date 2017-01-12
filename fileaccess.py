import re
with open("diag.out","r")as input:
	list=[]
	for line in input:
		matchObj=re.match("----- APmgr info: apmgrinfo -a",line,re.M|re.I)
		if matchObj:
			for line in input:
				list.append(line)
				matchObj2=re.match("----- Disconnected APs: wlaninfo --all-disc-ap -l 3",line,re.M|re.I)
				if matchObj2:
  					break
for lin in list:

	match=re.findall(r'(?:[\d][1-9]{2,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',lin)
#	if match:
	#	print match
	mac=re.findall(r'[0-9a-f][0-9a-f][:-][0-9a-f][0-9a-f][:-][0-9a-f][0-9a-f][:-][0-9a-f][0+-9a-f][:-][0-9a-f][0-9a-f][:-][0-9a-f][0-9a-f]',lin)
#	if mac:
#		print mac
	psk=re.findall(r'\s*PSK\s*:\s*(.*)',lin)
#	if psk:
#		print psk
	name=re.findall(r'\s*Name\s*:\s*(.*)',lin)
#	if name:
#		print name
	state=re.findall(r'\s*State\s*:\s*(.*)',lin)
#	if state:
#		print state
	mesh_role=re.findall(r'\s*Mesh Role\s*:\s*(.*)',lin)
#	if mesh_role:
#		print mesh_role
	timer=re.findall(r'\s*Timer\s*:\s*(.*)',lin)
#	if timer:
#		print timer
	tunnel=re.findall(r'\s*Tunnel/Sec Mode\s*:\s*(.*)/',lin)
#	if tunnel:
#		print tunnel
	l=re.match(r'\s*Tunnel/Sec Mode\s*:(\s*(.*))',lin)
#	print "j"
	if l:
		sec_mode=l.group(2)
		sec_mode=sec_mode.split("/")
#		print l[1]
	hw=re.findall(r'\s*HW/SW Version\s*:\s*(.*)/',lin)
#	if hw:
#		print hw	
	l1=re.match(r'\s*HW/SW Version\s*:(\s*(.*))',lin)
	if l1:
		sw=l1.group(2)
		sw=sw.split("/")
		print sw[1]
	model=re.findall(r'\s*Model/Serial Num\s*:\s*(.*)/',lin)
#	if model:
#		print model
	l2=re.match(r'\s*Model/Serial Num\s*:(\s*(.*))',lin)
	if l2:
		serial_num=l2.group(2)
		serial_num=serial_num.split("/")
#		print l2[1]
#	n=re.findall(r'([A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}',lin)
#	if n:
#		print 'l3'
#		ipv6=l3.group(2)
#		ipv6=ipv6.split("/")
#		print ipv6[2]
