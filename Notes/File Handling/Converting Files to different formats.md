# Converting Files to Different Formats

## What are the commonly used formats?
Before converting files to different formats, we need to know what are the most common file formats Python deals with:

1. `.txt` : plain text files with no fixed structure like rows & columns or key-value pairs
2. `.csv` : (Comma Separated Values); stores data in tabular format, similar to Excel Spreadsheet; row-> record ; column -> field; columns usually separated by commas.

**Difference between `.csv` & `.xlsx`:**

| .csv                                                                                  | .xlsx                                                                                                                          |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| plain text format with a series of values separated by commas.                        | binary file that holds information about all the worksheets in a file, including both content and formatting.                  |
| can be opened with any text editor generally.                                         | can be only read by applications that have been especially written to read their format, and can only be written the same way. |
| format for saving tabular information into a delimited text file with extension .csv. | is a spreadsheet that saves files into its own proprietary format viz. xls or xlsx.                                            |
| importing csv files can be much faster, and also consumes less memory.                | excel consumes more memory while importing data.                                                                               |
| used when we need to store/exchange simple tabular data without formatting.           | used when we need spreadsheets with formatting, formulas, charts, multiple sheets, etc.                                        |
3. `.json` :  (JavaScript Object Notation); stores data in key-value structure; commonly used for APIs, web applications and data exchange.

## When to Use What?
- **CSV** : use when we have a simple tabular data arranged in rows and columns, esp when we need to exchange data between different programs such as excel, databases, or python.
- **JSON** : use when we have structured data with key-value pairs, esp when the data can be nested or when communicating between applications through APIs.
- **TXT** : used when we need to store plain, unstructured text, such as notes, logs, messages, or simple textual information.

## Converting to different formats

1. CSV Conversions

```
# CSV -> JSON
import csv
import json

with open(r'files\file.csv', mode='r') as f:
    reader = csv.reader(f)
    data = list(reader)

with open(r'files\csv_file.json', mode = 'w') as f:
    json.dump(data,f,indent=4)

# CSV -> TXT

import csv
with open(r'files\file.csv', mode = 'r') as f:
    reader = csv.reader(f)

    with open(r'files\csv_file.txt', mode = 'w') as f:
        for x in reader:
            f.write(' '.join(x)+'\n')
```

2. JSON Conversions

```
# JSON -> CSV

import csv
import json

with open(r'files\file.json', "r") as f:
    data = json.load(f)

with open(r'files\json_file.csv', "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())

    writer.writeheader()
    writer.writerows(data)

# JSON -> TXT
import json
with open(r'files\file.json', mode = 'r') as f:
    reader = json.load(f)

    with open(r'files\json_file.txt', mode = 'w') as f:
        for x in reader:
            f.write(str(x)+'\n')
```

3. TXT Conversions

```
# TXT -> CSV
import csv

with open('files\file.txt', mode ='r') as f:
    with open('files\txt_file.csv', mode = 'w') as f1:
        writer = csv.writer(f1)

        for x in f:
            writer.writerows(x.strip().split(","))

# TXT -> JSON
import json

with open(r'files\file.txt', mode='r') as f:
    data = f.read()
    with open(r'files\txt_file.json', mode = 'w') as f1:
        json.dump(data,f1,indent=4)
```
