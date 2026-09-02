# # file handling
# f = open('geek.txt','r')
# print(f)
# f.close()
# print("file closed")

# # checking properties
# f = open('geek.txt','r')
# print("filename: ",f.name)
# print("mode: ",f.mode)
# print("is closed?", f.closed)
# f.close()
# print("is closed?",f.closed)

# # reading file content
# f = open('geek.txt','r')
# content = f.read()
# print(content)

## writing to a file

# f = open("geek.txt",'w')
# f.write(
#     """
#     a
#     b
#     c
#     d
#     """
# )
# f.close()
# f = open("geeks.txt",'r')
# content = f.read()
# print(content)


## or

# with open("geeks.txt",'w') as f:
#     f.write("""
#     hello
#     world
#     """)

# print(open('geeks.txt','r').read())

## creating a file
# with open("geeks.txt",'a') as f:
#     f.write("Added more content")
# with open("geeks.txt",'r') as f:
#     print(f.read())

## deleting a file
# import os
# os.remove("new.txt")

## checking if a file exists before deleting
# import os
# if os.path.exists("new.txt"):
#     os.remove("new.txt")
# else:
#     print("file does not exist!")

## deleting a folder
# import os
# os.rmdir("foldername")

# ------------------------------------- #
# # CSV -> JSON
# import csv
# import json

# with open(r'files\file.csv', mode='r') as f:
#     reader = csv.reader(f)
#     data = list(reader)

# with open(r'files\csv_file.json', mode = 'w') as f:
#     json.dump(data,f,indent=4)

# # CSV -> TXT

# import csv
# with open(r'files\file.csv', mode = 'r') as f:
#     reader = csv.reader(f)

#     with open(r'files\csv_file.txt', mode = 'w') as f:
#         for x in reader:
#             f.write(' '.join(x)+'\n')

# ------------------------------------- #

# # JSON -> CSV

# import csv
# import json

# with open(r'files\file.json', "r") as f:
#     data = json.load(f)

# with open(r'files\json_file.csv', "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=data[0].keys())

#     writer.writeheader()
#     writer.writerows(data)

# # JSON -> TXT
# import json
# with open(r'files\file.json', mode = 'r') as f:
#     reader = json.load(f)

#     with open(r'files\json_file.txt', mode = 'w') as f:
#         for x in reader:
#             f.write(str(x)+'\n')

# ------------------------------------- #

# # TXT -> CSV
# import csv

# with open('files\file.txt', mode ='r') as f:
#     with open('files\txt_file.csv', mode = 'w') as f1:
#         writer = csv.writer(f1)

#         for x in f:
#             writer.writerows(line.strip().split(","))

# TXT -> JSON
import json

with open(r'files\file.txt', mode='r') as f:
    data = f.read()
    with open(r'files\txt_file.json', mode = 'w') as f1:
        json.dump(data,f1,indent=4)