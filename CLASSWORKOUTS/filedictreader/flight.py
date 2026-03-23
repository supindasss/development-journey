fr=open("CLASSWORKOUTS\\filedictreader\\flight.txt","r")

flight=[]

for line in fr:

    data=line.rstrip("\n").rsplit(",")

    single_line={"year":data[0],"month":data[1],"passengers":int(data[2])}

    flight.append(single_line)

print(flight)    

year_wise_count={}

for passengers in flight:

    year=passengers.get("year")

    passe=passengers.get("passengers")

    if year in year_wise_count:

        year_wise_count[year]+=passe

    else:
        year_wise_count[year]=passe  

print(year_wise_count)  

year_wise_count_sorted=sorted([[v,k] for k,v in year_wise_count.items()],reverse=True)

print(year_wise_count_sorted)
