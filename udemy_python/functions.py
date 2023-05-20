import os

if not os.path.exists('files/todoss.txt'):
    with open('files/todoss.txt', 'w') as file:
        pass

FILEPATH = 'files/todoss.txt'

def get_todos(file_path=FILEPATH):
    """Read a text file and return the
       list of todo item."""
    with open(file_path,'r') as file_local:   #option 2
        todos_local = file_local.readlines()                 #Benefit: Don't need to close file
        return todos_local                                        #Option 2 is recommended over option 1

def write_todo(todos_args,file_path=FILEPATH):
    """ Write the to-do item list in the text file."""
    with open(file_path,'w') as file:
        file.writelines(todos_args)

#print('I am outside!')

print('__name__=',__name__)
if __name__ == "__main__":
    print('Hello')