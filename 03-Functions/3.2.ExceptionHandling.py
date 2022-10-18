#enabling the program to detect errors, handle them and continue to run
#program to see how many numbers can divide 2022
def division(divisor):
    return 2022/divisor

print(division(2))
print(division(12))
print(division(-29))
#when divided by zero an error will appear
#print(division(0))

#using exception handling
def division(divisor):
    try:
        return 2022/divisor
    except ZeroDivisionError:
        print("ERROR, cannot divide by zero")

print(division(2))
print(division(12))
print(division(-29))
print(division(0))

#Project
import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()