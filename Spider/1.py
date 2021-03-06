#CrawBaiduStocksA.py
import requests
from bs4 import BeautifulSoup
import traceback
import re
import bs4
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "cuowu"
 
def getStockList(lst, stockURL,fpath):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser') 
    a = soup.find_all('a')
    print('ha')
    for i in a:
        try:
            #print(i)
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue       
    '''with open(fpath,'a',encoding='utf-8') as f:
        f.write(str(lst))
        f.write('\n')'''
    
def getList(list):
    for i in list:
        print(i)                
 
def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html=="":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})
            if isinstance(stockInfo,bs4.element.Tag):   # 注意点2：增加一个if判断语句以及后续代码的缩进
                name = stockInfo('a','bets-name')[0]
                infoDict.update({'股票名称': name.text.split()[0]})
             
                keyList = stockInfo.find_all('dt')
                valueList = stockInfo.find_all('dd')
                for i in range(len(keyList)):
                    key = keyList[i].text
                    val = valueList[i].text
                    infoDict[key] = val
                with open(fpath, 'a', encoding='utf-8') as f:
                    f.write( str(infoDict) + '\n' )
                    count = count + 1
                    print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
        except:
            count = count + 1
            print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
            traceback.print_exc()
            continue
          
 
def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D://BaiduStockInfo.txt'
    slist=[]
    getStockList(slist, stock_list_url,output_file)
    getStockInfo(slist, stock_info_url, output_file)
    getList(slist)
 
main()