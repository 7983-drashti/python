#reverse letters of file from one file to another file..
"""f=open('file1.txt','r')
ff=open('file2.txt','w')
s=f.read(500)
l=len(s)
for i in range(l-1,-1,-1):
	ff.write(s[i])
print('file saved')"""

#reverse string..
"""f=open('file1.txt','r')
ff=open('file2.txt','w')
s=f.read(500)
t=s[::-1]
ff.write(t)
print('file saved')"""


#count no. of digits in a file...
"""f=open('file1.txt','r')
s=f.read(500)
c=0
for x in s:
	if x.isdigit():
		c=c+1
print('digit are',c)"""

#count no. of small letters...
"""f=open('file1.txt','r')
s=f.read(500)
c=0
for x in s:
	if x.islower():
		c=c+1
print('small latters are',c)"""

#saperate numbers or letters ...
'''f=open('python5.txt','r')
a=open('file3.txt','w')
b=open('file4.txt','w')
s=f.read(500)
for x in s:
	if x.isdigit():
		a.write(x)
	else:
		b.write(x)
print('file saved')
f.close()
a.close()
b.close()'''



#rename file...
"""import os
f=input('enter file name')
q=input('enter new file name')
os.rename(f,q)

print('name changed')"""

#delete file ..
"""import os
f=input('enter file name')
os.remove(f)

print('file removed')"""

#create folder...
"""import os
f=input('enter folder name')
os.mkdir(f)
print('folder created')"""


#delete folder...
"""import os
f=input('enter folder name')
os.rmdir(f)
print('folder removed')"""

#find current folder...

'''import os
print(os.getcwd())'''





