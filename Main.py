import PySimpleGUI as sg

sg.theme("LightBlue3")
layout = [
    [sg.Text("input excel file:"), sg.Input(key="-IN-"), sg.FileBrowse()],
    [sg.Text("output folder:"), sg.Input(key="-OUT-"), sg.FolderBrowse()],
    [sg.Exit(), sg.Button("Convert To CSV")]
]

window = sg.Window("excel to cvs converter", layout)

while True:
    event, values = window.read()
    print(event,values)
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Convert to CSV":
        sg.popup_error("Not Yet Implemented")
window.close()
