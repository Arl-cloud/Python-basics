#Simple List Comprehension
temps = [221, 234, 340, 230] #to save space, some data is saved without a decimal

new_temps = []
for temp in temps:
    new_temps.append(temp / 10) #the calculated numbers are stored in the new list new_temps

print(new_temps)

#better way to do it:
new_temps2 = [temp2 / 10 for temp2 in temps]

print(new_temps2)

#Missing Values / List Comprehension with if conditio
temps2 = [221, 234, -999, 230] #missing data is stored as e.g. -999

new_temps3 = [temp3 / 10 for temp3 in temps2 if temp3 != -999] #this way, the function will not try to devide the missing number

print(new_temps3)

#Function that only returns integers
def foo(numbers):
    return [i for i in numbers if isinstance (i, int)]
        
print(foo([99, "no data", 3, "no data", 5]))

#Function that only returns positive numbers
def foo2(numbers2):
    return [j for j in numbers2 if j > 0]

print(foo2([99, -2, 3, -5]))

#Replace missing data entry (e.g. -999 for 0)
#if + else: for loops goes at the very end
new_temps4 = [temp4 / 10 if temp4 != -999 else 0 for temp4 in temps2 ] #loop has to be AFTER the conditional

print(new_temps4)

#Strings are turned to 0s
def fun(numbers2):
    return [l if isinstance (l, int) else 0 for l in numbers2]

print(fun([99, "no data", 3, "no data", 5]))

#dir(list)

#Function that returns sum of a list (and turns strings into floats)
def lit(potato):
    return sum ([float(z) for z in potato])

print(lit(["1.2", "3.4"]))