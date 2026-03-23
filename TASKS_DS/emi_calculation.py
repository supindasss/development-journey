""" EMI CALCULATION """
p=int(input("Enter principal Loan amount"))
r=float(input("Enetr monthly interest rate "))
n=float(input("Enter Loan Tenure"))

EMI=(p*r*(1+r)**n)/(((1+r)**n)-1)

print("You total EMI Will be",EMI)