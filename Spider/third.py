import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return '11'	
	
def fillUnivList(ulist,html):
	soup =BeautifulSoup(html,'html.parser')
	for tr in soup.find('tbody').children:
		if isinstance(tr,bs4.element.Tag):
			tds=tr('td')
			ulist.append([tds[0].string,tds[1].string,tds[2].string])
def printList(ulist,num):
	print("{0:^6}\t{1:{3}^10}\t{2:^6}".format('排名','学校','省份',chr(12288)))
	for i in range(num):
		print("{0:^6}\t{1:{3}^10}\t{2:^6}".format(ulist[i][0],ulist[i][1],ulist[i][2],
			chr(12288)))

def ppp(html):
	soup =BeautifulSoup(html,'html.parser')
	a=soup.tbody.contents[1]
	print(a)
	print(len(a('td')))

def main():
	uinfo=[]		
	url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
	html=getHTMLText(url)
	#print(html[:10000])
	fillUnivList(uinfo,html)
	printList(uinfo,20)
	ppp(html)
main()