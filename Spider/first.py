import requests
url1='https://www.baidu.com/s?wd=%E5%AD%99%E7%AC%91%E5%B7%9D'
try:
	r=requests.get(url1)
	r.raise_for_status()
	r.encoding=r.apparent_encoding
	print(len(r.text))
except:
	print("异常")
url2='http://www.baidu.com/s'
kv={'wd':'孙笑川'}
try:
	b=requests.get(url2,params=kv)
	print(b.request.url)
	b.raise_for_status()
	b.encoding=b.apparent_encoding
	print(len(b.text))
	print(r.request.headers)
except:
	print("异常2")
url3='http://www.baidu.com/s'
kv={'wd':'孙笑川'}
try:
	b=requests.get(url3,params=kv)
	print(b.request.url)
	b.raise_for_status()
	b.encoding=b.apparent_encoding
	print(len(b.text))
except:
	print("异常3")					

			