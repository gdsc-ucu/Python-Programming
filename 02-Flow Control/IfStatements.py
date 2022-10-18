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
    print("Hey Ruth, welcome")
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
if ((name=="Ruth")or (name=="John")or (name=="Mary"))
    print(f"Hey {name}, Welcome")