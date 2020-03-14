#Mailing using python....
'''import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('7983drashti@gmail.com','dr11as05ht19i99')
message="Hiii i am drashti...."
s.sendmail('7983drashti@gmail.com','drashti7983@gmail.com',message)
print('mail send')
s.quit()'''


'''import smtplib
t=input('enter email address')
m=input('enter message')
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('7983drashti@gmail.com','dr11as05ht19i99')
s.sendmail('7983drashti@gmail.com',t,m)
print('mail send')
s.quit()'''

'''import smtplib
t=input('enter email address')
f=open('file1.txt','r')
m=f.read(500)
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('7983drashti@gmail.com','dr11as05ht19i99')
s.sendmail('7983drashti@gmail.com',t,m)
print('mail send')
s.quit()'''

#sending mail to the multiple user....
'''import  smtplib
lt=['drashti7983@gmail.com','krtikarajput399@gmail.com']
for i in range(0,len(lt)):
	s=smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	s.login('7983drashti@gmail.com','dr11as05ht19i99')
	message='how are u?'
	s.sendmail('7983drashti@gmail.com',lt[i],message)
	s.quit()
print('mail send')'''


class fruit:
	name=''
	price=0
	color=''
a=fruit()
a.name='apple'
a.price=10
a.color='red'
b=fruit()
b.name='mango'
b.price=50
b.color='yellow'
print(a.name)
print(a.price)
print(a.color)
print(b.name)
print(b.price)
print(b.color)
