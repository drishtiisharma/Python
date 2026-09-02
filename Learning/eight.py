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
import os
os.rmdir("foldername")
