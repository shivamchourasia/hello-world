import sys
def filehandle(var):
	var3=" "
	while var3!="quit":
		f=open("testing.txt","r")
		lines=f.read()
		lines=lines.split("\n")
		dict={}
#	var=raw_input("enter a word ")
		print "input is "+var
		for line in lines:
			word=line.split(" ")
			dict[word[0]]=word[1:]
	
		if var in dict:
			print(dict[var])
		else:
			var1=raw_input("please enter the synonyms")
			dict[var]=var1
#	v1=dict[var]
			f=open("testing.txt","a")
			f.write("\n"+var+" "+":")
			f.write(str(dict[var]))
			print(var,":",dict[var])
			f.close
		var3=raw_input("enter 'quit' to exit")
	else:
		sys.exit("u typed quit")
var=raw_input("enter a word")
filehandle(var)
