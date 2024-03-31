#Kenneth Smith 3/31/2024 3.2
#This project is intended to calculate how long it will take a invest to double at a given interest rate

#Create the variables
annual_interest_rate = float(input("Enter current annual interest rate: "))
investment_amount = float(input("Enter investment amount: "))

#variables to be used in the while loop
account_balance = investment_amount
years = 0

#while loop using interest formula
#interest rate must be entered as a decimal with this formula
while account_balance < investment_amount * 2:
    account_balance += account_balance * annual_interest_rate 
    years += 1

print(f"${investment_amount} will take {years} years to double")
