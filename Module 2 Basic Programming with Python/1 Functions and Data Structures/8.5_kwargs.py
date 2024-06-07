def sum_of(**kwargs):
    sum = 0
    for key, value in kwargs.items():
        sum += value
    return round(sum, 2)


print(sum_of(coffee=2.99, cake=4.55, juice=2.99))  # 10.53
""" 
The advantage of using args and kwargs is that you can pass in which of the following? Select all that apply.  

Non-keyword variables
Correct! You can use kwargs to pass in non-keyword variables.

Keyword arguments
Correct! You can use kwargs to pass keyword arguments.

"""
