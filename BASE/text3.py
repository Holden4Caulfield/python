n=input()
try:
	if 90<= eval(n) <=100:
		print("输入成绩属于A级别。")
		print("祝贺你通过考试！")
	elif 80<= eval(n) <90:
		print("输入成绩属于B级别。")
		print("祝贺你通过考试！")
	elif 70<= eval(n) <80:
		print("输入成绩属于C级别。")
		print("祝贺你通过考试！")
	elif 60<= eval(n) <70:
		print("输入成绩属于D级别。")
		print("祝贺你通过考试！")
	else:
		print("输入成绩属于E级别。")	
except:
	print("输入数据有误！")
finally:
	print("好好学习，天天向上!")					
	