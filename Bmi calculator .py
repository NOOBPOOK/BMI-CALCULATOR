print("Hello friends,this is working BMI calcultor")
n = input("Enter your name here....")
w = int(input("Enter your weight in kg's here..."))
h = float(input("Enter your height in metres here..."))
bmi = w / (h ** 2)
print("Calulating your bmi!!")

if bmi < 18.5:
    print(str(bmi) + " You are certainly under underweight!!")
    print("Don't you eat anything else?")
    ans = input("True or False.....")
    if ans == "True":
        print("Then what are you doing here, go and eat something!!")
    elif ans == "False":
        print("You should eat healthy")

elif bmi >= 18.5 and bmi < 25:
    print(str(bmi) + " You have pretty in decent fitness")

elif bmi >= 25 and bmi < 30:
    print(str(bmi) + " You are slightly overweight!!")

elif bmi >= 30:
    print(str(bmi) + " You are overweight!!")

print("Your final bmi is counted as ..." + str(bmi))
