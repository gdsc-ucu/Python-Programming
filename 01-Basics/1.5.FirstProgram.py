#This program will ask for all your names, age, height and display them
print("Enter your first name:")
first_name=str(input())
#alternatively
#first_name=str(input("Please enter your first name:"))

print("Enter your second name:")
second_name=str(input())
#alternatively
#second_name=str(input("Please enter your second name:")

print("Very nice to meet you "+first_name+" "+second_name)
#alternatively
#print(f"Very nice to meet you {first_name} {second_name}")

#len() is an int hence concatenation is needed
print("As a a funfact, the length of your name is "+str(len(first_name+second_name)))

print("Before you go, How old are you?")
age=int(input())
print("Wow"+first_name+" You are "+str(age)+"years old!")
#how old they will be in 10 years
print("Oh and by the way, you will be "+str(age+10)+" in 10 years")