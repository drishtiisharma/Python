rows = int(input("rows: "))
cols = int(input("cols: "))

# for x in range(rows):
#     for y in range(cols):
#         print("*",end='')
#     print()

for x in range(1,rows+1):
    
    for y in range(x):
        print("*",end='')
    
    print()