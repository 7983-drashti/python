#code 2
'''import pymysql
db=pymysql.connect('localhost','root','root','factory')
cur=db.cursor()
s="select * from employee"
try:
	cur.execute(s)
	res=cur.fetchall()
	for r in res:
		print('empno',r[0])
		print('name',r[1])
		print('city',r[2])
		print('salary',r[3])
except:
	print('any issue')
db.close()

#code 1
import pymysql
db=pymysql.connect('localhost','root','root','factory')
cur=db.cursor()
cur.execute('select version()')
data=cur.fetchone()
print('Database version is',data)
db.close()





#code 3 for insert data
import pymysql
db=pymysql.connect('localhost','root','root','factory')
cur=db.cursor()
s="insert into employee value(11,'shnaya','Sirsaganj',5000)"
try:
	cur.execute(s)
	db.commit()
	print('data saved')
except Exception as e:
	print('any issue',e)
	
db.close()'''


import pymysql
db=pymysql.connect('localhost','root','root','factory')
cur=db.cursor()
e=int(input('enter empno'))
n=input('enter name')
c=input('enter city')
sl=int(input('enter salary'))
s="insert into employee values(%d,'%s','%s',%d)"%(e,n,c,sl)
try:
	cur.execute(s)
	db.commit()
	print('record saved')
except:
	print('any issue')
db.close()
