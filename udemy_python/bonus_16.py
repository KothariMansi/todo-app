import PySimpleGUI as sg
import zip_creator

label1 = sg.Text(text="Select files to Compress:")
input1 = sg.InputText()
choose_button1 = sg.FileBrowse("Choose", key='files')
label2 = sg.Text(text="Select destination folder:")
input2 = sg.InputText()
choose_button2 = sg.FolderBrowse("Choose", key='folder')

compress_button = sg.Button("Compressor")
output = sg.Text(key='output', text_color='red')

window = sg.Window("File Compressor", layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [compress_button, output]])

while True:
    event, values = window.read()
    print(event, values)
    filepath = values['files'].split(';')
    folder = values['folder']
    match event:
        case 'Compressor':
            zip_creator.make_archive(filepaths=filepath, dest_dir=folder)
            window['output'].update(value="Compressor Completed")
        case sg.WIN_CLOSED:
            break

window.close()