"""word="ihave2pen1pencilonecar"
for ch in word:
    if ch.isdigit():
        print(ch)"""
#w.a.p to display alphabet count,digit count ,special charactret count
word="aman##aplan**panamawith2car1bike"
dcount=0
acount=0
chj=0
for ch in word:
    if ch.isdigit():
        dcount=dcount+1   
    elif ch.isalpha():
        acount=acount+1
    else:
        chj=chj+1    
print(dcount) 
print(acount) 
print(chj)