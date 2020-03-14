import pymysql
import matplotlib.pyplot as plt
import numpy as np
itemname=[]
qty=[]
db=pymysql.connect('localhost','root','root','factory')
cur=db.cursor()
s="select iname,purchasecity from item"
c=0
try:
	cur.execute(s)
	res=cur.fetchall()
	for r in res:
		itemname.append(r[0])
		qty.append(r[1])
		c=c+1
except Exception:
	print('any issue')
x=np.arange(c)
plt.bar(x,qty,tick_label=itemname,color=['blue','red'])
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()