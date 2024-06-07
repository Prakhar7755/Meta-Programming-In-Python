# def sum_of(a,b):
#   return a+b;
def sum_of(*args):
    sum = 0
    for value in args:
        sum += value
    return sum


print(sum_of(4, 5, 6))
print(sum_of(4, 5, 6, 5, 6, 9, 10))

""" 
The advantage of using args and kwargs is that you can pass in which of the following? Select all that apply.  

Non-keyword variables
Correct! You can use kwargs to pass in non-keyword variables.

Keyword arguments
Correct! You can use kwargs to pass keyword arguments.

"""
