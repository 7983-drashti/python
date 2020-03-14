#record delete  in sql table...
import pymysql
db=pymysql.connect('localhost','root','root','factory')
cur=db.cursor()
e=int(input('enter empno'))
s="delete from employee where empno=%d"%(e)
try:
	cur.execute(s)
	db.commit()
	print('record deleted')
except Exception as ex:
	print('any issue')
db.close()

#for update record in sql

import pymysql
db=pymysql.connect('localhost','root','root','factory')
cur=db.cursor()
e=int(input('enter empno'))
n=input('enter new name')
c=input('enter new city')
sl=int(input('enter new salary'))
s="update employee set name='%s',city='%s',salary=%d where empno=%d"%(n,c,sl,e)
try:
	cur.execute(s)
	db.commit()
	print('record changed')
except Exception as es:
	print('any issue')
db.close()

#for select data 
import pymysql
db=pymysql.connect('localhost','root','root','factory')
cur=db.cursor()
e=int(input('enter empno'))
s="select * from  employee where empno=%d"%(e)
try:
	cur.execute(s)
	res=cur.fetchall()
	for r in res:
		print('empno',r[0])
		print('name',r[1])
		print('city',r[2])
		print('salary',r[3])

except Exception as ex:
	print('any issue')
db.close()'''