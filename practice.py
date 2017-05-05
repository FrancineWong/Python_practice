with Query('Bob') as q:
	q.query()

try:
	f = open('/path/to/file', 'r')
	f.read()
finally:
	if f:
		f.close()

with open('path/to/file', 'r') as f:
	f.read()

#实现上下文
@contextmanager
def tag(name):
	print("<%s>" %name)
	yield
	print("</%s>" %name)

with tag("h1"):
	print("hello")
	print("world")

class MyHTMLParser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		print('<%s>' % tag)

	def handle_endtag(self, tag):
		print('</%s>' % tag)

	def handle_startendtag(self, tag, attrs):
		print('<%s/>' % tag)

	def handle_data(self, data):
		print(data)

	def handle_comment(self, data):
		print('<!--', data, '-->')

	def handle_entityref(self, name):
		print('&%s;' %name)

	def handle_charref(self, name):
		print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html
	<head></head>
	<body>
	<!--test html parser -->
	<p>Some ''')


#urllib
from urllib import request

with request.urlopen('http://api.douban.com/v2/book/2129650') as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', data.decode('utf-8'))


#Get
from urllib import request
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
	print('Status:', f.status, f.reason)
	for k, vin f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', f.read().decode('utf-8'))





























