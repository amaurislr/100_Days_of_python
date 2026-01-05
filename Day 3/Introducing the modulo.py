#Pause 2 - check Odd or Even

#Write some code using what you have learnt about the modulo operator and conditional
#cheks in Python to check if the number in he input area is odd or even. if it's odd
#print out the word "Odd" otherwise printout "Even".


num = int(input("Introduzca un numero: "))


if num % 2 == 0:
    print("This number is an odd")
else:
    print("This number is an Even")