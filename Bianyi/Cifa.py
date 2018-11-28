
def isId(token):
	global num_id
	try:
		if(token==''):
			return 0
		if(token in dict_id.keys()):
			return 1
		dict_id[token]=list(str(num_id))
		num_id=num_id+1
		return 1
	except:
		return 1

def isKw(token):
	global num_kw
	try:
		if(token in dict_kw.keys()):
			return 1
		if(token in key_word):
			dict_kw[token]=list(str(num_kw))
			num_kw=num_kw+1
			return 1
		else:
			return 0
	except:
		return 0

def isLb(token):
	global num_lb
	try:
		if(token==' '):
			return 1
		if(token in dict_lb.keys()):
			return 1
		if(token in limit_bound):
			dict_lb[token]=list(str(num_lb))
			num_lb=num_lb+1
			return 1
		else:
			return 0
	except:
		return 0


def isStr(token):
	global num_str
	global num_char
	try:
		if(len(token)==1):
			dict_char[token]=list(str(num_char))
			num_char=num_char+1
		else:
			dict_str[token]=list(str(num_str))
			num_str=num_str+1
		return 1
	except:
		return 0


def isChar(token):
	global num_char
	if(len(token)==1):
		dict_char['num_char']=token
		num_char=num_char+1

def isConst(token):
	global num_const
	try:
		if(token.isdigit() or '.' in token):
			dict_const[token]=list(str(num_const))
			num_const=num_const+1
			return 1
	except:
		return 0

def analys(r_list):
	token=''
	str_tag=0
	tp=0
	st_tag=0            #开始
	for ch in r_list:
		token=token+ch
		#print('token='+token)
		if(tp==1):
			tp=0
			print('hhah'+token)
			token=''
			continue
		if(isKw(token)):
			token=''
			continue
		try:
			if(((ch+r_list[r_list.index(ch)+1]) in limit_bound ) and (ch in limit_bound) ):
				isLb((ch+r_list[r_list.index(ch)+1]))
				tp=1
				print('lalla '+token)
				if(isConst(token[:-1])):
						pass
				else:
					isId(token[:-1])
					pass
				continue
			elif(isLb(ch)):
				st_tag=1
				#匹配字符串
				if(ch=='"' or ch=="'"):
			       	#字符串启动标志
					str_tag=~str_tag
					#print('dong'+str(str_tag)+str(st_tag))
					if(str_tag==0 and st_tag==1):
						st_tag=0        #token中包含字符串,形如  alala"
						#print('strr')
						isStr(token[:-1])
				else:
					if(isConst(token[:-1])):
						pass
					else:
						isId(token[:-1])
						pass
				token=''
				continue
		except:
			pass

def scre(r_list):
	token=''
	tp=0
	str_tag=0
	st_tag=0            #开始
	for ch in r_list:
		token=token+ch
		print('token='+token)
		if(tp==1):
			print('555'+token)
			tp=0
			token=''
			continue
		if(token in key_word):
			print("{0:<10}{1:^6}{2:>5}>".format('kw',token,dict_kw[token][1]))
			continue
		try:
			if(((ch+r_list[r_list.index(ch)+1]) in limit_bound )):
				print('66'+token)

				tp=1
				if((token[:-1]).isdigit()):
					print("{0:<10}{1:^6}{2:>5}>".format('数字',token[:-1],dict_const[token[:-1]][1]))
				else:
					try:
						print("{0:<10}{1:^6}{2:>5}>".format('id',token[:-1],dict_id[token[:-1]][1]))
					except:
						pass
				print("{0:<10}{1:^6}{2:>5}>".format('界限',(ch+r_list[r_list.index(ch)+1]),dict_lb[(ch+r_list[r_list.index(ch)+1])][1]))
				continue
			elif(ch in limit_bound ):
				st_tag=1
				#匹配字符串
				if(ch=='"' or ch=="'"):
			       	#字符串启动标志
					str_tag=~str_tag
					#print('dong'+str(str_tag)+str(st_tag))
					if(str_tag==0 and st_tag==1):
						st_tag=0        #token中包含字符串,形如  alala"
						#print('strr')
						if(len(token)==2):
							print("{0:<10}{1:^6}{2:>5}>".format('字符',token[:-1],dict_char[token[:-1]][1]))
						else:
							print("{0:<10}{1:^6}{2:>5}>".format('string',token[:-1],dict_str[token[:-1]][1]))
						token=''

				else:
					#print('token====='+token)
					if((token[:-1]).isdigit() or '.' in token[:-1]):
						print('here')
						print("{0:<10}{1:^6}{2:>5}>".format('数字',token[:-1],dict_const[token[:-1]][1]))
						token=''
					else:
						try:

							print("{0:<10}{1:^6}{2:>5}>".format('id',token[:-1],dict_id[token[:-1]][1]))
						except:
							pass
						token=''
				if(ch!=' '):
					print("{0:<10}{1:^6}{2:>5}>".format('界限',ch,dict_lb[ch][1]))
				token=''
				continue
		except:
			pass
def bianhao():
	num=4
	for item in dict_id.items():
		item[1].append(0)
	for item in dict_str.items():
		item[1].append(1)
	for item in dict_const.items():
		item[1].append(2)
	for item in dict_char.items():
		item[1].append(3)
	for item in dict_kw.items():
		item[1].append(num)
		num=num+1
	for item in dict_lb.items():
		item[1].append(num)
		num=num+1

key_word=["int","main","void","if","char","else"]    #关键字
limit_bound=["<=","==","=",">","<","+","-","*","/","{",
        "}",",",";","(",")",'"',"'",' ']
dict_kw={}
num_kw=1
dict_lb={}
num_lb=1
dict_str={}
num_str=1
dict_char={}
num_char=1
dict_id={}
num_id=1
dict_const={}
num_const=1

token=''
def main():
	global token
	rea_lis=[]
	#f= open('bianyi.txt').read()
	f='4*4+5#'
	for ch in f:
		if(ch in ['\n','\t','']):
			continue
		rea_lis.append(ch)
		#print(ch,end=' ')
	print(rea_lis)
	analys(rea_lis)
	'''print('关键字表',end='')
	print(dict_kw)
	print('字符串',end='')
	print(dict_str)
	print('界限',end='')
	print(dict_lb)
	print('常数',end='')

	print('id',end='')
	'''
	bianhao()
	print(dict_const)
	scre(rea_lis)
main()
