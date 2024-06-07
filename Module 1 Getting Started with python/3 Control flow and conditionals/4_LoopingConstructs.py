
for i in range(10):
    print("Looping", i)
""" 
Looping 0
Looping 1
Looping 2
Looping 3
Looping 4
Looping 5
Looping 6
Looping 7
Looping 8
Looping 9 
"""

favorites = ["Creme brulee", 'Apple Pie',
             'Churros', 'Timarisu', 'Chocolate Cake']
for item in favorites:
    print(item)
""" 
Creme brulee
Apple Pie
Churros
Timarisu
Chocolate Cake 
"""

#   WHILE LOOP

count = 0

while count < len(favorites):
    print('One of my favorite desserts is', favorites[count])
    count += 1
""" 
I like this dessert Creme brulee
I like this dessert Apple Pie
I like this dessert Churros
I like this dessert Timarisu
I like this dessert Chocolate Cake
"""
