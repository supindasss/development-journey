keep_going=True
while True:
     
     distance=int(input("Enter the total distance trvelled"))
     Total_fare=50+(15*distance)
     print("Your total fare will be",Total_fare)
     keep_going=input("Stop...?")
     if keep_going.lower()=="yes":
          keep_going=False
          break
     else:
          "SEE YOU"

          

