import threading
import time
def Hello():
	print('wait for 5 sec')
	time.sleep(5)
	print('welcome to Hello')
t=threading.Thread(target=Hello)
t.start()