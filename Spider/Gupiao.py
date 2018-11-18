import requests
import re
from bs4 import BeautifulSoup
import traceback

def getHtml(url):
	try:
		r=requests.get(url)
		r.raise_for_status()
		r.encoding=r.apparent.encoding
		return r.text
	except:
		return""

def getStockList(lst,stockUrl):
	html=getHtml(stockUrl)
	soup=BeautifulSoup(html,'html.parser')
	a=soup('a')
	for i in a:
		try:
			href=i.attrs['href']
			lst.append(re.findall(r'[s][hz]\d{6}',href)[0])
		except:
			continue

def getStockInfo(lst,stockUrl,fpath):
	for stock in lst:
		url=stock_info_url+stock+'.html'
		html=BeautifulSoup(html,'html.parser')
		try:
			if html=="":
				continue
			infoDict={}
			stockInfo=soup.find('div',attrs={'class':'stock-bets'})

			name=stockInfo.find_all(attrs={'class':'bets_name'})[0]	
			infoDict.update({'股票名称':name.string.split()[0]})

			keyList=stockInfo('dt')
			valueList=stockInfo('dd')
			for i in range(len(keyList)):
				key=keyList[i].string
				value=valueList[i].string
				infoDict[key]=value
			with open(fpath,'a',encoding='utf-8') as f:
				f.write(str(infoDict)+'\n')	
		except:
			traceback.print_exc()
			continue		
def main():
	stock_list_url='http://quote.eastmoney.com/stocklist.html'
	stock_info_url='https://gupiao.baidu.com/stock/'
	path='D:/BaiduStockInfo.txt'
	slist=[]
	getStockList(slist,stock_list_url)
	getStockInfo(slist,stock_info_url,path)

main()	

					