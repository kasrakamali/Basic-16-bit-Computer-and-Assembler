print("Please enter the name of your source file:")
inp=input()
f=open(inp,"r")
a=f.readlines()
f.close()
for i in range(0,len(a)):
	if a[i].find("/")!=-1:
		a[i]=a[i][:a[i].find("/")]
	a[i]=a[i].strip()
	
#1st pass

LC=0
location=list()
label=list()
address=list()
for i in range(0,len(a)):
	if a[i][0:3] == "ORG" :
		LC=int(a[i][4:],16)
		continue
	else:
		if a[i].find(",",1,4)!=-1 :
			label.append(a[i][0:(a[i].find(","))])
			address.append(LC)
	location.append(LC)
	LC+=1
print("\n>> 1st pass :\n")
print("Address symbol\tHexadecimal address\n")
for i in range(len(label)):
	print("     %s  \t\t%03x"%(label[i], address[i]))
print("\n***********************************\n")

#2nd pass

MRI={
"AND":0x0,
"ADD":0x1,
"LDA":0x2,
"STA":0x3,
"BUN":0x4,
"BSA":0x5,
"ISZ":0x6
}
nonMRI={
"CLA":0x7800,
"CLE":0x7400,
"CMA":0x7200,
"CME":0x7100,
"CIR":0x7080,
"CIL":0x7040,
"INC":0x7020,
"SPA":0x7010,
"SNA":0x7008,
"SZA":0x7004,
"SZE":0x7002,
"HLT":0x7001,
"INP":0xF800,
"OUT":0xF400,
"SKI":0xF200,
"SKO":0xF100,
"ION":0xF080,
"IOF":0xF040
}
PI=[
"ORG",
"END",
"DEC",
"HEX"
]

code=list()
for i in range(0,len(a)):
	I=0
	c=-1
	for j in MRI :
		if a[i].find(j,a[i].find(",")+1) != -1:
			c=MRI[j]
			if a[i][len(a[i])-2:] ==" I":
				I=1
				c+=8
			s=a[i].split()
			if I :
				s=s[len(s)-2]
			else:
				s=s[len(s)-1]
			if s.isnumeric():
				c=0x1000*c+int(s,16)
			else:
				for k in range(0,len(label)) :
					if s == label[k]:
						c=0x1000*c+address[k]
						break
			code.append(c)
			break
	if c != -1:
		continue
	for j in nonMRI :
		if a[i].find(j,a[i].find(",")+1) != -1:
			c=nonMRI[j]
			code.append(c)
			break
	if c !=-1:
		continue
	for j in PI:
		if a[i].find(j,a[i].find(",")+1) != -1:
			if j=="DEC":
				s=a[i].split()
				s=s[len(s)-1]
				c=int(s)
				code.append(c)
			elif j=="HEX":
				s=a[i].split()
				s=s[len(s)-1]
				c=int(s,16)
				code.append(c)
			else:
				break
				
for i in range(len(code)):
	if code[i]<0:
		code[i]=0xffff+code[i]+1
print(">> 2nd pass :\n")
print("Location\tContent\n")
for i in range(len(code)):
	print("  %03x\t\t  %04x" %(location[i], code[i]))
print("\nDo you want to save the results?")
print("1.Yes\n2.No")
inp=input()
if inp =="1" :
	print("Please enter a name for the output file:")
	inp=input()
	f=open(inp,"w")
	f.write(">> 1st pass :\n\n")
	f.write("Address symbol\tHexadecimal address\n\n")
	for i in range(len(label)):
		f.write("     %s  \t\t%03x\n"%(label[i], address[i]))
	f.write("\n***********************************\n\n")
	f.write(">> 2nd pass :\n\n")
	f.write("Location\tContent\n\n")
	for i in range(len(code)):
		f.write("  %03x\t\t  %04x\n" %(location[i], code[i]))
	f.close()