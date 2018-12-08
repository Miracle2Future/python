# threding_condition.py

import threading
# from threading import condition

# 通过condition完成协同读诗

class TianMao(threading.Thread):



	def __init__(self, cond):
		super().__init__(name='天猫精灵')
		self.cond = cond

	def run(self):
		TM = (
			'小爱同学', 
			'我们来对古诗吧', 
			'我住长江头', 
			'日日思君不见君', 
			'此水几时休', 
			'只愿君心似我心')
		with self.cond:
			for i in range(len(TM)):
				print('{}:{}'.format(self.name, TM[i]))
				self.cond.notify()
				self.cond.wait()

class XiaoAi(threading.Thread):

	

	def __init__(self, cond):
		super().__init__(name='小爱同学')
		self.cond = cond

	def run(self):
		XA = (
			'在', 
			'好啊', 
			'君住长江尾',
			'共饮长江水',
			'此恨何时已',
			'定不负相思意')
		with self.cond:
			for i in range(len(XA)):
				self.cond.wait()
				print('{}:{}'.format(self.name, XA[i]))
				self.cond.notify()
				
if __name__ == '__main__':
	cond = threading.Condition()
	tm = TianMao(cond)
	xa = XiaoAi(cond)
	
	# 启动顺序很重要
	# 在调用with cond之后 才能调用wait或者 notify方法
	# condition 有两层锁 一把底层锁会在线程调用wait方法的时候释放
	#   上面的锁会在每次调用wait的时候分配一把并放入到cond的等待队列中，等待notify方法唤醒


	# 必须小爱先start
	xa.start()
	tm.start()


	
