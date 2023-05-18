#pending download git
#day_15

#from functions import get_todos,write_todo
import functions
import time
print("Hello")
while True:
    user_action = input('Type add, show, edit, complete or exit ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo+'\n')                           #Option 2 is recommended over option 1
        
        functions.write_todo(todos)
            
    elif user_action.startswith('show'):
        todos = functions.get_todos()
        
        new_todo =[item.strip('\n') for item in todos] #option 2
        for index, item in enumerate(new_todo):
            #item = item.strip()                       #option 3
            print(f'{index+1}-{item}')
            
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            
            todos = functions.get_todos()

            todo_new = input('Enter new todo: ')
            todos[number] = todo_new + '\n'
            
            functions.write_todo(todos)
        except ValueError:
            print('Your Command is not Valid.')
            continue
            
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            
            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(number-1)
            
            functions.write_todo(todos)
                
            message = f'Todos {todo_to_remove.strip()} removed from the List.'
            print(message)
        except IndexError:
            print('Their is no Item with that number')
            continue
        
    elif user_action.startswith('exit'):
        break
    else:
        #print('Hey, You entered an unknown commmand.')
        print('THe command is not valid.')
print('bye!!')