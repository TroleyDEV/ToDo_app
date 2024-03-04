# Create a desktop GUI program that gets feet and inches from the user and outputs the results in meters.

import PySimpleGUI as sg

sg.theme('DarkBlack')

# Widgets declaration

feet_label = sg.Text("Enter feet:")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches:")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
exit_button = sg.Button("Exit")
result = sg.Text(key="result")

# Window declaration

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, exit_button, result]],
                   font=('Helvetica', 20))

# Main loop

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    print(event)
    print(values)
    match event:
        case "Convert":
            try:
                meters = float(values["feet"]) * 0.3048 + float(values["inches"]) * 0.0254
                window["result"].update(value=f'{meters} m')
            except ValueError:
                sg.popup("Please provide two numbers")
        case "Exit":
            break

window.close()
