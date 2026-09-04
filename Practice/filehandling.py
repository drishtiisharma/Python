## CSV TO JSON
# import csv 
# import json 
# with open(r'files\file.csv',mode='r') as f:
#     reader = csv.reader(f)
#     data = list(reader)
# with open(r'files\conversions\csv_file.json',mode='w') as f:
#     json.dump(data,f,indent=4)


## CSV TO TXT
# import csv
# with open(r'files\file.csv',mode='r') as f:
#     reader = csv.reader(f)
    
#     with open(r'files\conversions\csv_file.txt',mode='w') as f1:
#         for x in reader:
#             f1.write(' '.join(x)+'\n')

## JSON TO CSV
# import json 
# import csv
# with open(r'files\file.json',mode='r') as f:
#     data = json.load(f)

# with open(r'files\conversions\json_file.csv',mode='w') as f:
#     writer = csv.DictWriter(f,fieldnames=data[0].keys())
#     writer.writeheader()
#     writer.writerows(data)

## JSON TO TXT
# import json

# with open(r'files\file.json',mode='r') as f:
#     data = json.load(f)

#     with open(r'files\conversions\json_file.txt',mode='w') as f1:
#         for x in data:
#             f1.write(str(x)+'\n')

## TXT TO CSV
# import csv 

# with open(r'files\file.txt',mode='r') as f:
#     with open(r'files\conversions\txt_file.csv',mode='w',newline ='') as f1:
#         writer = csv.writer(f1)

#         for x in f:
#             writer.writerow(x.strip().split(','))

## TXT TO JSON
# import json 

# with open(r'files\file.txt',mode='r') as f:
#     data = f.read()
#     with open(r'files\conversions\txt_file.json',mode='w') as f1:
#         json.dump(data,f1,indent=4)


# import json 

# with open(r'files\file.txt',mode='r') as f:
#     lines = f.readlines()

# headers = lines[0].split()
# data = []

# for line in lines[1:]:
#     values = line.split()
#     data.append(dict(zip(headers,values)))

# with open(r'files\conversions\txt_file.json',mode='w') as f1:
#         json.dump(data,f1,indent=4)



