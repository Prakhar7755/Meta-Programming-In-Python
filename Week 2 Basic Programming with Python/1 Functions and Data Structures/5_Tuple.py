my_tuple = (1, "stringVal", 5.4, True)

print(my_tuple[1])

print(type(my_tuple))  # <class 'tuple'>

# it counts the no. of occurrences of the specific var
print(my_tuple.count("stringVal"))

""" 
You have declared the following tuple my_tuple = (1, 2, "hello"). This tuple contains two items of type integer and a third item of type string. Can you create tuples that have items with different data types?

Yes

Correct
Correct! A tuple can accept any mix of data types. 
"""

print(my_tuple.index(5.4))  # tell index of 5.4 which is 2

for x in my_tuple:
    print("Tuple value", x)


""" 
Tuple value 1
Tuple value stringVal
Tuple value 5.4
Tuple value True 
"""

