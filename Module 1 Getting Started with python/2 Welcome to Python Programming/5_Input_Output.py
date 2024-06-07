email = input('Enter your email: ')

print('Your entered:', email)

# print args

print(1, 2, 3)

# print arithmetic

print(4**5)


# str concatenation
print('Hello'+" World")



# WHEN YOU TAKE AN INPUT THEN IT RETURNS A STRING OUTPUT 
a = input('Enter a ')
b = input('Enter b ')

print("type of a and b is",type(a)) #  <class 'str'>
print(a+b)# STRING CONATENATED
print("after converting them to string",int(a)+int(b)) # TYPECAST FOR ADDTION


print('Hello',"World",sep=", ")



print("the value {} and {}".format(a,b))
print("the value {0} and {1}".format(a,b))
print("the value {1} and {0}".format(a,b))