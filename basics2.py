#Lists
dir(list) #what to do with lists
monday_temperatures = [9.1, 8.8, 7.5]
help(list.append)
monday_temperatures.append(8.1) #add value to list
monday_temperatures.clear #clears all items from list
monday_temperatures.index(8.8) #the index of this list item (list starts counting values at 0, 1 , 2, ..)
#starts search by default from 1st item
monday_temperatures.index(8.8, 2)#starts search from third item/value
monday_temperatures.remove(7.5) #removes only this item
monday_temperatures[1] #gives item with index nr. 1 (2ns item)
#Slices
monday_temperatures[1:4] #gives second to forth item "slice", item with index 4 is not included
monday_temperatures[:2] #gives item with index 0 + 1
monday_temperatures[2:] #gives item with index 2 and end of list

monday_temperatures[-1] #gives last item of list
monday_temperatures[-2] #gives second last item
monday_temperatures[-2:] #gives second last item and end of list
print(monday_temperatures)

#accessing characters and slices in strings
mystring = "hello"
mystring[1] #gives letter e
mystring[-1] #gives letter o
mystring[:3] #gives "hel"

m_t = ["hello", 1, 2, 3]
m_t[0] #gives "hello"
m_t[0][2] #gives letter "l" (with index 2)

#accessing items in dictionaries - instead of indexes, dicts have keys
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
student_grades["Sim"] #gives Sims value

eng_french = { "horse": "cheval", "sister": "soeur"}
eng_french["horse"]