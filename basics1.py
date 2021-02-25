import datetime
mynow = datetime.datetime.now()
print(mynow)

mynumber = 10
mytext = "Hello"
print (mynumber, mytext)
x = 10
y = "10"
z = 10.1
sum1 = x + x
sum2 = y + y
print(sum1, sum2)
print(type(x), type (y), type (z))

student_grade ={0.1, 0.8, 7.5} #geschwungene brackets=liste
print(list(range(1,10))) #kreiert Liste von ganzen Zahlen 1-9
print(list(range(1,10,2))) #kreiert Liste 1-9, aber nur von jeder 2. Zahl

dir(list) #shows you all the things you can do with a list
dir(float)#shows you all the things you can do with a float
dir(str)
help(str.upper) #shows what this specific function does
"hello".upper() #also possible with
name = "hello"
print(name.upper())

student_grades = [0.1, 8.8, 7.5]
#sum is a function, does not use a . notation to use it
dir(__builtins__) #complete list of builtin functions
mysum = sum(student_grades) #do not use sum as variable name!
length = len(student_grades)
mean = mysum/length
print(mean)
#calculate maximum with max
max_student = max(student_grades)
print(max_student)
print(student_grades.count(10.0)) #counts how many student got the grade 10

student_g = {"Mary": 9.1, "Sim": 8.8, "John": 7.5} #items in a dictionary are made of keys and itemy
#caluclate mean
dir(dict) #dictionary have vaules
student_g.values()
mysum = sum(student_g.values()) 
length = len(student_g)
mean = mysum/length
print(mean)
student_g.keys() #calls student names

monday_temperatures = (1, 4, 5) #tupel, are immutable
print(monday_temperatures)
tuesday_temperatures = [1, 4, 5] #lists are mutable, changable
tuesday_temperatures.append(6) #6 is added to list
tuesday_temperatures.remove(4) #4 is removed from list
print(tuesday_temperatures)
