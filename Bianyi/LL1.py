from CifaClass import CifaAny            #词法分析
from preTabel import dic_Tab             #构造分析
class LL1():
    # 构造预测分析表
    dists = {
        # ('E', 'i'): 'TH',
        # ('E', '('): 'TH',
        # ('H', '-'): '-TH',
        # ('H', '+'): '+TH',
        # ('H', ')'): 'e',
        # ('H', '#'): 'e',
        # ('T', 'i'): 'FY',
        # ('T', '('): 'FY',
        # ('Y', '+'): 'e',
        # ('Y', '-'): 'e',
        # ('Y', '*'): '*FY',
        # ('Y', '/'): '/FY',
        # ('Y', ')'): 'e',
        # ('Y', '#'): 'e',
        # ('F', 'i'): 'i',
        # ('F', '('): '(E)',
    }
    ano_lis=[]
    # 构造终结符集合
    t=0
    lis_sem=[]
    Vt = ['+', '*', '(', ')','/','-','i']
    id_dict={}               #标识符，常量表
    sem=[]
    # 构造非终结符集合
    Vh = ['E', 'H', 'T', 'Y', 'F']

    next_word=[]        #token串
    def __init__(self,lis,id_d,dis):
        self.dists=dis
        self.next_word=lis
        self.ano_lis=lis
        self.id_dict=id_d
        self.Vt=self.Vt+list(id_d.keys())
        self.masterctrl(lis)
        for item in self.lis_sem:
            print(item)

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


    def error(self):
        print('Error')
        exit()


    def masterctrl(self,lis):
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
        if(a in self.id_dict.keys()):           #把标识符改为i
            a='i'
        self.printstack(stack)
        flag = True
        count = 0
        tag_id=''
        tag_num=0
        op=[]
        print('{:<10}\t{:<20}\t{:<30}\t'.format(count, self.printstack(stack), self.printstr(lis,location)))
        while flag:

            if count == 0:
                pass
            else:
                if x in self.Vt:
                    print('{:<10}\t{:<20}\t{:<30}\t'.format(count,self.printstack(stack), self.printstr(lis, location)))
                else:
                    print('{:<10}\t{:<20}\t{:<30}\t{:>15}->{:20}'.format(count, self.printstack(stack), self.printstr(lis, location), x, s))
            x = stack.pop()
            if(x=='P'):
                 self.push(tag_id)
                 tag_num=0
                # print(self.sem)
                 x=stack.pop()
            if(x=='Q'):
                 self.GEQ(op.pop())
                # print(self.sem)
                 x=stack.pop()
            if x in self.Vt:
                if x in ['+','-','*','/']:
                    op.append(x)
                if lis[location] in list(self.id_dict.keys()):
                    tag_id=lis[location]
                    tag_num=1
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
                    self.error()
            elif (x, a) in self.dists.keys():
                s = self.dists[(x, a)]
                if(s in ['*FY','/FY','-TH','+TH']):
                    s=list(s)
                    s.insert(2,'Q')
                    s=''.join(s)
                if s=='i':
                    s+='P'
                for i in range(len(s) - 1, -1, -1):
                    if s[i] != 'e':
                        stack.append(s[i])
            else:
                self.error()
            count += 1

    def push(self,word):
        self.sem.append(word)

    def GEQ(self,Char):
        #print('op='+Char)
        t_now='t'+str(self.t+1)
        a=self.sem.pop()
        b=self.sem.pop()
        #print('({} {} {} {})'.format(Char,b,a,t_now))
        strn='('+Char+' '+b+' '+a+' '+t_now+')'
        self.lis_sem.append(strn)
        self.t=self.t+1
        self.sem.append(t_now)


str1 = '#(Aa+Bb)*(4*4.63+5)/55+3#'
rea_lis=[]
for ch in str1:
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


print('{:<10}\t{:^15}\t{:^20}\t{:>20}'.format('步骤','符号栈','输入串','产生公式'))
table=dic_Tab()
ltext=LL1(lis_word,id_d,table.dists)
