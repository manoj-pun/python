text_data = "My name is Manoj Pun"

# file_path = "writingtextfile.txt"

# with open(file_path,"w") as file: #note:file_path is file and second argument is mode and also w will overwrite the file
#     file.write(text_data)
#     print("File was created.")


########mode x
# file_path = "writingtextfile.txt"
# try:
#     with open(file_path,"x") as file: 
#         file.write("\n" + text_data)
#         print("File was created.")
# except FileExistsError:
#     print("That file exists")

#######mode a
# file_path = "writingtextfile.txt"
# try:
#     with open(file_path,"a") as file: 
#         file.write("\n" + text_data)
#         print("File was created.")
# except FileExistsError:
#     print("That file exists")


########working with list
# employees = ["Manoj","David","Ram"]
# file_path = "writingtextfile.txt"
# try:
#     with open(file_path,"w") as file: 
#         for employee in employees:
#             file.write(employee + " ")
#         print("File was created.")
# except FileExistsError:
#     print("That file exists")




########JSON
# import json

# employee = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }

# file_path = "writingjsonfile.json"
# try:
#     with open(file_path,"w") as file: 
#         json.dump(employee,file)
#         # json.dump(employee,file,indent=4)
#         print("Json File was created.")
# except FileExistsError:
#     print("That file exists")



#######working with csv
# import csv

# employees = [
#     ["Name","Age","Location"],
#     ["Alice", 30, "New York"],
#     ["Bob", 25, "London"],
#     ["Charlie", 35, "Tokyo"]
# ]

# file_path = "writingcsvfile.csv"
# try:
#     with open(file_path,"w") as file: 
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print("CSV File was created.")
# except FileExistsError:
#     print("That file exists")





####some modes
# 'r'  - Read (default)
# 'w'  - Write (creates/truncates)
# 'a'  - Append (creates/append)
# 'x'  - Exclusive create (fails if exists)
# 'r+' - Read + Write (no truncate)
# 'w+' - Write + Read (truncates)
# 'a+' - Append + Read (append mode)
# 'x+' - Exclusive + Read/Write
# 'rb' - Read binary
# 'wb' - Write binary
# 'ab' - Append binary
# 'rb+'- Read/Write binary
# 'wb+'- Write/Read binary
# 'ab+'- Append/Read binary
# 'xb' - Exclusive binary
# 'xb+'- Exclusive binary + Read/Write