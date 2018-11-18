#GovRptWordCloudv1.py
import jieba
import wordcloud
from scipy.misc import imread
mask=imread('lian.png')
f = open("data.txt",'r',encoding='utf-8')
t = f.read()

f.close() 
w=wordcloud.WordCloud(font_path="msyh.ttc",\
	background_color="white",\
	mask=mask)
#w=wordcloud.WordCloud(background_color="white")
w.generate(" ".join(jieba.lcut(t)))
w.to_file("grwordcloud.png")
