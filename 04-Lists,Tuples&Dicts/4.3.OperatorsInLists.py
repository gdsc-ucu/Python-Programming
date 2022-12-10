#you can use the in and not in operators in lists for verification
my_list=['dog','cat','fish','monkey','giraffe']

print('lion' in my_list)
#will putput a boolean statement verifying if it is there or not

print('lion' not in my_list)
#will putput a boolean statement verifying if it is there or not

#this can also be used with if statements

my_list=['dog','cat','fish','monkey']
animal_list=str(input("Please enter your other animal's name:"))

if animal_list not in my_list:
    print("I do not have that animal")
else:
    print("Yes we do have that animal")
print("These are the animals you have:", my_list)

#Multiple assignment trick
#assign multiple variables with values in a list
student=['age','height','name','class']
#instead of assigning each varibale to a value
21=student[0]
'121cm'=student[1]
'Dondox Krout'=student[2]
'First year'=student[3]
print(student)
#to be revisted

21,'121cm','Dondox Krout','First Year'= student

#does the same thing
#however length of the variables must be equal to the length of the values

