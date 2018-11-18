import requests
from bs4 import BeautifulSoup
import os
import bs4
import re
import time

headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36',
		'Referer': 'https://www.dmmsee.net/'}
def getHtml(url):
	try:
		r=requests.get(url,headers=headers,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return'爬取网页失败'	

def main():
	url='https://www.dmmsee.net/SABA-471'	
	html=getHtml(url)
	#print(html[0:500])
	soup=BeautifulSoup(html,'html.parser')
	title=soup.title.string
	actors=soup('div',attrs={'class':'star-name'})
	print('a')
	sli=[]
	if (len(actors)==0):
		print("空")
	for act in actors:
		sli.append(act.a.string)
	print(sli)
	dic={}
	dic['actors']=sli
	dic['ma']=title
	with open(root+'file.txt','a',encoding='utf-8') as f:
		f.write(str(dic)+'\n')


root='D://JavSpider//'
main()	