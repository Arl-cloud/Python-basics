#For loops: How and Why
monday_temperatures = [9.1, 8.8, 7.6]

print(round(monday_temperatures[0])) #print rounded number with index 0

#in 1st iteration, variable temp = 9.1, in the 2nd iteration 8.8
for temp in monday_temperatures:
    print(round(temp)) #executed command for all items in an array
    print("Done")

for letter in "hello":
    print(letter.title()) #array can also be a string

#For loop (with if condition) that prints out only numbers in colors over 50
colors = [11, 34, 98, 43, 45, 54, 54]
for foo in colors:
    if foo > 50:
        print(foo)

#prints out only if number in colors is type integer
for boo in colors:
    if isinstance(boo, int): #use isinstance to check for type
        print(boo)

#Loops for dictionaries
student_grades = {"Marry": 9.9, "Sim": 6.5, "John": 7.4}
for grades in student_grades.items(): #iterates over ITEMS (= key + value)
    print(grades) #keys(names) and values are printed out in a tupel

for grades2 in student_grades.keys(): #iterates over keys
    print(grades2)

for grades3 in student_grades.values(): #iterates over values
    print(grades3)

#Combining dictionary loop and string formatting
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for key, value in phone_numbers.items():
    print("{}: {}".format(key, value))

#replace "+" with "00" in phone numbers
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for value in phone_numbers.values():
    print(value.replace("+", "00"))

#a for loop runs until a container is exhausted
for i in [1, 2, 3]:
    print(i)

#a while loop runs as long as its condition is TRUE
a = 3
#while a > 0:       will run endlessly, as this condition is always true
#    print(1)

#execution of this loop ends when user types in "pypy" as username
username = "" #variable username is an empty string

while username != "pypy": #!= means is different than
#in the first iteration, variable username is an empty string-thus different than "pypy" and one gets the print
#in the second iteration, the variable username is what is entered by user
    username = input("Enter username: ")

#while loops with break and continue

while True: #is always true
    name = input("Enter name: ")
    if name == "pypy": #if variable name is "pypy"
        break #stops loop
    else:
        continue