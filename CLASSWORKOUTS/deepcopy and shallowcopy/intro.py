arun_fav_color= ["red","green","blue"]

hari_fav_color=arun_fav_color

hari_fav_color[0]="purple"

print("arun fvt = ",arun_fav_color) #the both outputs are same for arun_fav color and 

print("hari fvt = ",hari_fav_color)#hari_fav color so here there is doent create any seperate objects for it

#when once it changes in to one index to a new value that will effect for all objects,here pointing same objects
# for pointing different object we use copy of method 

arun=["red","green","black"]
hari=arun.copy()
hari[0]="yellow"

print("arun = ",arun)

print("hari = ",hari)

