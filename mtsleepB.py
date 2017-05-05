#!/Users/Fancy/desktop/Python_practice python
import _thread
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec, lock):
	print('start loop', nloop, 'at:', ctime())
	sleep(nsec)
	print('loop', nloop, 'done at:', ctime())
	lock.release()

def main():
	print('starting at:', ctime())
	locks = []
	nloops = range(len(loops))

	#创建锁的列表，通过acquire获取，一旦上锁，添加到lock中
	for i in nloops:
		lock = _thread.allocate_lock()
		lock.acquire()
		locks.append(lock)
	#派生线程
	for i in nloops:
		_thread.start_new_thread(loop, (i, loops[i], locks[i]))
	#等待，暂停主线程，直到所有锁被释放
	for i in nloops:
		while locks[i].locked():pass

	print('all DONE at: ', ctime())

if __name__ == '__main__':
	main()