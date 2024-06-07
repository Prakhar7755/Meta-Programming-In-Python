""" 
open and close function 

open(<FILE_NAME> <FILE_LOCATION>,<MODE>) --> 

different <MODES> 
    r => open and read (text format)
    rb => open and read(binary format)
    r+ => open for reading and writing
    w => open for writing
    a => open for editing and appending data
    (ADD 'b' AT THE END OF EACH ONE TO MAKE IT OPERATE ON BINARY)

close() - to close the open file connection

## opening a file using WITH OPEN FUNCTION

  with open('testing.txt','r') as file:
  
      THIS APPROACH CLOSES THE FILE AUTOMATICALLY
"""

# file = open("test.txt", mode="r")
with open("./files/test.txt", mode="r+") as file:
    data = file.readline()
    print(data)  # Hello there!








""" 
The open function is a versatile method that is used for file handling in Python. Which of the following statements are true? Choose all that apply. 


You can use it with the statement in the open function so that the file is automatically closed for you.  

Correct
Well done. It can also accept two arguments: the file name or file location and the mode, and you can use it with the statement in the open function so that the file is automatically closed for you.  


The open function can be used in three modes: reading, writing, or creating files. 

Correct
Well done. The open function can also be used in three modes: reading, writing or creating files, and you can use it with the statement in the open function so that the file is automatically closed for you.  


The open function can accept two arguments: the file name or file location, and the mode.

Correct
Well done.  The open function can also be used in three modes: reading, writing or creating files, and the open function can accept two arguments: the file name or file location, and the mode.
"""
