#function is a mini program
#to further update
#def statememt defines the function in this case names "hello"
def hello():
    #body of the function
    print("Hello There")
    print("My name is Jasper")
    print("Your trainer for this session")
#calling the function
hello()
#calling the function again
hello()

#function with parameters
def hello(name):
    print(f"Hello {name}, how are you doing today.")
    print(f"{name} is such a nice name")

hello("James") #will print the body of the text with the name filled with the provided name
hello("Moses")

#absence of a value is denoted by None
#functions like print have a return value of None

#Return Values
#usually used with if inclusive

import random

def get_answer(answer_number):
    if answer_number==1:
        return "You have the firstone"
    if answer_number==2:
        return "You have the secondone"
    if answer_number==3:
        return "You have the thirdone"
    if answer_number==4:
        return "You have the fourthone"
    if answer_number==5:
        return "You have the fifthone"

number=random.randint(1,5)
print(number)
gotten=get_answer(number)
print(gotten)
#alternatively
print(get_answer(random.randint(1,5)))
