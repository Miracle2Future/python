# threading_Queue.py

import time
from queue import Queue
import threading

# 获取文章列表
def get_detail_url(queue):
	while True:
		print('get url start')
		time.sleep(2)
		for i in range(20):
			queue.put('http://projectsedu.com/{id}'.format(id=i))
		print('get url end')

# 获取所有详情页详情信息
def get_detail_html(queue):
	get_url = queue.get()
	while True:
		print('get html start')
		time.sleep(4)
		print('get html end')

if __name__ == '__main__':
	# 队列最大1000
	detail_url_queue = Queue(maxsize=1000)
	thread_get_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue))
	# thread_get_detail_url.start()
	for i in range(10):
		get_detail_html = threading.Thread(target=get_detail_html, args=(detail_url_queue))
		get_detail_html.start()

	## 结束线程阻塞
	# detail_url_queue.task_done()
	## 线程阻塞
	detail_url_queue.join()
