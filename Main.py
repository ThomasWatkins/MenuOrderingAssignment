import PySimpleGUI as sg

sg.theme("LightBlue3")
layout = [
    [sg.Text("input excel file:"), sg.Input(key="-IN-"), sg.FileBrowse()],
    [sg.Text("output folder:"), sg.Input(key="-OUT-"), sg.FolderBrowse()],
    [sg.Exit(), sg.Button("Convert To CSV"), sg.Button("HELLO!")],
    [sg.Text("input Username:",expand_x=1)],
    [sg.InputText(key="-TEXT-"), sg.Button("submit")],
]

window = sg.Window("excel to cvs converter", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Convert To CSV":
        sg.popup_error("Not Yet Implemented")
    if event == "HELLO!":
        print("you pressed hello")
    if event == "submit":
        text_input_value = values["-TEXT-"]
        print(text_input_value)
        
window.close()
