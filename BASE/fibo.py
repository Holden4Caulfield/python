def fib(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fib(n-2)+fib(n-1)

n=eval(input())
ls=[]
for i in range(1000):
	num=fib(i)
	if num<=n:
		ls.append(num)
	else:
		break
sum=0
for i in range(len(ls)):
	print(str(ls[i]),end="")
	sum+=ls[i]
print(str(sum)+','+str(int(sum/(len(ls)))))	