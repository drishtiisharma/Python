# Exercise 8: Re-raising Exceptions
# Problem Statement: Write a function process_data(value) that converts a string to an integer. Catch any ValueError, log a message to the console, and then re-raise the same exception so the calling code can handle it at a higher level.
def process_data(value):
    try:
        return int(value)
    except ValueError as e:
        print(f"[Log] process_data failed: {e}")
        raise

try:
    process_data("abc")
except ValueError as e:
    print(f"[main] Caught re-raised exception: {e}")

