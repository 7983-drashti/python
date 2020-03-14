
#create class and objects

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

'''class fruit:
	name=''
	price=0
	color=''
	def read(self):  #self keyword must be use here..self will not change..
		self.name='apple'
		self.price=20
		self.color='red'
	def show(self):
		print(self.name)
		print(self.price)
		print(self.color)
f=fruit()
f.read()
f.show()

class fruit:
	name=''
	price=0
	color=''
	def read(self,n,p,c):  #self keyword must be use here..self will not change..
		self.name=n
		self.price=p
		self.color=c	
	def show(self):
		print(self.name)
		print(self.price)
		print(self.color)
f=fruit()
f.read('apple',40,'red')
f.show()
g=fruit()
g.read('mango',50,'yellow')
g.show()



class employee:
	empno=0
	ename=''
	salary=0
	grade=''
	def read(self,a,b,c):
		self.empno=a
		self.ename=b
		self.salary=c
	def cgrade(self):
		if self.salary>=3000:
			self.grade='A'
		else:
			self.grade='B'
	def show(self):
		self.cgrade()
		print(self.ename)
		print(self.grade)
e=employee()
e.read(111,'Pooja',4000)
e.show()

#constructor...
class clt:
	def __init__(self):
		print('hello world')
c=clt()
d=clt()'''







