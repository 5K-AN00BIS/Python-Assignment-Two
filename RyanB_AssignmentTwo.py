# Ryan Bachman
# University of Advancing Technology
# CSC235, Python 1, Fall 2020, Online 2
# I/O with Python Assignment (Week One)

# Start Program
# Begin print statements
print() # Skips a line
# Print out the header.
print("'''---___---''' Ryan's Ultra Awesome First Python Program Tutorial '''---___---'''")
print() # Skips a line
# Collect user data and store as a variable.
name = input("What is your name?: ") # Collect and store user name. STRING INPUT
age = input("How old are you?: ") # Collect and store age. NUM INPUT
pi = input("What are the first 3 digits of pi?: ") # Collect and store pi digits (3.14). FLOAT INPUT
firstTime = input("Is this your first time programming? (Yes or No): ") # Collect and store whether it's their first time programming. BOOL INPUT
print() # Skips a line
# Print out a greeting with the above inputs. OUTPUT
print("Hello " + name + " who is " + age + " years old. It's nice to meet you!")
print() # Skips a line
# Print out instructions for printing in Python.
print("In today's lesson, we will talk about how to print a line in Python.")
print("In order to print a new line, type the following:")
print("print('This is an example.')")
print("Believe it or not, that's it!")
print("Now you try typing it: ")
printVal = input() # Ask for user input and store in printVal variable. INPUT
print("You entered: " + printVal) # Prints out what the user entered. OUTPUT
print("Does this look the same as what we entered before? If not, please note what was incorrect!")
# Print out separation line.
print("--------------------------------------------------------------------------")
# Print out instructions for commenting in Python
print("Now let's talk about commenting your code.")
print("In order to comment a section, just add a #. Simple as that!")
print("For example:")
print("# print('This is an example.')")
print("The line above will not print anything to PowerShell, it's simply a way to comment your code!")
print("Now you try typing it: ")
printVal2 = input() # Ask for user input and store in printVal2 variable. INPUT
print("You entered: " + printVal) # Prints out what the user entered. OUTPUT
print("Does this look the same as what we entered before? If not, please note what was incorrect!")
# Print out separation line.
print("--------------------------------------------------------------------------")
print("This concludes my first tutorial and thus ends the assignment. Whew!")
print() # Skips a line
print("Please see a set of your entries below:")
data = {name, age, pi, firstTime, printVal, printVal2} # Place all input data into a Set data structure.
print(data) # Print the set for the user to view.
# End Program
