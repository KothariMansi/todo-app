import PySimpleGUI as sg
 
label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")
 
window = sg.Window("File Compressor",
                   layout=[[label],
                           [option1], [option2], [option3], [option4]
                           ])
 
window.read()
window.close()
###########
import PySimpleGUI as sg

feet_text = sg.Text("Enter feet:")
feet_input = sg.InputText()

inches_text = sg.Text("Enter inches:")
inches_input = sg.InputText()

convertor = sg.Button("Convertor")


window = sg.Window("Convertor",layout=[[feet_text,feet_input],[inches_text,inches_input],[convertor]])

window.read()
window.close()