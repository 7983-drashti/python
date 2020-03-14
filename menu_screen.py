print("welcome to library management system")
print("press 1 for student")
print("press 2 for course")
print("press 3 for books")
print("press 4 for issue")
print("press 5 for return")
print("enter your choice!!!")
x=int(input())
if x==1:	
	print("press 1 for saving a new student")	
	print("press 2 for find a student according to rollno")	
	print("press 3 for delete a student")	
	print("press 4 for updating student details")
	y=int(input('enter your choice'))	
	if y==1:		
		import student_save
	elif y==1:		
		import student_find
	elif y==2:		
		import student_delete
elif x==2:
	print("press 1 for saving a new course")	
	print("press 2 for find a course")	
	print("press 3 for delete a course")	
	print("press 4 for updating course details")	
	y=int(input('enter your choice'))	
	if y==1:		
		import course_save	
	elif y==2:		
		import course_find		
	elif y==3:		
		import course_delete	
elif x==3:	
	print("press 1 for saving a new book")	
	print("press 2 for find a book according to bookid")	
	print("press 3 for delete a book")	
	print("press 4 for update an existing book")	
	y=int(input('enter your choice'))	
	if y==1:		
		import book_save
	elif y==2:		
		import book_find		
	elif y==3:		
		import book_delete
elif x==4:	
	print("press 1 for saving issue book data")	
	print("press 2 for find issue book data")	
	print("press 3 for delete issue book data")	
	print("press 4 for updating issue book data")	
	y=int(input('enter your choice'))	
	if y==1:		
		import issue_book_save
	elif y==2:		
		import issue_book_find		
	elif y==3:		
		import issue_book_delete
elif x==5:	
	print("press 1 for saving return book data")	
	print("press 2 for find return book data")	
	print("press 3 for delete return book data")	
	print("press 4 for updating return book data")	
	y=int(input('enter your choice'))	
	if y==1:		
		import return_book_save
	elif y==2:		
		import return_book_find		
	elif y==3:		
		import return_book_delete
else:
	print("out of library management")	