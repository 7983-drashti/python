#exception handling.....
'''try:
	x=int(input('enter a no.'))
	y=int(input('enter a no.'))
	z=x/y
	print('Div is',z)
except Exception as e:
	print('tjere is any issue',e)


except Exception:
	print('Any issue')


except ZeroDivisionError:
	print('second no.is zero')
except ValueError:
	print('wrong value pass')
finally:
	print('the end')'''


#
'''try:
	n=input('enter file name')
	f=open(n,'r')
	s=f.read(500)
	print(s)
except:
	print('any issue')'''



try:
	x=int(input('enter a no.'))
	if x<10:
		raise Exception
	else:
		print('ok')
except:
	print('some issue')



