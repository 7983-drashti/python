import pymysql
db=pymysql.connect('localhost','root','root','factory')
cur=db.cursor()
e=int(input('enter itemno'))
s="select iname,qty from item where itemno=%d"%(e)
lt=[]
try:
	cur.execute(s)
	res=cur.fetchall()
	for r in res:
		print('iname',r[0])
		print('qty',r[1])
except Exception as ex:
	print('any issue')
db.close()