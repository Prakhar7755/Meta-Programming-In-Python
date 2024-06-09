menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]


# map(function,article that will be passed)

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee


""" 
map_coffee = map(find_coffee, menu)
# map_coffee = list(map(find_coffee, menu))

print("MAP OBJECT RECEIVED", map_coffee)

for x in map_coffee:
    print(x)
 """

# FILTER FUNCTION

filter_coffee = filter(find_coffee, menu)
print("FILTER OBJECT RECEIVED", filter_coffee)

for x in filter_coffee:
    print(x)
""" 
cappuccino
cortado 
"""
