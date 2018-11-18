import requests
import re
from bs4 import BeautifulSoup
import bs4

def getHtmlText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		print(r.text[:5000])
		return r.text
	except:
		return"获取网页失败"


def parsePage(ilt,html):
	try:
		plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
		for i in range(len(plt)):
			price=eval(plt[i].split(':')[1])
			title=eval(tlt[i].split(':')[1])
			ilt.append([price,title])
	except:
		print("")	

def printGoodsList(ilt):
	tplt="{:4}\t{:8}\t{:16}"
	print(tplt.format("序号","价格","名称"))
	count=0;
	for i in ilt:
		count=count+1
		print(tplt.format(count,i[0],i[1]))

def main():
	goods="书包"
	deepth=2
	start_url="https://s.taobao.com/search?q="+goods
	infoList=[]
	print("11")
	for i in range(deepth):
		try:
			url=start_url+"&s="+str(44*i)
			print("11")
			html=getHtmlText(url)
			parsePage(infoList,html)
		except:
			continue;
		printGoodsList(infoList)
		
main()					