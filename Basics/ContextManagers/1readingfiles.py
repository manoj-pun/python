################Reading txt file
# file_path = "/Users/manojpun/Desktop/python_related/python/Basics/ContextManagers/textfile.txt"

# with open(file_path,"r") as file:
#     content = file.read()
#     print(content)

# or you could do
# with open("/Users/manojpun/Desktop/python_related/python/Basics/ContextManagers/textfile.txt","r") as file:
#     content = file.read()
#     print(content)

#what if the file don't exist,we could use try except
# file_path = "/Users/manojpun/Desktop/python_related/python/Basics/ContextManagers/textfile"

# try:
#     with open(file_path,"r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("That file is not found")





##################Reading json file and while reading json file you must import json
import json

file_path = "/Users/manojpun/Desktop/python_related/python/Basics/ContextManagers/jsonfile.json"

# try:
#     with open(file_path,"r") as file:
#         content = file.read() #in json when you do this,the texts are read as string it works though but cannot be access the values,so json must be read as load
#         print(content)
# except FileNotFoundError:
#     print("That file is not found")

##with json load
# try:
#     with open(file_path,"r") as file:
#         content = json.load(file) #now it returns as dictionary
#         print(content)
# except FileNotFoundError:
#     print("That file is not found")

#########To print the specific values
# file_path = "/Users/manojpun/Desktop/python_related/python/Basics/ContextManagers/jsonfile.json"

# try:
#     with open(file_path,"r") as file:
#         content = json.load(file)
#         print(content["name"])
# except FileNotFoundError:
#     print("That file is not found")






#############Reading csv files and csv must be imported to read csv files
import csv 
# file_path = "/Users/manojpun/Desktop/python_related/python/Basics/ContextManagers/csvfile.csv"

# try:
#     with open(file_path,"r") as file:
#         content = csv.reader(file) #it gives the memory address
#         print(content)
# except FileNotFoundError:
#     print("That file is not found")

########with csv file you need to read the csv file line by line
# file_path = "/Users/manojpun/Desktop/python_related/python/Basics/ContextManagers/csvfile.csv"

# try:
#     with open(file_path,"r") as file:
#         content = csv.reader(file)
#         for line in content:
#             print(line)
# except FileNotFoundError:
#     print("That file is not found")

##########to get the specified colums we can give index
file_path = "/Users/manojpun/Desktop/python_related/python/Basics/ContextManagers/csvfile.csv"

try:
    with open(file_path,"r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[1])
except FileNotFoundError:
    print("That file is not found")