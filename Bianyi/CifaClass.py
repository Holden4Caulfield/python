class CifaAny():
    key_word = ["int", "main", "void", "if", "char", "else"]  # 关键字
    limit_bound = ["<=", "==", "=", ">", "<", "+", "-", "*", "/", "{",
                   "}", ",", ";", "(", ")", '"', "'", ' ','#']
    dict_kw = {}
    num_kw = 1
    dict_lb = {}
    num_lb = 1
    dict_str = {}
    num_str = 1
    dict_char = {}
    num_char = 1
    dict_id = {}
    num_id = 1
    dict_const = {}
    num_const = 1
    lis_next = []

    def isId(self, token):
        try:
            if(token == ''):
                return 0
            if(token in self.dict_id.keys()):
                return 1
            self.dict_id[token] = list(str(self.num_id))
            self.num_id = self.num_id + 1
            return 1
        except:
            return 1

    def isKw(self, token):

        try:
            if(token in self.dict_kw.keys()):
                return 1
            if(token in self.key_word):
                self.dict_kw[token] = list(str(self.num_kw))
                self.num_kw = self.num_kw + 1
                return 1
            else:
                return 0
        except:
            return 0

    def isLb(self, token):

        try:
            if(token == ' '):
                return 1
            if(token in self.dict_lb.keys()):
                return 1
            if(token in self.limit_bound):
                self.dict_lb[token] = list(str(self.num_lb))
                self.num_lb = self.num_lb + 1
                return 1
            else:
                return 0
        except:
            return 0

    def isStr(self, token):
        try:
            if(len(token) == 1):
                self.dict_char[token] = list(str(self.num_char))
                self.num_char = self.num_char + 1
            else:
                self.dict_str[token] = list(str(self.num_str))
                self.num_str = self.num_str + 1
            return 1
        except:
            return 0

    def isChar(self, token):

        if(len(token) == 1):
            self.dict_char['num_char'] = token
            self.num_char = self.num_char + 1

    def isConst(self, token):

        try:
            if(token.isdigit() or '.' in token):
                self.dict_const[token] = list(str(self.num_const))
                self.num_const = self.num_const + 1
                return 1
        except:
            return 0

    def analys(self, r_list):
        r_list.append(' ')
        token = ''
        str_tag = 0
        tp = 0
        st_tag = 0  # 开始
        for ch in r_list:
            token = token + ch
            # print('token='+token)
            if(tp == 1):
                tp = 0
                token = ''
                continue
            if(self.isKw(token)):
                token = ''
                continue
            try:
                if(((ch + r_list[r_list.index(ch) + 1]) in self.limit_bound) and (ch in self.limit_bound)):
                    self.isLb((ch + r_list[r_list.index(ch) + 1]))
                    tp = 1
                    print('lalla ' + token)
                    if(self.isConst(token[:-1])):
                        pass
                    else:
                        self.isId(token[:-1])
                        pass
                    continue
                elif(self.isLb(ch)):
                    st_tag = 1
                    # 匹配字符串
                    if(ch == '"' or ch == "'"):
                        # 字符串启动标志
                        str_tag = ~str_tag
                        # print('dong'+str(str_tag)+str(st_tag))
                        if(str_tag == 0 and st_tag == 1):
                            st_tag = 0  # token中包含字符串,形如  alala"
                            # print('strr')
                            self.isStr(token[:-1])
                    else:
                        if(self.isConst(token[:-1])):
                            pass
                        else:
                            self.isId(token[:-1])
                            pass
                    token = ''
                    continue
            except:
                pass
        self.bianhao()
        self.scre(r_list)

    def scre(self, r_list):
        token = ''
        tp = 0
        str_tag = 0
        st_tag = 0  # 开始
        for ch in r_list:
            token = token + ch
            # print('token='+token)
            if(tp == 1):
                tp = 0
                token = ''
                continue
            if(token in self.key_word):
                self.lis_next.append(token)
                print("{0:<10}{1:^6}{2:>5}>".format(
                    'kw', token, self.dict_kw[token][1]))

                continue
            try:
                if(((ch + r_list[r_list.index(ch) + 1]) in self.limit_bound)):

                    tp = 1
                    if((token[:-1]).isdigit()):
                        self.lis_next.append(token[:-1])
                        print("{0:<10}{1:^6}{2:>5}>".format(
                            '数字', token[:-1], self.dict_const[token[:-1]][1]))

                    else:
                        try:
                            self.lis_next.append(token[:-1])
                            print("{0:<10}{1:^6}{2:>5}>".format(
                                'id', token[:-1], self.dict_id[token[:-1]][1]))
                        except:
                            pass
                    print("{0:<10}{1:^6}{2:>5}>".format(
                        '界限', (ch + r_list[r_list.index(ch) + 1]), self.dict_lb[(ch + r_list[r_list.index(ch) + 1])][1]))
                    self.lis_next.append((ch + r_list[r_list.index(ch) + 1]))

                    continue
                elif(ch in self.limit_bound):
                    st_tag = 1
                    # 匹配字符串
                    if(ch == '"' or ch == "'"):
                        # 字符串启动标志
                        str_tag = ~str_tag
                        # print('dong'+str(str_tag)+str(st_tag))
                        if(str_tag == 0 and st_tag == 1):
                            st_tag = 0  # token中包含字符串,形如  alala"
                            # print('strr')
                            if(len(token) == 2):
                                self.lis_next.append(token[:-1])
                                print("{0:<10}{1:^6}{2:>5}>".format(
                                    '字符', token[:-1], self.dict_char[token[:-1]][1]))

                            else:
                                self.lis_next.append(token[:-1])
                                print("{0:<10}{1:^6}{2:>5}>".format(
                                    'string', token[:-1], self.dict_str[token[:-1]][1]))

                            token = ''

                    else:
                        # print('token====='+token)

                        if((token[:-1]).isdigit() or '.' in token[:-1]):
                            self.lis_next.append(token[:-1])
                            print("{0:<10}{1:^6}{2:>5}>".format(
                                '数字', token[:-1], self.dict_const[token[:-1]][1]))
                            token = ''
                

                        else:
                            try:
                                self.lis_next.append(token[:-1])
                                print("{0:<10}{1:^6}{2:>5}>".format(
                                    'id', token[:-1], self.dict_id[token[:-1]][1]))
                            except:
                                pass
                            token = ''
                    if(ch != ' '):
                        self.lis_next.append(ch)
                        print("{0:<10}{1:^6}{2:>5}>".format(
                            '界限', ch, self.dict_lb[ch][1]))
                    token = ''
                    continue
            except:
                pass

    def bianhao(self):
        num = 4
        for item in self.dict_id.items():
            item[1].append(0)
        for item in self.dict_str.items():
            item[1].append(1)
        for item in self.dict_const.items():
            item[1].append(2)
        for item in self.dict_char.items():
            item[1].append(3)
        for item in self.dict_kw.items():
            item[1].append(num)
            num = num + 1
        for item in self.dict_lb.items():
            item[1].append(num)
            num = num + 1


# rea_lis = []
# f = open('bianyi.txt').read()
# for ch in f:
# 	if(ch in ['\n', '\t', '']):
# 		continue
# 	rea_lis.append(ch)
# 	# print(ch,end=' ')
# print(rea_lis)
# pp=CifaAny()
# pp.analys(rea_lis)
# pp.bianhao()
# pp.scre(rea_lis)
