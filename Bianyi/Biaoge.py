import sys
sys.setrecursionlimit(1000000)
Lan = ['E-TH', 'H-wTH', 'H-e', 'T-FG', 'G-bFG', 'G-e', 'F-i', 'F-(E)']
Vn = ['E', 'T', 'H', 'G', 'F']
first_dict = {}
follow_dict = {}


def get_first():
    count=1
    for line in Lan[::-1]:
        if line[0] not in first_dict.keys():
            first_dict[line[0]] = ['']
        if line[2] in Vn:
            if line[2] in first_dict.keys():
                first_dict[line[0]] += first_dict[line[2]]
        elif line[2] == 'e':
            first_dict[line[0]] += 'e'
        else:
            first_dict[line[0]] += line[2]

        count=count+1
    for item in first_dict.values():
        while(item[0] == ''):
            item.remove('')
        pass


def get_follow(char):
    for line in Lan:
        if char not in follow_dict.keys():
            follow_dict[char] = ['e']
            print(follow_dict)
        if char in line[2:]:
            print(line)
            if line.index(char) == len(line) - 1:
                follow_dict[char] += get_follow(line[0])
            else:
                try:
                    if line[line.index(char,2) + 1] in Vn:
                        if 'e' in first_dict[line[line.index(
                            char, 2) + 1]]:
                            follow_dict[char] += get_follow(line[line.index(
                                char, 2) + 1])
                        follow_dict[char] += first_dict[line[line.index(
                            char, 2) + 1]]
                    else:
                        follow_dict[char] += line[line.index(char,2) + 1]
                except:
                    pass
    follow_dict[char]=list(set(follow_dict[char]))
    return follow_dict[char]

get_first()
for char in ['H', 'G']:
    get_follow(char)
for item in follow_dict.items():
    print(item)
print(follow_dict)

select={}
count=1
for line in Lan:
    if line[2] in Vn:
        select[count]=first_dict[line[2]]
    elif line[2]=='e':
        select[count]=follow_dict[line[0]]
    else:
        select[count]=list(line[2])

    count=count+1

print(select)
