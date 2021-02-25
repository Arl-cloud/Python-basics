#User input
def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"
user_input = float(input("Enter temperature:")) #the input from user has to be a float (otherwise user input is always a str)

print(weather_condition(user_input)) 
#String formatting
user_i = input("Enter your name: ")
message = "Hello %s!" % user_i #%s - value of variable will go in %, works with python 2
print(message) #prints e.g. Hello Arleen!

message2 = f"Hello {user_i}" #f = prefix, works with python 3 or higher
print(message2)

#String formatting with multiple variables
name = input("Enter your name: ")
surname = input("Enter your surname: ")
when = "today"
message3 = "Hello %s %s. What's up %s"  % (name, surname, when) #2 varibles - 2 placeholders
print(message3)
message4 = f"Bye {name} {surname}"#2 brackets (with spaces inbetween)
print(message4)

def foo(name):
    return "Hi %s" % name
print(foo("Arle"))

def foo(name):
    return "Hi %s" % name.title() #returns name with capitalized 1st letter.
#important to call the function in line 2