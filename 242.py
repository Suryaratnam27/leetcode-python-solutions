s="anagram"
t="anagram"

s_char={}
t_char={}

for c in s:
    s_char[c]=0
for d in t:
    t_char[d]=0
for c in s:
    s_char[c]+=1
for d in t:
    t_char[d]+=1

s_char={}

alph="qwertyuioplkjhgfdsazxcvbnm"
ch_char="abcdefghijklmnopqrstuvwxyz"


for c in alph:
    s_char[c]=False
for c in ch_char:
    s_char[c]=True
flag=False
for b in s_char.values():
    if not b:
        flag=True

if flag:
    print("False")
else:
    print("True")
