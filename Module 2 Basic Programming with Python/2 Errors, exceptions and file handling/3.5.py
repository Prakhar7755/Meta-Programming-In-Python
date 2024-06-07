try:
  with open('./sample/newfile.txt', 'r') as file:
      file.writelines(['\nThis is a new file created',
                      '\nThis is another line to be added'])
except FileNotFoundError as e:
   print("ERROR",e);

#  ERROR [Errno 2] No such file or directory: './sample/newfile.txt'
 