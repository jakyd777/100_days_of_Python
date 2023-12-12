height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#Write your code below this line 
height_float = float(height)
weight_float = float(weight)
bmi = weight_float/height_float**2

bmi_int = round(bmi)
if bmi < 18.5:
  print(f"Your BMI is {bmi_int}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi_int}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi_int}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi_int}, you are obese.")
else:
  print(f"Your BMI is {bmi_int}, you are clinically obese.")