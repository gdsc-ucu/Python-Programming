#function is a mini program
#def statememt defines the function in this case names hello
def hello():
    #body of the function
    print("Hello There")
    print("My name is Jasper")
    print("Your trainer for this session")
#calling the function
hello()

#function with parameters
def hello(name):
    print(f"Hello {name}, how are you doing today.")
    print(f"{name} is such a nice name")

hello("James") #will print the body of the text with the name filled with the provided name
hello("Moses")
