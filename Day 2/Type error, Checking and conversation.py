#These errors when you are using the wrong data type. e.g
#len(12345)

#because you can only give the len() function Strings, it will refuse to work and give you a TypeError if you give
#if you give it a number (integer)

len("hello world")

#Pause 2  Write out 4 type checks to print all 4 data types checks to print all 4 data types

#Using the type () and print () functions to print out 4 lines into the output area so we get the full collection of
#types that we learn about. <Class 'str'> <class 'int'> <class 'float'> and <class 'bool'>

print(type(1234))
print(type(1.234))
print(type("Hello world"))
print(type(True))

#pause 3
name = input("Enter your name: ")
name_l = len(name)


print("Number of letters in your name: " + str(name_l))
