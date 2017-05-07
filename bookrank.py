#!/User/Fancy/desktop/Python_practice python

#脚本通过单线程进行下载图书排名信息的调用
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen as uopen

REGEX = compile('#([\d,]+) in Books') # 匹配图书排名模式，正则表达
AMZN = 'http://amazon.com/dp/'

ISBNs = { #国标标准书号
	'0132269937': 'Core Python Programming',
	'0132356139': 'Python Web Development with Django',
	'0137143419': 'Python Fundamentals',
}

def getRanking(isbn):
	# page = uopen('%s%s' % (AMZN, isbn)) 
	# or str.format()
	page = uopen('{}{}'.format(AMZN, isbn))
	data = page.read()
	page.close()
	return REGEX.findall(data)[0]

def _showRanking(isbn):
	print('- %r ranked %s' % (ISBNs[isbn], getRanking(isbn)))

def _main():
	print('AT', ctime(), 'on Amazon...')
	for isbn in ISBNs:
		# _showRanking(isbn)
		Thread(target=_showRanking, args=(isbn,)).start() #_showRanking(isbn)

@register
def _atexit():
	print('all DONE at :', ctime())

if __name__ == '__main__':
	_main()