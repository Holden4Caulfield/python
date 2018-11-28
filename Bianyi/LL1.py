from CifaClass import CifaAny
class LL1():
    # 手动构造预测分析表
    dists = {
        ('E', 'i'): 'TH',
        ('E', '('): 'TH',
        ('H', '-'): '-TH',
        ('H', '+'): '+TH',
        ('H', ')'): 'e',
        ('H', '#'): 'e',
        ('T', 'i'): 'FY',
        ('T', '('): 'FY',
        ('Y', '+'): 'e',
        ('Y', '*'): '*FY',
        ('Y', '/'): '/FY',
        ('Y', ')'): 'e',
        ('Y', '#'): 'e',
        ('F', 'i'): 'i',
        ('F', '('): '(E)',
    }

    # 构造终结符集合
    Vt = ['+', '*', '(', ')','/','-','i']
    id_dict={}

    # 构造非终结符集合
    Vh = ['E', 'H', 'T', 'Y', 'F']

    # 获取输入栈中的内容
    next_word=[]
    def __init__(self,lis,id_d):
        self.next_word=lis
        self.id_dict=id_d
        self.Vt=self.Vt+list(id_d.keys())
        self.masterctrl(lis)

    def printstack(self,stack):
        rtu = ''
        for i in stack:
            rtu += i
        return rtu


    # 得到输入串剩余串
    def printstr(self,lis, index):
        rtu = ''
        for i in range(index, len(lis), 1):
            rtu +=lis[i]
        return rtu


    # 定义error函数
    def error(self):
        print('Error')
        exit()


    # 总控程序
    def masterctrl(self,lis):
        '''
        总控程序，用于进程文法的判断
        '''
        # 用列表模拟栈
        stack = []
        location = 0
        # 将#号入栈
        stack.append(lis[location])

        # 将文法开始符入栈
        stack.append('E')
        # 将输入串第一个字符读进a中
        location += 1
        a = lis[location]
        #print(self.id_dict.keys())         当前所有非终结符，除去运算符号
        if(a in self.id_dict.keys()):
            a='i'
        self.printstack(stack)
        flag = True
        count = 0
        print('%d\t\t%s\t\t%s' % (count, self.printstack(stack), self.printstr(lis,location)))
        while flag:
            if count == 0:
                pass
            else:
                if x in self.Vt:
                    print('%d\t\t%s\t\t%s' % (count,self.printstack(stack), self.printstr(lis, location)))
                else:
                    print('%d\t\t%s\t\t%s\t\t%s->%s' % (count, self.printstack(stack), self.printstr(lis, location), x, s))
            x = stack.pop()
            if x in self.Vt:
                if lis[location] in list(self.id_dict.keys()):
                    lis[location]='i'
                if x == lis[location]:
                    location += 1
                    if location==len(lis):
                        self.error()
                    a = lis[location]
                    if(a in self.id_dict.keys()):
                        a='i'
                else:
                    self.error()
            elif x == '#':
                if x == a:
                    flag = False
                else:
                    error()
            elif (x, a) in self.dists.keys():
                s = self.dists[(x, a)]
                for i in range(len(s) - 1, -1, -1):
                    if s[i] != 'e':
                        stack.append(s[i])
            else:
                self.error()
            count += 1

str = '#(Aa+Bb)*(4*4.63+5)/55.5+6#'
rea_lis=[]

for ch in str:
    if(ch in ['\n','\t','']):
        continue
    rea_lis.append(ch)
examp=CifaAny()
examp.analys(rea_lis)
id_d=dict(examp.dict_id,**examp.dict_const)
lis_word=[]
for item in examp.lis_next:
    if item=='':
        continue
    lis_word.append(item)
print("步骤\t\t符号栈\t\t输入串\t\t\t所用产生式")
ltext=LL1(lis_word,id_d)
