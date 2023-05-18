#main------------------

while True:
    user_action = input('Type add, show, edit, complete or exit ')
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input('Enter a todo ') + '\n'
            
            #file = open('files/todoss.txt','r')          #Option 1
            #todos = file.readlines()
            #file.close()
            
            with open('files/todoss.txt','r') as file:   #option 2
                todos = file.readlines()                 #Benefit: Don't need to close file
            todos.append(todo)                           #Option 2 is recommended over option 1
            
            with open('files/todoss.txt','w') as file:
                file.writelines(todos)
                
        case 'show' | 'display':
            file = open('files/todoss.txt','r')
            todos = file.readlines()
            file.close()
            #new_todo = []                                 #Option 1
            #for item in todos:
                #new_item = item.strip()
                #new_todo.append(new_item)
            new_todo =[item.strip('\n') for item in todos] #option 2
            for index, item in enumerate(new_todo):
                #item = item.strip()                       #option 3
                print(f'{index+1}-{item}')
                
        case 'edit':
            number = int(input('Number of todo to edit '))
            number = number - 1
            
            with open('files/todoss.txt','r') as file:
                todos = file.readlines()

            todo_new = input('Enter new todo: ')
            todos[number] = todo_new + '\n'
            
            with open('files/todoss.txt','w')  as file:
                file.writelines(todos)
        case 'complete':
            number = int(input('Number of the todo to complete: '))
            with open('files/todoss.txt','r')  as file:
                file.readlines()
            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(number-1)
            
            with open('files/todoss.txt','w')  as file:
                file.writelines(todos)
                
            message = f'Todos {todo_to_remove.strip()} removed from the List.'
            print(message)
            
        case 'exit':
            break
        case whatever:
            print('Hey, You entered an unknown commmand.')
print('bye!!')