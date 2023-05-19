import PySimpleGUI as sg
import functions

label = sg.Text("Type in a To-Do ")
input_box = sg.InputText(tooltip="Enter Todo", key='todo')

add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 12))


while True:
    event, values = window.read()
    #print(window.read())
    print("1 Event", event)
    print("2 Values", values)
    print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_value = values['todo']+'\n'
            todos.append(new_value)
            functions.write_todo(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            todos = functions.get_todos()
            todo_to_complete = values['todos'][0]
            todos.remove(todo_to_complete)
            functions.write_todo(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todo(todos)
            window['todos'].update(values=todos)
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
window.close()