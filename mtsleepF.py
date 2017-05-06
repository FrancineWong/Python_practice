#!/User/Fancy/desktop/Python_practice python3
#utilize with to simplify the acquire and release of lock
from atexit import register
from random import randrange
from threading import Thread, Lock, currentThread
from time import sleep, ctime
# from __future__ import with_statement #2.5 only

class CleanOutputSet(set):
	"""docstring for CleanOutputSet"""
	def __str__(self):
		return (', '.join(x for x in self))

lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()

def loop(nsec):
	myname = currentThread().name
	# lock.acquire()
	# remaining.add(myname)
	# print('[%s] Started %s' % (ctime(), myname))
	# lock.release()
	# sleep(nsec)
	# lock.acquire()
	# remaining.remove(myname)
	# print('[%s] Completed %s (%d secs)' % (ctime(), myname, nsec))
	# print(' (remaining: %s)' % (remaining or 'NONE'))
	# lock.release()
	with lock:
		remaining.add(myname)
		print('[%s] Started %s' % (ctime(), myname))
	sleep(nsec)
	with lock:
		remaining.remove(myname)
		print('[%s] Completed %s (%d secs)' % (ctime(), myname, nsec))
		print(' (remaining: %s)' % (remaining or 'NONE'))

def _main():
	for pause in loops:
		Thread(target=loop, args=(pause, )).start()

@register
def _atexit():
	print('all DONE at: ', ctime())

if __name__ == '__main__':
	_main()

