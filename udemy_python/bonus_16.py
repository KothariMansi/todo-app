import PySimpleGUI as sg

label1 = sg.Text(text="Select files to Compress:")
input1 = sg.InputText()
choose_button1 = sg.FileBrowse("Choose")
label2 = sg.Text(text="Select destination folder:")
input2 = sg.InputText()
choose_button2 = sg.FileBrowse("Choose")

compress_button = sg.Button("Compressor")

window = sg.Window("File Compressor",layout=[[label1,input1,choose_button1],
                                             [label2,input2,choose_button2],
                                             [compress_button]])

window.read()
window.close()