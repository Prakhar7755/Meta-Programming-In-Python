list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d"]
list3 = ["Hello", 1, True, 20.44]

print(list1[2])

list4 = [1, [2, 3, 4], 5, 6]  # nested lists


print(*list1)
print(list1)
print(*list1, sep=", ")

list1.insert(len(list1), 6)
print(*list1, sep=", ")

list1.append(7)
print(*list1, sep=", ")

list1.extend([8, 9, 10])
print(list1)

list1.pop(4)
print("Poping idx 4:\t", *list1, sep=", ")

del list1[2]
print("deleting idx 2:\t", *list1, sep=", ")


for x in list1:
    print("Value", x)
    """ Value 1
Value 2
Value 4
Value 6
Value 7
Value 8
Value 9
Value 10 """

""" You need to add a new item to an existing list at a specified point in the index in your Python code. Which of the following functions can you use to complete this action?

insert()

Correct
Correct! The insert function is used to insert an item within an existing list at a specified index.     """
