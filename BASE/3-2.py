a=eval(input())
print(str(abs(a))+" ",end="")
b=abs(a)+10
c=abs(a)-10
d=abs(a)*10
if a >=0:
	print("{} {} {}".format(abs(b),abs(c),abs(d)))
else:
	print("{} {} {}".format(-abs(b),-abs(c),-abs(d)))
