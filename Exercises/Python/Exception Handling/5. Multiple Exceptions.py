# Exercise 5: Multiple Exceptions
# Problem Statement: Write a function parse_and_divide(value, divisor) that converts value to a float and then divides it by divisor. Use a single try block that handles ValueError (bad conversion) and ZeroDivisionError (division by zero) with separate messages for each.

def parse_and_divide(value,divisor):
    
    try:
        value = float(value)
        value = value/divisor
        return value
    except ValueError:
        return "bad conversion"
    except ZeroDivisionError:
        return "can't be divided by 0"

print(parse_and_divide(10,2))
print(parse_and_divide(10,0))
print(parse_and_divide("hello",2))