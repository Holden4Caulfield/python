st='abcdefghigklmnopqrstuvwxyz'
s=st+st+st.upper()+st.upper()
words=input()
word=''
for i in words:
	if i in s:
		n=s.find(i)
		#print("n={0}".format((n+3)%26))
		word+=s[n+3]
	else:
		word+=i	
print(word)
