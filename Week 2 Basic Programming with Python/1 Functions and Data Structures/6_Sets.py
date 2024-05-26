set_a = {1, 2, 3, 4, 5}

print(set_a)
print(type(set_a))  # <class 'set'>

set_a.add(6)
set_a.remove(1)
set_a.remove(2)


print(set_a)  # {3, 4, 5, 6}

""" MATHEMATICAL OPERATIONS """
set_b = {3, 4, 5, 6, 7, 8, 9}

print(set_a.union(set_b))  # {3, 4, 5, 6, 7, 8, 9}
print(set_a | set_b)  # {3, 4, 5, 6, 7, 8, 9}

""" Can you place duplicate values inside your declared sets?
No

Correct
Correct! Sets do not accept duplicate values. """


print(set_a.intersection(set_b))  # {3, 4, 5, 6}
print(set_a & set_b)  # {3, 4, 5, 6}


print(set_a.difference(set_b)); # set()
print(set_a - set_b); # set()

# symmetric difference using ^