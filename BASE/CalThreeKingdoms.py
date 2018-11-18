import jieba
txt=open('threekingdoms.txt','r',encoding='utf-8').read()
words=jieba.lcut(txt)
counts={}
for word in words:
	if len(word)==1:
		continue
	elif word=="诸葛亮" or word=="孔明曰":
		rword="孔明"
	elif word=="曹操" or word=="孟德":	
		rword="曹操"
	else:
		rword=word
	counts[rword]=counts.get(rword,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
	word,count=items[i]
	print("{0:<10}{1:>15}".format(word,count))		

