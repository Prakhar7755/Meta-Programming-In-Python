data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end=" ")
""" <generator object <genexpr> at 0x00000259C1E34F40>
<class 'generator'>
2 3 5 7 11 13 17 19 23 29 31  """
