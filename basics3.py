#Creating own functions
def mean(mylist): #parameters inside ()
    the_mean = sum(mylist) / len(mylist) #4 spaces indented
    return the_mean
mean([1, 4, 5]) #execute function, with input value - will produce mean of these 3 numbers
#function is only designed to process lists
print(type(mean), type(sum)) #mean is a function, sum a builtin fuction

#function that counts items in list
dir(list)
def lengther(lst):
    return(len(lst))
print(lengther([1, 4, 5, 6]))

#function that squares number
def foo(x):
    return(x*x)
print(foo(4))

#Conditionals, e.g. to define functions to apply to dicts
def mean(value): #parameters inside () 
    if type(value) == dict: #== is "equal to", if-loop, interpreter checks if type of the value is dict
        the_mean = sum(value.values()) / len(value) #if type of dict is true, this line will be executed
    else: #this line will be executed if type is not dict
        the_mean = sum(value) / len(value)
    
    return (the_mean) #is outside the if/else block! current value of mean is returned

monday_temperatures = [9.1, 8.8, 9.9] #when print is being executed, the list is stored as "value"
print(mean(monday_temperatures)) #calling the function mean

student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(student_grades))

if 3 < 1:
    print("Greater")
else:
    print("Not greater")

isinstance(3, int) #output is "True"

def foo(password):
     if len(password) < 8:
        return False
     else:
        return True
foo("ldfnlwef")

def foo(temperature):
    if temperature > 7:
        print ("Warm")
    else:
        print("Cold")
foo(10)

x = 3
y = 1
if x < y:
    print ("x is less than y")
elif x == y:
    print ("x is equal to y")
else:
    print("x is greater than y")


def fo(temperature):
    if temperature > 25:
        return "Hot"
    elif  15<= temperature <=25:
        return "Warm"
    else:
        return "Cold"
print(fo(15))
