import requests
from bs4 import BeautifulSoup
import os
import bs4
import re
import time

def getHtml(url):
	try:
		r=requests.get(url,headers=headers,timeout=30)
		r.raise_for_status()
		r.encoding='utf-8'
		return r.text
	except:
		return'爬取网页失败'	


def getInfo(html,soup):
#获取界面种子url
	global today_task
	movie_list=re.findall(r'https://www\.dmmsee\.net/.{0,8}-\d{0,5}',html)
	updat_list=soup.find_all('button',attrs={"title":"包含最新出種的磁力連結"})
	if(len(updat_list)==30):
		for i in range(len(updat_list)):
			if(updat_list[i].string!='今日新種'):
				del movie_list[i:len(movie_list)]
				today_task=0
				break
			else:
				pass
	else:
		today_task=0
		del movie_list[len(updat_list):30]
	getMessage(movie_list)

def getMessage(mlist):
#获取影片详细信息,保存
	global tag
	path=root+date+'//'+date+'.txt'
	count=0
	mov_dic={}
	for item in mlist:
		actors_name=[]
		#判断今日是否已经更新数据
		if(tag==1):
			break
		count=count+1
		html=getHtml(item)
		soup=BeautifulSoup(html,'html.parser')
		#获取封面
		cover_list=soup.find('a',attrs={'class':'bigImage'})
		url_href=cover_list['href']
		fpath=item.split('/')[-1]+'.jpg'
		saveCover(url_href,fpath)
		message=soup.find('meta',attrs={'name':'description'})['content']
		#print(message)
		actors=soup('div',attrs={'class':'star-name'})
		if(len(actors)==0):
				actors_name.append('暂无出演者信息')
		else:
			for act in actors:
				actors_name.append(act.a.string)
		mov_dic['主要信息']=message
		mov_dic['演员']=actors_name	
		try:
			with open(path,'a+',encoding='utf-8') as f:
				f.write(str(mov_dic)+'\n')
				print('\r种子信息当前进度:{:2f}%\r'.format(count*100/len(mlist),end=''))				
		except:
			print('\r种子信息当前进度:{:2f}%\r'.format(count*100/len(mlist),end=''))
			pass
	print('信息文件已保存')		
				

def saveCover(url,fname):
#保存封面
	cover_root=date_root+'Cover//'
	path=cover_root+fname
	print(path)
	try:
		if not os.path.exists(root):
			os.mkdir(root)
		if not os.path.exists(date_root):
			os.mkdir(date_root)
		if not os.path.exists(cover_root):
			os.mkdir(cover_root)	
		if not os.path.exists(path):
			r = requests.get(url)
			with open(path,'wb') as f:
				f.write(r.content)
				f.close()
				print(fname.split('.')[0]+"保存成功")
		else:
			print('文件已存在')		
	except:
		print(fname.split()[0]+'保存失败')		


headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36',
		'Referer': 'https://www.dmmsee.net/'}
Ori_url='https://www.dmmsee.net/'
root='D://JavSpider//'

tag=0
today_task=1       #今日新种任务
date=time.strftime('%Y-%m-%d',time.gmtime())
date_root=root+date+'//'	
def main():
	#print(html[500:1500])
	page=1
	global tag
	if os.path.exists(date_root):
		tag=1
	while(today_task):
		print('爬取第'+str(page)+'页')
		get_url=Ori_url+'page/'+str(page)
		page=page+1
		html=getHtml(get_url)
		soup=BeautifulSoup(html,'html.parser')
		getInfo(html,soup)
	print('今日新种保存完毕')	
main()	
