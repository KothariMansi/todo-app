import PySimpleGUI as sg
import functions
import time

sg.theme("Purple")
#TealMono
#GreenMono
#BlueMono
#LightGreen5
#LightBlue2
clock = sg.Text("", key='clock')

label = sg.Text("Type in a To-Do ")
input_box = sg.InputText(tooltip="Enter Todo", key='todo')

#add_button = sg.Button("Add")
add_button = sg.Button(key="Add", size=2, image_source='add.png', mouseover_colors='Purple')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")

complete_button = sg.Button(key="Complete", image_source='complete.png')

exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box],
                           [edit_button, complete_button, exit_button]],
                   font=("Helvetica", 12))

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

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
            try:
                todos = functions.get_todos()
                todo_to_complete = values['todos'][0]
                todos.remove(todo_to_complete)
                functions.write_todo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select an Item First')
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todo(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please Select an Item First")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
window.close()