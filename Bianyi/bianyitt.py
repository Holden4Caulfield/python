lis=['a','b','c']
print(lis.index('b')+1)
'''if(tp==1):
			tp==0
			con'''
		if(isKw(token)):
			token=''
			continue
		if(((ch+r_list[r_list.index(ch)+1]) in limit_bound ) and (ch in limit_bound) ):
			isLb((ch+r_list[r_list.index(ch)+1]))
			tp=1
			continue