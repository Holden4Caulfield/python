input = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
sortls = sorted(input,key=(lambda x:x[1]))
print(sortls)
sortlist = sorted(sortls,key=(lambda x:x[0]),reverse=True)
print(sortlist)
output = []
for item in sortlist:
	print(item[1])
	output.insert(item[1],item)
	print(item[1])
   # print(output)

