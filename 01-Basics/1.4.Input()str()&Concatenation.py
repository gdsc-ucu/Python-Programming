#input() function waits for the user to type text on the keyboard and press enter
#variable_name=input()
#print(variable_name) will output what the person typed in the program

name1=input()
print(name)

#we usually want to prompt the user with a message hence useful that you ask what they should input
name2=input("Please enter your name:")
print(name2)

#the input() accepts only strings, hence to input and print numbers, concatenation is applied
#CONCATENATION
first_name="Bob"
last_name="Smith"

print(first_name+last_name) # output BobSmith
print(first_name+" "+last_name) #output Bob Smith

age=21
print(first_name+age) #will output a type error so we concantenate

print(first_name+str(age)) #output Bob21
print("Hey my name is "+first_name+" and I am "+age+" years old.") #output: Hey my name is Bob and I am 21 years old.

#the len() function: evaluates to the interger value of the number of characters in that string
print("Hey "+first_name)
print(len(first_name)) #output 3

#you can concatenate to anything using str(), int() and float()
variable_1=str(29)
variable_2=int('-99')
variable_3=float(10)
print(variable_1+","+variable_2+","+variable_3)



























































