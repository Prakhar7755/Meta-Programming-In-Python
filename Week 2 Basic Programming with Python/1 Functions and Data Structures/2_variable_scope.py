my_global = 10


def fn1():
    enclosed_v = 8

    def fn2():
        local_v = 5
        my_global = 6
        print("access to global var", my_global)
        print("access to enclosed var", enclosed_v)
        print("access to local var", local_v)
    fn2()


fn1()

# print("can't access local var:",local_v)
print("updated global var:", my_global)

""" In your program, you've declared the enclosed variable a = 'Hello'. 

At which scope levels is this variable accessible? 

Select all that apply.      
Enclosed
Correct! As this is the level of declaration, the variable is accessible here.      


Local
Correct! Enclosed variables can be accessed locally.      



 """
