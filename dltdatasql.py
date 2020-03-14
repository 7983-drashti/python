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
