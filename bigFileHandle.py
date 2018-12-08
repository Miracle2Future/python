# -*-coding:utf-8 -*-

# 生成器大文件分割处理(500G文件)
import random
def myfilefunc(f, newline):
	'''
		para:
				f: 文件句柄
				newline: 分割符号
	'''
	buf = ''
	while True:
		while newline in buf:
			pos = buf.index(newline)
			yield buf[:pos]
			buf = buf[pos + len(newline):]
		# 读取 4096 * 10 文件	
		chunk = f.read(4096*10)
		if not chunk:
			# 说明已经读到了文件结尾
			yield buf
			break
		buf += chunk

if __name__ == '__main__':
	# 生成一个测试文件
	with open('test.txt', 'w') as f:
		tag = '{|}'
		d = ','		
		for i in range(1000000):
			msg = 'this is a test file'
			msg += random.choice((msg,tag,d))
			f.write(msg)

	# 读取文件
	with open('test.txt', 'r') as f:
		for chunk in myfilefunc(f, '{|}'):
			print(chunk)
