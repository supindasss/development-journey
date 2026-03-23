f_all=open("fullstackjourney\\fileoperations\\students_all.txt","r")
f_pass=open("fullstackjourney\\fileoperations\\students_passed.txt","r")

n_all={i.rstrip("\n") for i in f_all}
n_pass={j.rstrip("\n") for j in f_pass}
difference=n_all.difference(n_pass)
print(difference)
