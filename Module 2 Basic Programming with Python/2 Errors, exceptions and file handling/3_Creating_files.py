
""" THIS FUNCTION WILL CREATE A FILE OR OVERRIDE AN EXISTING FILE """

# with open('./files/newfile.txt', 'w') as file:
#     # file.write("This is a new file created!")
#     file.writelines(['2 This is a new file created',
#                     '\nThis is another line to be added'])


""" APPENDING CONTENT  TO THE FILE """

with open('./files/newfile.txt', 'a') as file:
    # file.write("This is a new file created!")
    file.writelines(['\nThis is a new file created',
                    '\nThis is another line to be added'])


""" 
In Python you can create files and insert content into those files. Which method allows you to write a list in a file instead of just a single line of text?  


writelines function

Correct
Correct! To write multiple lines of content you use the writelines() function. You use the write() function to add one line of content and the open() function to create, write or read a file.  
"""
