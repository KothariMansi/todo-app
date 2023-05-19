import PySimpleGUI as sg
import parser14

feet_label = sg.Text("Enter Feet ", key='feet')
feet_input = sg.InputText(key='input1')

inches_label = sg.Text("Enter Inches", key='inches')
inches_input = sg.InputText(key='input2')

convert = sg.Button('Convert', key='convert')

meter_output = sg.Text(key='output')

layout = [[feet_label, feet_input], [inches_label, inches_input], [convert, meter_output]]
window = sg.Window("Convertor", layout=layout)
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "convert":
            feet = values['input1']
            inches = values['input2']
            converted = parser14.convert(int(feet), int(inches))
            window['output'].update(f"{converted} m")
        case sg.WIN_CLOSED:
            break

window.close()