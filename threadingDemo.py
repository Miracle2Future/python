# threading.py

import threading
import time

# 模拟多线程爬取网站列表页与详情页

# 重写自己线程
class GetHtml(threading.Thread):

	def __init__(self, name):
		super().__init__(name=name)

	def run(self):
		print('get html start')
		time.sleep(2)
		print('get html end')

class GetUrl(threading.Thread):

	def __init__(self, name):
		super().__init__(name=name)

	def run(self):
		print('get url detail start')
		time.sleep(4)
		print('get url detail end')

if __name__ == '__main__':

	get_html = GetHtml('get_html')
	get_url = GetUrl('get_url')
	start = time.time()
	get_html.start()
	get_url.start()

	# 阻塞线程
	get_html.join()
	get_url.join()
	print('run time:{}'.format(time.itme()-start))
