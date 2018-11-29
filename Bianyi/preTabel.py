class dic_Tab():
    Lan = ['E-TH', 'H-wTH', 'H-e', 'T-FY', 'Y-bFY', 'Y-e', 'F-i', 'F-(E)']
    Vn = ['E', 'T', 'H', 'Y', 'F']
    first_dict = {}
    follow_dict = {}
    dists={}
    select={}
    def __init__(self):
        self.get_first()
        for char in ['H', 'Y']:
            self.get_follow(char)
        self.get_select()
    def get_first(self):
        count=1
        for line in self.Lan[::-1]:
            if line[0] not in self.first_dict.keys():
                self.first_dict[line[0]] = ['']
            if line[2] in self.Vn:
                if line[2] in self.first_dict.keys():
                    self.first_dict[line[0]] += self.first_dict[line[2]]
            elif line[2] == 'e':
                self.first_dict[line[0]] += 'e'
            else:
                self.first_dict[line[0]] += line[2]

            count=count+1
        for item in self.first_dict.values():
            while(item[0] == ''):
                item.remove('')
            pass


    def get_follow(self,char):
        for line in self.Lan:
            if char not in self.follow_dict.keys():
                self.follow_dict[char] = ['e']
            if char in line[2:]:
                if line.index(char) == len(line) - 1:
                    self.follow_dict[char] += self.get_follow(line[0])
                else:
                    try:
                        if line[line.index(char,2) + 1] in self.Vn:
                            if 'e' in self.first_dict[line[line.index(
                                char, 2) + 1]]:
                                self.follow_dict[char] += self.get_follow(line[line.index(
                                    char, 2) + 1])
                            self.follow_dict[char] += self.first_dict[line[line.index(
                                char, 2) + 1]]
                        else:
                            self.follow_dict[char] += line[line.index(char,2) + 1]
                    except:
                        pass
        self.follow_dict[char]=list(set(self.follow_dict[char]))
        return self.follow_dict[char]



    def get_select(self):
        count=0
        for line in self.Lan:
            if line[2] in self.Vn:
                self.select[count]=self.first_dict[line[2]]
            elif line[2]=='e':
                self.select[count]=self.follow_dict[line[0]]
            else:
                self.select[count]=list(line[2])
            count=count+1
        for item in self.select.items():
            location=item[0]
            for i in item[1]:
                if i =='w':
                    for j in ['+','-']:
                        tup=(self.Lan[location][0],j)
                        self.dists[tup]=j+self.Lan[location][3:]
                        if(self.Lan[location][-1]=='e'):
                            self.dists[tup]='e'
                elif i =='b':
                    for j in ['*','/']:
                        tup=(self.Lan[location][0],j)
                        self.dists[tup]=j+self.Lan[location][3:]
                        if(self.Lan[location][-1]=='e'):
                            self.dists[tup]='e'
                elif i == 'e':
                    tup=(self.Lan[location][0],'#')
                    self.dists[tup]=self.Lan[location][2:]
                else:
                    tup=(self.Lan[location][0],i)
                    self.dists[tup]=self.Lan[location][2:]

lp=dic_Tab()
