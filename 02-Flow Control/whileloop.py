#Want a block to execute over and over, a while statement can do that for you
#the code will execute as long as the condition is True eg
count=0
#condition
while count<5: #don't forget the :
    print("Hey my people")
    count+=1 #increment statement
             #BE CAREFUL: # +=1 is different from =+
    #alternatively
    #count=count+1

#an annoying loop that asks you to enter "your name"
name=""
while name!="your name":
    print("Please enter 'your name'")
    name=input()
    #alternatively name=str(input("Please enter 'your name'":)
print("Thank you so much")

#using break and or an if statement
while True:
    name=str(input("Please enter 'your name':"))
    if name=="your name":
        break
print("Thank you so much")
