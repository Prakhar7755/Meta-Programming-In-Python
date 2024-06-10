# class Recipe():
#     def __new__(cls) -> Self:
#         pass

#     def __init__(self) -> None:
#         pass
class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print(f"The {self.dish} has {self.items} and takes {
              self.time} min to prepare")


# Example usage:


pizza = Recipe("Pizza", ["cheese", "bread", 'tomato'], 45)
pasta = Recipe("Pasta", ["penne", "sauce"], 55)

print(pizza.items)
print(pasta.items)


print(pizza.contents())


my_recipe = Recipe(dish="Spaghetti Carbonara",
                   items="pasta, eggs, bacon, cheese", time=20)
my_recipe.contents()
