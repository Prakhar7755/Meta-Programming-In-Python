# IMPURE FUNCTION


"""
 my_list = [1,2,3];

def add_to_list(item):
  return my_list.append(item);

add_to_list(4)

print(my_list) [1, 2, 3, 4]
 """


# PURE FUNCTIONS

my_list = [1, 2, 3]


def add_to_list(lst,item):
    # CREATING A NEW LIST AND THEN EDITING THAT SO THAT THE GLOBAL DATA DOESN'T CHANGE
    nl = lst.copy();
    nl.append(item)
    return nl


new_list = add_to_list(my_list,4)

print(my_list)  # [1, 2, 3]
print(new_list)  # [1, 2, 3, 4]
