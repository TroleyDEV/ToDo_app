import time

import PySimpleGUI as sg

import functions

sg.theme('DarkBlack')

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip='Enter todo', key="todo")
add_button = sg.Button(size=2, image_source="add.png", key='Add', mouseover_colors="LightBlue2", tooltip="Add Todo")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button(size=10, image_source="complete.png", key='Complete')

exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    if event == sg.WINDOW_CLOSED:
        break
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))  # Simple clock
    print(1, event)
    match event:
        case "Add":
            todos = functions.get_todos()  # Get existing todos from file
            new_todo = values['todo'] + "\n"  # Store new to-do in variable
            todos.append(new_todo)  # Add new to-do to existing list
            functions.write_todos(todos)  # Write new list to the file
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select and item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select and item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

window.close()
