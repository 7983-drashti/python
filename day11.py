#distructor..
'''class my:
	x=0
	y=0
	def __init__(self,a,b):
		self.x=a
		self.y=b
		print('cons callled ')
	def show(self):
		print('x is ',self.x)
		print('y is',self.y)
m=my(20,5)
m.show()
p=my(25,10)
p.show()


#distructor..
class my:
	x=0
	y=0
	def __init__(self,a,b):
		self.x=a
		self.y=b
		print('cons callled ')
	def show(self):
		print('x is ',self.x)
		print('y is',self.y)
	def __del__(self):
		print('object')
m=my(20,5)
m.show()
p=my(25,10)
p.show()'''

#parent child enheritance...

class Asup:
	x=0
	y=0
	def read(self,a,b):
		self.x=a
		self.y=b
	def sum(self):
		print('sum',self.x,self.y)
class Asub(Asup):
	def get(self,p,r):
		self.m=p
		self.n=r
	def calc(self):
		print('sub',self.m,self.n)
p=Asub()
p.get(10,5)
p.calc()
p.read(20,5)
p.sum()
'''


class Asup:
	x=0
	y=0
	def read(self,a,b):
		self.x=a
		self.y=b
	def sum(self):
		print('sum',self.x,self.y)
class Asub(Asup):
	def get(self,p,r):
		self.m=p
		self.n=r
	def calc(self):
		print('sub',self.m,self.n)


class Bsub(Asub):
	def mul(self,a,b):
		print('multiply',(a*b))
p=Bsub()
p.get(10,5)
p.calc()
p.read(10,5)
p.sum()
p.mul(2,3)


#string representation for the object
class abc:
	def __str__(self):
		return'hello python class'
obj=abc()
print(str(obj))


# making 

class abc:
	def __hi(self):#private function
		print('hi')
obj=abc()
obj.hi()


class calculator:
	a=0
	b=0
	def get(self,x,y):
		self.a=x
		self.b=y
	def ans(self,op):
		if op=='+':
			print('sum is',self.x,self.y)'''
			






