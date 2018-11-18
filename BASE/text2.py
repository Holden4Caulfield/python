n=input()
sum=0
if not n.isdigit():
	print("输入有误，请输入正整数")
else:
	if type(eval(n))!=int:
		print("输入有误，请输入正整数")
	else:
		for i in range(1,eval(n)+1):
			a=i
			b=1
			for j in range(1,a+1):
				b=b*j
			sum=b+sum
		if eval(n)==0:print("输入有误，请输入正整数")
		else:print(sum)	

