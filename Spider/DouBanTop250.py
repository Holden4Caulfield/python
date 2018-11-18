import requests
from bs4 import BeautifulSoup
import bs4

def getHtml(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return'获取网页失败'	

def getList(html):
#获取界面的内容，保存入文件
	soup=BeautifulSoup(html,'html.parser')
	items=soup('div',attrs={'class':'item'})
	try:
		for item in items:
			dic={}
			name=item.find('span',attrs={'class':'title'}).string
			rank=item.find('em').string
			num=item.find('div',attrs={'class':'star'})('span')[3].string
			#print(rank)
			score=item.find('span',attrs={'class':'rating_num'}).string
			dic['rank']=rank
			list.append(dic)
			'''with open(path,'a',encoding='utf-8') as f:
				f.write(mod.format(name,rank,score,num)+'\n')'''
	except:
		pass		


def main():
	depth=10
	infoDict={}
	start_url='https://movie.douban.com/top250?start='
	for i in range(depth):
		url=start_url+str(i*25)+'&filter='
		#print(url)
		html=getHtml(url)
		getList(html)
	print(list)	

#https://movie.douban.com/top250?start=175&filter=

#https://movie.douban.com/top250?start=25&filter=
path='D://DouBanTop.txt'
mod='名称：{0:^6}\t 排名{1:^10}\t 评分{2:^2} 评价人数{3}".'
list=[]
main()		