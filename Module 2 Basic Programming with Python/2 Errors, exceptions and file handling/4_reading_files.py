""" read(), readline(), readlines() """

with open('./files/newfile.txt', 'r') as file:
    # print(file.read()); # read complete file
    # print(file.read(40)); # it tells to read approx 40 characters from the file
    
    # print(file.readline()); # read the first file
    print(file.readline(44))



    print("\n\nTIME FOR READLINES FUNCTION\n")
    # print(file.readlines()) # returns a list of all lines
    Lines = file.readlines()
    print(len(Lines))
    for line in Lines:
        print(line)

""" readlines() reads the entire contents of the file and returns it in an ordered list """


""" You want to read the entire contents of a file. What two methods can you use to do this?

read()

That’s right. The Read method returns the entire contents of the file as a string that will contain all the characters.

readlines()

That's right. The Readlines method reads the entire contents of the file and then returns it in an ordered list. This is useful because it allows you to iterate over the list or pick out specific lines based on a condition.

"""
