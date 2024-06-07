str = "racecar"


def is_palindrome(str):
    startIndex = 0
    endIndex = len(str)-1

    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True


print(is_palindrome(str))
print(is_palindrome(str+"s"))

""" 
 Algorithms are very useful in programming. Which of the following statements about an algorithm are true?  Select all that apply.      


An algorithm is a series of steps to solve a problem.

That's correct! An algorithm solves both small and complex problems by executing the same steps each time.   

Once created the steps of an algorithm are the same every time. 

That's correct! An algorithm solves both small and complex problems by executing the same steps each time.  
"""
