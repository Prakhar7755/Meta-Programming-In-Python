"""
A company wants to determine the general age of its customers. You help them by writing 
a program that uses a customer's ID number (7512171283423) to determine his or her age. But 
the data set that you are provided with has the ID numbers saved as strings. What 
typecasting function can you use to solve the problem?

int('7512171283423')


Correct
You are correct! You will use the integer function as it will output whole numbers with no 
decimal places.
"""

a = 55
b = 10.3
c = '533'

# EXPLICT CONVERSION
d = float(a)
e = str(b)
f = int(c)


print(type(d))  # <class 'float'>
print(type(e))  # <class 'str'>
print(type(f))  # <class 'int'>


# ord() , hex() , oct(), tuple(), set(), dict()

print(int(5.44))