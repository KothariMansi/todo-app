import os


#FILEPATH = 'C:/Users/PC/Desktop/python/udemy_python/files/todoss.txt'
FILEPATH = 'files/todoss.txt'
def create_file(FILEPATH):
    if not os.path.exists(FILEPATH):
        with open(FILEPATH, 'w') as file:
            pass

def get_todos(file_path=FILEPATH):
    """Read a text file and return the
       list of todo item."""
    with open(file_path, 'r') as file_local:   #option 2
        todos_local = file_local.readlines()                 #Benefit: Don't need to close file
        return todos_local                                        #Option 2 is recommended over option 1

def write_todo(todos_args,file_path=FILEPATH):
    """ Write the to-do item list in the text file."""
    with open(file_path, 'w') as file:
        file.writelines(todos_args)

#print('I am outside!')

print('__name__=',__name__)
if __name__ == "__main__":
    print('Hello')