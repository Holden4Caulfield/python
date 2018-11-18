sr1="abcdefghijklmnopqrstuvwxyz"
sr2=sr1.upper()
sr=sr1+sr1+sr2+sr2
in_str=input("")
out_str=""
for j in in_str:
    if j==" ":
        out_str = out_str +" "
        continue
    i=sr.find(j)
    if(i>-1):
        out_str=out_str+sr[i+3]
print(out_str)