from CifaClass import CifaAny
# E -> T G
#  G-> w0 T G|ε
#  T -> F H
#  H-> w1 F H|ε
#  F -> I | ( E )
w0=['+','-']
w1=['*','/']
class Recur():

    sem=[]
    t=1
    string_input=''
    word=''
    next_word=[]              #token 串
    num=0
    wor_dic={}               # 数字，标识符，和w0 w1区别开
    lis_sem=[]
    def __init__(self,lis,dic):
        self.next_word=lis
        self.word=lis[0]
        self.wor_dic=dic
        self.parser()
        print(self.lis_sem)
    def E(self):
        print('当前单词{:<4}\t\t\t使用文法{}'.format(self.word,'E-->TG'))
        self.T()
        self.G()
    def T(self):
        print('当前单词{:<4}\t\t\t使用文法{}'.format(self.word,'T-->FH'))
        self.F()
        self.H()
    def F(self):
        if self.word in self.wor_dic:
            print('当前单词{:<4}\t\t\t使用文法{}'.format(self.word,'F-->I'))
            self.push(self.word)
            self.nextword()
            return
        elif self.word=='(':
            print('当前单词{:<4}\t\t\t使用文法{}'.format(self.word,'F-->(E)'))
            self.nextword()
            self.E()
            if self.word==')':
                self.nextword()
                return
            else:
                print('error')
                exit(0)
        else:
            print('error')
            exit(0)

    def G(self):
        if self.word in w0:
            print('当前单词{:<4}\t\t\t使用文法{}'.format(self.word,'G-->wo TG'))
            op=self.word
            self.nextword()

            self.T()
            self.GEQ(op)
            self.G()
        else:
            print('当前单词{:<4}\t\t\t使用文法{}'.format(self.word,'G-->##'))
    def H(self):
        if self.word in w1:
            print('当前单词{:<4}\t\t\t使用文法{}'.format(self.word,'H-->w1 FH'))
            op=self.word
            self.nextword()
            self.F()
            self.GEQ(op)
            self.H()
            return
        else:
            print('当前单词{:<4}\t\t\t使用文法{}'.format(self.word,'H-->##'))
            return
    def nextword(self):
        try:
            self.num=self.num+1
            self.word=self.next_word[self.num]
        except:
            pass
        #print(self.word)
    def parser(self):
        self.E()
        if self.word!='#':
            print('error  缺少终结符#')
            exit(0)
        else:
            print('done')

    def GEQ(self,Char):
        strn=''
        t_now='t'+str(self.t)
        a=self.sem.pop()
        b=self.sem.pop()
        #print('({} {} {} {})'.format(Char,b,a,t_now))

        strn='('+Char+' '+b+' '+a+' '+t_now+')'
        self.lis_sem.append(strn)
        self.t=self.t+1
        self.sem.append(t_now)
    def push(self,word):
        self.sem.append(word)


rea_lis=[]
f='(Aa+Bb)*(4*4.63+5)/55+3#'
for ch in f:
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
yufa=Recur(lis_word,id_d)
