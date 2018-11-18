import re
line = "Cats li are smarter than dogs"
matchObj = re.findall( r'\d{0,3}', '123 125')
if matchObj:
    print(matchObj)
else:
    print ("No match!!")