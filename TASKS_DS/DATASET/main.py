"""Task 26 || Dataset || 03-03-2026 """
tips_data = [
    {"total_bill": 16.99, "tip": 1.01, "sex": "Female", "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 10.34, "tip": 1.66, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 3},
    {"total_bill": 21.01, "tip": 3.50, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 3},
    {"total_bill": 23.68, "tip": 3.31, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 24.59, "tip": 3.61, "sex": "Female", "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 4},
    {"total_bill": 25.29, "tip": 4.71, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 4},
    {"total_bill": 8.77,  "tip": 2.00, "sex": "Male",   "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 26.88, "tip": 3.12, "sex": "Male",   "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 4},
    {"total_bill": 15.04, "tip": 1.96, "sex": "Male",   "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 14.78, "tip": 3.23, "sex": "Female", "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 10.27, "tip": 1.71, "sex": "Male",   "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 2},
    {"total_bill": 35.26, "tip": 5.00, "sex": "Female", "smoker": "Yes", "day": "Sat",  "time": "Dinner", "size": 4},
    {"total_bill": 15.42, "tip": 1.57, "sex": "Male",   "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 2},
    {"total_bill": 18.43, "tip": 3.00, "sex": "Male",   "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 4},
    {"total_bill": 14.83, "tip": 3.02, "sex": "Female", "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 2},
    {"total_bill": 21.58, "tip": 3.92, "sex": "Male",   "smoker": "Yes", "day": "Fri",  "time": "Dinner", "size": 2},
    {"total_bill": 10.33, "tip": 1.67, "sex": "Female", "smoker": "No",  "day": "Fri",  "time": "Lunch",  "size": 2},
    {"total_bill": 16.29, "tip": 3.71, "sex": "Male",   "smoker": "Yes", "day": "Fri",  "time": "Lunch",  "size": 3},
    {"total_bill": 13.37, "tip": 2.00, "sex": "Female", "smoker": "No",  "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 12.69, "tip": 2.31, "sex": "Male",   "smoker": "Yes", "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 17.92, "tip": 4.08, "sex": "Male",   "smoker": "No",  "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 20.29, "tip": 2.75, "sex": "Female", "smoker": "Yes", "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 15.77, "tip": 2.23, "sex": "Male",   "smoker": "No",  "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 39.42, "tip": 7.58, "sex": "Male",   "smoker": "Yes", "day": "Sat",  "time": "Dinner", "size": 4},
    {"total_bill": 19.82, "tip": 3.18, "sex": "Female", "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 2}
]
#day wise summary
day_wise_summary={}
for line in tips_data:
    tip=float(line.get("tip"))
    day=line.get("day")
    if day in  day_wise_summary:
        day_wise_summary[day]+=tip
    else:
        day_wise_summary[day]=tip 

print(f"day wise summary ={day_wise_summary}")

#day with highest revanue

highest_revanue={}

for d in tips_data:
    total_bill=float(d.get("total_bill"))
    day=d.get("day")

    if day in highest_revanue:
        highest_revanue[day]+=total_bill
    else:
        highest_revanue[day]=total_bill
#print only highest paid day        
max_revanue_day=max([[v,k] for k,v in highest_revanue.items()])
print("highest paid day=",max_revanue_day)    
 
#which gender has highest tip

hihest_tip={}

for g in tips_data:
    tipp=float(g.get("tip"))
    gen=g.get("sex")

    if gen in hihest_tip:
        hihest_tip[gen]+=tipp
    else:
        hihest_tip[gen]=tipp   

max_tip=max([[v,k] for k,v in hihest_tip.items()])
print("highest tip =",max_tip)





