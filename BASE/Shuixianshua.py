my_dict = {"a":(2,'5'), "c":(5,'7'), "b":(1,'3')}
ls=list(my_dict.items())
print(ls)
a=[]
ls.sort(key=lambda x:x[1][1], reverse=True)
a=ls
print(a)