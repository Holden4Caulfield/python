import requests
try:
	r=requests.get('https://blog.csdn.net/qq_38329811/article/details/76735872')
	r.raise_for_status()
	print(r.title)
	r.encoding=r.apparent_encoding
	print((r.text[:1000]))
except:
	print('11')