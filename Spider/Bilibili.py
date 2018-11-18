from bs4 import BeautifulSoup
import requests
import bs4
def getHtml(url):
	try:
		r = requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		print(r.encoding)
		return r.text
	except:
		return'11'

def getRank(html):
	soup=BeautifulSoup(html,'html.parser')
	tbody=soup.ol
	for li in tbody.children:
		if isinstance(li,bs4.element.Tag):
			divs=li.div('div')
			print('排名{0:^2}{1:{2}^10}'.format(divs[0].em.string
				,divs[2].span.string,chr(12288)))
			print(divs[4]('span')[3].text)


def main():
	url='https://movie.douban.com/top250'
	html=getHtml(url)
	getRank(html)
	soup=BeautifulSoup(html,'html.parser')
	tbody=soup.ol.li
	#print(tbody('span','inq')[0].string)
	print(len(soup.ol.contents))

	
	
main()
