# threading_sync.py

import threading

from threading import Lock, RLock
total = 0
# 锁 同步 耗费时间
# 情景： 多线程访问同一个商品的库存
# lock = Lock()
# 在同一个线程里，可以连续多次调用acquire
lock = RLock() # 可重入的锁
def add():
	global total
	global lock
	for i in range(100000):
		lock.acquire()
		dos(lock)
		total += 1
		lock.release()

def desc():
	global total
	global lock
	for i in range(100000):
		lock.acquire()
		total -= 1
		lock.release()

def dos(lock):
	lock.acquire()
	# do
	lock.release()

if __name__ == '__main__':
	
	thread1 = threading.Thread(target=add)
	thread2 = threading.Thread(target=desc)
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()

	print(total)
