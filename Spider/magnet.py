import re
import requests
from bs4 import BeautifulSoup

headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36',
		'Referer': 'https://www.dmmsee.net/DDT-608'}


r=requests.get("https://www.dmmsee.net/ajax/uncledatoolsbyajax.php?floo&gid=38623343653&uc=0&img='https://pics.javcdn.pw/cover/6tlr_b.jpg'",headers=headers)
r.encoding='utf-8'
html=r.text
soup=BeautifulSoup(html,'html.parser')
tr=soup.find_all('tr')
daxiao=re.findall(r'\d{0,3}\.\d{0,3}GB',html)
print(daxiao)