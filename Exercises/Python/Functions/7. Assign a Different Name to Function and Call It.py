# Exercise 7. Assign a Different Name to Function and Call It
def display_student(name,age):
    return name,age

show_student = display_student # can rename functions like this
print(show_student("alice", 56))