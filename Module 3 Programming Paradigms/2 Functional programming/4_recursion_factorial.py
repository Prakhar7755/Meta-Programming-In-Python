def find_factorial_recursive(n):
    if n == 1:
        return 1
    return n*find_factorial_recursive(n-1)


print(find_factorial_recursive(1))
print(find_factorial_recursive(2))
print(find_factorial_recursive(3))
print(find_factorial_recursive(4))
print(find_factorial_recursive(5))
print(find_factorial_recursive(6))

""" 
Which of the following are advantages of using recursions? Check all that apply.     

Generation of sequences can be easier to understand than nested loops. 


Yes! It is easier to create a sequence with a recursion than with nested loops.

Complex tasks can be broken down into easier-to-read sub-problems . 


Correct. Recursive code is especially good for working on things that have many possible branches and are too complex for an iterative approach.      

Recursive code can make your code neater and less bulky.


Yes, that is correct.  Recursive code is simpler than nested loops.      
"""
