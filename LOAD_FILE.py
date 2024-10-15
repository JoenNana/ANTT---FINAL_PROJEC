import PySimpleGUI as sg
import csv, os
import webbrowser

working_direction = os.getcwd

layout = [
    [sg.Text("Choose a PDF file:")],
    [sg.InputText(key = "-FILE_PATH-"),
     sg.FilesBrowse(initial_folder = working_direction, file_types=[("PDF FILE","*.pdf")])],
    [sg.Button("Submit"), sg.Exit()]
]

window = sg.Window('File Loader', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    elif event == "Submit":
        pdf_address = values["-FILE_PATH-"]
window.close()
