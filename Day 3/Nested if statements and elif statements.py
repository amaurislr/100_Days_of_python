
#in this code you can see the explanation of how to use if, else and elif

height = int(input("what's your height ?"))


if height >= 120:
    print (" you can ride the rollercoaster")
    age = int(input("What is your age?"))

    if age >= 18:
        bill =12
        print("The ticket value is $12")
    elif age >=12:
        bill = 7
        print("You have to pay 7$")
    elif age >=45 and age <= 55:
        print ("Everything is going to be ok. Have a free ride on us!")
    else:
        print("You have to pay 5$")

    wanted_photo= input("Do you want to have photos take? Type y for yes and type n for")
    if wanted_photo == "y":
        bill +=3
        print(f"the total bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")



