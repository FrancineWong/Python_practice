#!/User/Fancy/desktop/Python_practice python

#为子类更加通用，将子类一道专门模块中，添加可滴啊用getresult()获得返回值

import threading
from time import sleep, ctime

class MyThread(threading.Thread):
	"""docstring for MyThread"""
	def __init__(self, func, args, name=''):
		threading.Thread.__init__(self)
		self.name = name
		self.func = func
		self.args = args

	def getResult(self):
		return self.res

	def run(self):
		print('starting', self.name, 'at:', ctime())
		self.res = self.func(*self.args)
		print(self.name, 'finished at:', ctime())
