# open file / read file

myfile = open("fruits.txt") #open-function creates file object in temporary memory (RAM), file here is in the same repository as this python file
#print(myfile.read()) #read-method

#File Cursor
#print(myfile.read()) #empty string, bc cursor is at last word, there is nothing to read after that

#Save content in a variable
#content = myfile.read() #read method is only executed once
#print(content)
#print(content) #cursor starts at beginning of file

#Closing a file / delete file from memory
#myfile.close()
#myfile.read() #after close, would return as an error

#better way:
with open("fruits.txt", "r") as myfile:
    content = myfile.read() #block, indented under the open line

print(content)
#print(content [:10]) #prints out 10 first characters of this file

#if fruit.txt is in another folder: specify path
# with open("files/fruits.txt") as myfile:

#creating/writing text into a file
with open("/Users/arleenlindenmeyer/Desktop/Python/vegetables.txt", "w") as myfile_v:
    myfile_v.write ("tomato\ncucumber\nzucchini") #\n creates new line

#if you write into an existing file, the original code will be overwritten!

#defines function that gets a single string character and a filepath and returns the number of occurences of that character in the file
def foo(character, filepath = "/Users/arleenlindenmeyer/Desktop/Python/fruits.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)

print(foo("a"))

#Appending text to an existing file
with open ("/Users/arleenlindenmeyer/Desktop/Python/vegetables.txt", "a") as myfile2: #a will append instead of overwrite
    myfile2.write("\nonion")

#Append and read at the same time 
with open ("/Users/arleenlindenmeyer/Desktop/Python/vegetables.txt", "a+") as myfile3: 
    myfile3.write("\ngarlic")
    myfile3.seek(0) #makes the cursor go to the top of the list
    conte = myfile3.read()

print (conte)