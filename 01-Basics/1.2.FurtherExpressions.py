#Further Expressions
#All the math operators in python

#The exponent operator (**)
print(4**2) #raises 4 to the power of 2 =16

#The modulus operator (%)
print(10%3) #returns the remainder of the division of 10 and 3 =1

#The Integer division Operator (//)
print(13//4) #returns the rounded down division output =3

#Order of Operations-Precedence
#In order pf precedence:
# **,*,/,//,% to overide this, parenthesis() can be used

print(2+3*6) #=20
print((2+3)*6) #=30

#evaluate the equation
print((5-1)*((7+1)/(3-1))) #=16.0

print(5-1*7+1/3-1) #=-2.666666666666667


# name="Gordon Kasagga"

# for i in range(20):
#     print(i+1,":",name)
    

def repeat(number):
    #number=int(input("How many times should this repeat:"))
    name=input("Please enter your name:")
    for i in range(number):
        print(i+1,":",name)

number=int(input("How many times should this repeat:"))
repeat(number)
  
def addition(int(number1),int(number2)):
    add=number1+number2
    return add

number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
addition(number1,number2)   


