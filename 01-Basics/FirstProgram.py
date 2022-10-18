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

print("As a a funfact, the length of your name is "+len(first_name+second_name))