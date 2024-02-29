import PySimpleGUI as gui

feet_label = gui.Text("Enter feet:")
inches_label = gui.Text("Enter inches:")
text_box1 = gui.Input()
text_box2 = gui.Input()
button = gui.Button("Convert")

window = gui.Window("Convertor",
                    layout=[[feet_label, text_box1],
                            [inches_label, text_box2],
                            [button]])
window.read()
#
window.close()
