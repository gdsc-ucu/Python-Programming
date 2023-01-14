#the most common type of flow control is the if statement
#the condition happens and if True, excutes the code in the main body if not, exits of the if function eg
#assume a program that has registered names:
print("Please enter your name(if you are not registered please do):")
name=input()
if name=="Ruth": #don;t forget the colon
    print("Hey Ruth, welcome")
#authenticates Ruth, any other name, the process will exit

#else statements
#Can be optionally following an if statement, if the condition is False, it is executed
if name=="Ruth":
    print("Hey Ruth , welcome")
else: #do not forget the colon:
    print("Name is not registered")

#elif statements
#for many possible clauses
#imagine Ruth, John, James, Stacy were in the system
if name=="Ruth":
    print("Hey Ruth, welcome")
elif name=="John":
    print("Hey John, welcome")
elif name=="James":
    print("Hey James, welcome")
elif name == "Stacy":
    print("Hey Stacy, welcome")
else: #do not forget the colon:
    print("Name is not registered")

#alternatively
if ((name=="Ruth") or (name=="John") or (name=="Mary"))
    print(f"Hey {name}, Welcome")

#another if statment
count=0
if count<5:
    print("Hello World")
    count=count+1

#if statment to check max of 3 numbers
#write a program that allows you to find the largest of three or more numbers
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
#comparing the first number
if num1>num2 and num1>num3:
     print(num1, "is greater than ",num2,"and",num3, "\n")
#checking for equality
elif num1==num2==num3:
        print(num1, "is equal to ",num2,"and",num3, "\n")
#comparing the second number
elif num2>num1 and num2>num3:
     print(num2, "is greater than ",num1,"and",num3, "\n")
#comparing the third number
else:
    print(num3, "is greater than ",num1,"and",num2, "\n")
