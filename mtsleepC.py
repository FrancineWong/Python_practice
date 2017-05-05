#!/User/Fancy/desktop/Python_practice python

'''join(), 主线程等待所有子线程完毕'''
import threading
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec):
	print('start loop', nloop, 'at:', ctime())
	sleep(nsec)
	print('loop', nloop, 'done at:', ctime())

def main():
	print('starting at:', ctime())
	threads = []
	nloops = range(len(loops))

	for i in nloops:
		t = threading.Thread(target=loop, args=(i, loops[i]))
		threads.append(t)

	for i in nloops: #start threads
		threads[i].start()

	for i in nloops: #wait for all threads to finish
		threads[i].join()

	print('all DONE at: ', ctime())

if __name__ == '__main__':
	main()