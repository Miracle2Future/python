# threading_Semaphore.py

import threading
import time

class SpiderHtml(threading.Thread):

	def __init__(self, url, sem):
		super().__init__()
		self.url = url
		self.sem = sem

	def run(self):
		time.sleep(2)
		print('spider html start')
		print('spider html end')
		self.sem.release()

class GetUrl(threading.Thread):

	def __init__(self, sem):
		super().__init__()
		self.sem = sem

	def run(self):
		for i in range(20):
			self.sem.acquire() # 控制线程并发执行数量为3
			spider = SpiderHtml('https://www.baidu.com/{}'.format(i), self.sem)
			spider.start()

if __name__ == '__main__':
	sem = threading.Semaphore(3)  # 控制线程并发执行数量为3
	get_url = GetUrl(sem)
	get_url.start()
