import PySimpleGUI as sg

import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip='Enter todo', key="todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()  # Get existing todos from file
            new_todo = values['todo']  # Store new to-do in variable
            todos.append(new_todo)  # Add new to-do to existing list
            functions.write_todos(todos)  # Write new list to the file
        case sg.WINDOW_CLOSED:
            break

window.close()
