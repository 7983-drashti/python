#calender..
import calendar 
for i in range(1,13):
	m=calendar.month(2020,i)
	print(m)



#write a program to input month and year of your date of birth print calender
import time
m=calendar.month(2020,5)
print(m)


#how to import time.......
import time 
t=time.time()
print (t)
tc=time.localtime(t)
print(tc)
ac=time.asctime(tc)
print(ac)
h=int(ac[11:13])
m=int(ac[14:16])
if h==17 and m>47:
	print('log out')
else :
	print('not')




#import method no 4........... 
from example import *
division(10,5)
mult(10,5)
sum(10,5)

#import method no 3.......
import example as tp
tp.division(10,5)
tp.sum(10,5)
tp.mult(10,5)'''

a='this is python'
b=a.capitalize()
print(b)