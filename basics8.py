#Functions with multiple Argument
def area(a, b): #parameter = a & b
    return a * b

print(area(4, 5)) #4 & 5 are non-keyword (also called positional) arguments: they dont have a keywork attached to them. Position is important!
print(area(a=3, b=2)) #works the same, but these are keyword arguments. Position does not matter

def subs(c, d=3): #d is a default parameter: when nothing is entered for d, d will be 3
#Watch out: default argument has to be the last / default before non-default not possible
    return c - d
print(subs(4, 5))
print(subs(c=4))

#dir(str)

#Concatenating/Adding two strings
def foo(x, y):
    return x + y

print(foo("bl", "ah"))

#Functions with an Arbitrary number of Non-keyword arguments
len("hello") #function only takes one argument
isinstance(6, int) #takes 2 arguments

def mean(*args): #Function takes as many arguments as we want - args is a tupil
    return sum(args) / len(args)

print(mean(4, 6, 1))

#Define function that turns strings uppercase and sorts them alphabetically
def fun(*args2):
    args2 =[i.upper() for  i in args2]
    return sorted(args2)
 
print(fun("ice", "baby", "amazing"))

#Functions with arbitrary number of keyword arguments
def kwdict(**kwargs):
    return kwargs

print(kwdict(a=1, b=4, c=5)) #function returns a DICT

#Sums up values of keywords
def find_sum(**kwargs2):
    return sum(kwargs2.values())
    
print(find_sum(a=3, b=4, c=2))