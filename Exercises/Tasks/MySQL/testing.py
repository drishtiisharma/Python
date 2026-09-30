username = input("Enter username: ")

# 1. Query built using string concatenation
query1 = "SELECT * FROM users WHERE username = '" + username + "'"
print(query1)

# 2. Query using ? placeholder with bound parameter
query2 = "SELECT * FROM users WHERE username = ?"
print(query2)

# 3. Query using string formatting
query3 = f"SELECT * FROM users WHERE username = '{username}'"
print(query3)

# 4. Query built using allowed_columns

allowed_columns = ["username", "salary", "created_at"]
sort_column = input("Enter column to sort by: ")
if sort_column in allowed_columns:
    query = f"SELECT * FROM users ORDER BY {sort_column}"
    print(query)
else:
    print("Invalid column")

