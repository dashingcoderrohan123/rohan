#Write a program to calculate the BMI of a person?

t=float(input("enter the height in cm"))
print(t)

r=float(input("enter the weight in kg"))
print(r)

bmi=r/(t)**2  #weight/(height)**2

print(bmi)

if bmi <18.4:
    print("Unhealthy")

elif bmi<=24.5:
    print("Healthy")

elif bmi<=29.9:
    print("overweight")

elif bmi<=34.9:
    print("too much over weight")

elif bmi<=39.9:
    print("obese")

else:
    print("you are very unhealthy")                