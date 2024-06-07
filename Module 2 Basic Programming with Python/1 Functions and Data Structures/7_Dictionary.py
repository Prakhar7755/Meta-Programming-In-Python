my_dict = {
    1: "Test",
    "Name": "Jim"
}
print(type(my_dict))  # <class 'dict'>

print(my_dict)  # {1: 'Test', 'Name': 'Jim'}
print(my_dict["Name"])  # Jim
print(my_dict[1])  # Test

my_dict[1] = "UpdatedTest"
print(my_dict)  # {1: 'UpdatedTest', 'Name': 'Jim'}

""" del my_dict[1];
print(my_dict) # { 'Name': 'Jim'} """

for key, value in my_dict.items():
    print(str(key)+" : "+value)
""" 
1 : UpdatedTest
Name : Jim
"""
