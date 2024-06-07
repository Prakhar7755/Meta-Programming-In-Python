# a = 5/0  ZeroDivisionError: division by zero
def divide(a, b):
    return a/b


print(divide(4, 6))  # 0.6666666666666666
# print(divide(4,0));ZeroDivisionError: division by zero

try:
    ans = divide(40, 0)
except:
    print("Something went wrong")

'''
Something went wrong
'''

try:
    ans = divide(40, 0)

except Exception as e:
    print("Something went wrong", e)
    print(e.__class__)

except ZeroDivisionError as e:
    print(e, "we can't divide by ZERO")
""" 
Something went wrong division by zero
<class 'ZeroDivisionError'>
 """


""" Like with any programming language exceptions happen in Python. You can handle more than one exception by chaining the except statement by adding another except statement. 


True
Correct
That's correct! It is possible to handle more than one exception without knowing what they are ahead of time by chaining except statements together.  """
