import requests
import re

def getHtml(url):
	try:
		r=requests.get(url)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return'爬取网页失败'	

def getPic(html):
	try:
		pic_url=re.findall(r'http://fm.shiyunjj.com/small/\d{4}/\d{0,5}.jpg',html)
		for pic in pic_url:
			fpath=root+'/'+pic.split('/')[-1]
			r=requests.get(pic,headers=header)
			with open(fpath,'wb') as f:
				f.write(r.content)
				f.close()
	except:
		pass	



def main():
	depth=9
	slist=[]
	for i in range(1,depth):
		url=start_url+'/'+str(i)
		html=getHtml(url)
		getPic(html)
		print(str(i)+'页爬取成功')


header = {
    'Referer':'http://www.mmjpg.com'}
start_url='http://www.mmjpg.com/tag/ugirls'		
root='D://pic'

main()