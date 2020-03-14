name=input('enter name')
city=input('anter city')
f=open('file1.txt','w')
f.write(name)
f.write(city)
print('file saved')
f.close()"""

"""n=input('filename.txt')
f=open(n,'w')
for i in range(1,6):
	name=input('enter name')
	city=input('enter city')
	f.write(name)
	f.write('\n')
	f.write(city)
	f.write('\n')
print('file saved')
f.close()"""



# reading the file...
"""f=open('file1.txt','r')
st=f.read(500)
print(st)
f.close()"""


#read from one file and write in another file...
"""f=open('abcdef.txt','r')
f1=open('python5.txt','w')
s=f.read(500)
f1.write(s)
f.close()"""


#it will show how many letters and words in file.
n=input('enter file name')
f=open(n,'r')
s=f.read(500)
c=0
l=len(s)
print('letter','l')
for i in range(0,l):
	if s[i]=='':
		c=c+1
print('words',c+1)



