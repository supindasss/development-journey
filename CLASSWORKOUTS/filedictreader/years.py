from csv import DictReader#csv=>list of dictionary[csv.py>DictReader]
fr=open("CLASSWORKOUTS\\filedictreader\\years.txt")
flight=[]

for line in fr:

    data=line.rstrip("\n").rsplit(",")

    passenger_data={"year":data[0],"month":data[1],"passengers":int(data[2])}

    flight.append(passenger_data)

year_wise_count={} 

for p in flight:

    year=p.get("year")

    passengers=p.get("passengers")

    if year in year_wise_count:
       
       year_wise_count[year]+=passengers

    else:
        year_wise_count[year]=passengers   
print(year_wise_count) 
yesr_wise_count_sorted=sorted([[v,k] for k,v in year_wise_count.items()],reverse=True)      



