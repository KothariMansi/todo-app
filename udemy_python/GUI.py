import PySimpleGUI as sg
import functions

label = sg.Text("Type in a To-Do ")
input_box = sg.InputText(tooltip="Enter Todo",key='todo')
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label,add_button],[input_box]],
                   font=("Helvetica",20))

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_value = values['todo']+'\n'
            todos.append(new_value)
            functions.write_todo(todos)
        case sg.WIN_CLOSED:
            break
window.close()