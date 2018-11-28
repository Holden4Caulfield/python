from CifaClass import CifaAny
# E -> T G
#  G-> w0 T G|ε
#  T -> F H
#  H-> w1 F H|ε
#  F -> I | ( E )

w0=['+','-']
w1=['*','/']

class Recur():

    string_input=''
    word=''
    next_word=[]
    num=0
    wor_dic={}
    def __init__(self,lis,dic):
        self.next_word=lis
        self.word=lis[0]
        self.wor_dic=dic
        self.parser()
    def E(self):
        print('E-->TG')
        self.T()
        self.G()
    def T(self):
        print('T-->FH')
        self.F()
        self.H()
    def F(self):
        if self.word in self.wor_dic:
            print('F-->I')
            self.nextword()
            return
        elif self.word=='(':
            print('F-->(E)')
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
            print('G-->wo TG')
            self.nextword()
            self.T()
            self.G()
        else:

            print('G-->##')
    def H(self):
        if self.word in w1:
            print('H-->w1 FH')
            self.nextword()
            self.F()
            self.H()
            return
        else:
            print('H-->##')
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
