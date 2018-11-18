var = 1
while var == 1:                 #制作一个循环，可以反复输入数字来判断是不是“快乐的数”
    a = eval(input())                 #输入一个正整数
    while (a != 1 and a != 4):  #当a不等于1或者4时，一直计算平方和
        num = list(str(a))      #读取输入数字的每位数制成列表
        a = 0                   #初始化a，用于计算每位平方和。此时a值已保存在num里，无需担心丢失。
        for i in num:           #遍历num列表中所有数值，计算出每位数平方和
            a = a + int(i)**2
    if(a == 1):                 #当a等于1时，判断为“快乐的数字”，打印“True”
        print('True')
    else:                       #当a不等于1时，打印“False”（其实不是1就是4）
        print('False')


