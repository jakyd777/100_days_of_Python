#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")

bill_price = input("What was the total bill? ")
tip_perc = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_people = input("How many people to split the bill? ")

tip_var = "1." + tip_perc

tip_var = float(tip_var)
bill_price = float(bill_price)
num_people = int(num_people)

pay_per_person = bill_price / num_people * tip_var

print(f"Each person should pay: %.2f $." % round(pay_per_person, 2))