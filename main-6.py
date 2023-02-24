from tkinter import *
from tkinter import ttk
from tkinter import filedialog

filename = 'patients_data.txt'
count = 0


class patient_management_system():  # creating class with name patient_management_system
    def __init__(self):  # initializing constructor
        self.window = Tk()  # creating tkinter window with name window
        self.window.geometry('400x400')  # setting the geometry of window
        self.window.title('My Patient Program')  # title of the window

    def label_creator(self, window, text, x_pos, y_pos):  # creating function label_creator with parameters window,
        # text, x_pos, y_pos
        label = ttk.Label(window, text=text, font=(None, 15))  # create tkinter Label with given parameters
        label.place(x=x_pos, y=y_pos)  # positioning the labels with given x_pos, and y_pos

        return label  # return label value

    def entry_box_creator(self, window, x_pos, y_pos):  # creating function entry_box_creator with parameters window,
        # x_pos, y_pos
        var = StringVar()  # creating variable
        entry = ttk.Entry(window, textvariable=var, font=('', 10))  # creating entry box
        entry.place(x=x_pos, y=y_pos, height=25)  # placing entry box on window

        return entry  # return entry widget

    def button_creator(self, window, text, x_pos,
                       y_pos):  # defining function button_creator with parameters window, text, x_pos, y_pos
        btn = ttk.Button(window, text=text)  # create button with parameters
        btn.place(x=x_pos, y=y_pos)  # place button

        return btn  # return button widget


def fileopen_func():  # defining function
    global show_data  # make show_data a global variable

    file_name = filedialog.askopenfile()  # opening dialog box to select file, save path of file in variable

    try:
        with open(file_name.name) as fileopen:  # open file
            data = fileopen.readlines()  # read lines
    except:
        return None
    show_data = Listbox(main_screen.window, font=('', 15))  # create Listbox to show data
    show_data.place(x=5, y=5, width=390, height=390)  # placing Listbox

    for current_line in data:  # using for loop to iterate though data from file
        show_data.insert('end', current_line.strip('\n'))  # insert data in Listbox


def add_patient():  # create function to add_patient
    add_patient_screen = patient_management_system()  # create object of class patient_management_system
    add_patient_screen.window.title('New Patient')  # set title of window
    label_1 = add_patient_screen.label_creator(add_patient_screen.window, 'First and Lastname', 5, 10)  # create label
    label_1.config(font=('', 10))  # set font of label
    entry_1 = add_patient_screen.entry_box_creator(add_patient_screen.window, 150, 10)  # create entry box
    entry_1.config(width=25)  # set width of entry widget

    label_2 = add_patient_screen.label_creator(add_patient_screen.window, 'Address', 5, 45)  # create label
    label_2.config(font=('', 10))  # set font size
    entry_2 = add_patient_screen.entry_box_creator(add_patient_screen.window, 150, 45)  # create entry widget
    entry_2.config(width=25)  # place entry widget

    label_3 = add_patient_screen.label_creator(add_patient_screen.window, 'Birthday (mm/dd/yy)', 5, 80)  # create label
    label_3.config(font=('', 10))  # set label font size
    entry_3 = add_patient_screen.entry_box_creator(add_patient_screen.window, 150, 80)  # create entry widget
    entry_3.config(width=25)  # set width of entry widget

    def close():  # defining function close
        add_patient_screen.window.destroy()  # destroy add patient screen

    btn_1 = add_patient_screen.button_creator(add_patient_screen.window, 'Close', 80, y_pos=355)  # creating button
    btn_1.config(width=20, command=close)  # set width and command of button

    def save_new_data():  # create function
        try:  # using try block
            show_data.insert('end', f'{entry_1.get()}, {entry_2.get()}, {entry_3.get()}')  # insert data
        except Exception:  # except block
            pass  # pass
        add_patient_screen.window.destroy()  # destroy add_patient screen

    btn_2 = add_patient_screen.button_creator(add_patient_screen.window, 'Save', 210,
                                              y_pos=355)  # create button on add_patient screen
    btn_2.config(width=20, command=save_new_data)  # configure button with width and commands


def modify_patients_data():  # create function modify_patients_data
    global count  # make global variable count
    count = 0  # set value of count 0

    modify_patient_screen = patient_management_system()  # create object of patient_management_system

    modify_patient_screen.window.title('Modify Patient')  # set title of window
    label_1 = modify_patient_screen.label_creator(modify_patient_screen.window, 'First and Lastname', 5,
                                                  10)  # add label on screen
    label_1.config(font=('', 10))  # configure label with font size
    entry_1 = modify_patient_screen.entry_box_creator(modify_patient_screen.window, 150,
                                                      10)  # add entry widget on screen
    entry_1.config(width=25)  # configure entry widget with width size

    label_2 = modify_patient_screen.label_creator(modify_patient_screen.window, 'Address', 5, 45)  # add label on screen
    label_2.config(font=('', 10))  # configure label with font size
    entry_2 = modify_patient_screen.entry_box_creator(modify_patient_screen.window, 150,
                                                      45)  # add entry widget on screen
    entry_2.config(width=25)  # configure entry widget with width size

    label_3 = modify_patient_screen.label_creator(modify_patient_screen.window, 'Birthday (mm/dd/yy)', 5,
                                                  80)  # add label on screen
    label_3.config(font=('', 10))  # configure label with font size
    entry_3 = modify_patient_screen.entry_box_creator(modify_patient_screen.window, 150,
                                                      80)  # add entry widget on screen
    entry_3.config(width=25)  # configure entry widget with width size

    info = show_data.get(0)  # get first data from Listbox
    info = info.split(',')  # split value by ','
    try:
        entry_1.insert(0, info[0])  # insert first value at index 0
        entry_2.insert(0, info[1])  # insert second value at index 0
        entry_3.insert(0, info[2])  # insert third value at index 0
    except:
        return None

    def previous():  # define function to previous
        global count  # make global variable count
        count -= 1  # -1 value from count

        try:  # try block
            info = show_data.get(count)  # get value from index = count
            # same done below as done above
            info = info.split(',')
            entry_1.delete(0, 'end')
            entry_2.delete(0, 'end')
            entry_3.delete(0, 'end')
            entry_1.insert(0, info[0])
            entry_2.insert(0, info[1])
            entry_3.insert(0, info[2])

        except Exception:  # except block
            count = len(show_data.get(0, 'end')) - 1
            info = show_data.get(count)
            info = info.split(',')
            entry_1.insert(0, info[0])
            entry_2.insert(0, info[1])
            entry_3.insert(0, info[2])

    btn_1 = modify_patient_screen.button_creator(modify_patient_screen.window, 'Previous', 70,
                                                 y_pos=110)  # create button on modify screen
    btn_1.config(width=20, command=previous)  # configure button with width and command

    def next_info():  # define function next_info
        global count  # make global variable count
        count += 1  # +1 in count
        try:  # try block
            info = show_data.get(count)  # get index value of count from Listbox
            info = info.split(',')  # split data by ','
            # same done as above
            entry_1.delete(0, 'end')
            entry_2.delete(0, 'end')
            entry_3.delete(0, 'end')
            entry_1.insert(0, info[0])
            entry_2.insert(0, info[1])
            entry_3.insert(0, info[2])

        except Exception:  # exception block
            count = 0
            info = show_data.get(count)
            info = info.split(',')
            entry_1.insert(0, info[0])
            entry_2.insert(0, info[1])
            entry_3.insert(0, info[2])

    btn_2 = modify_patient_screen.button_creator(modify_patient_screen.window, 'Next', 200, y_pos=110)  # create button
    btn_2.config(width=20, command=next_info)  # configure button

    def close():  # define function close
        modify_patient_screen.window.destroy()  # destroy modify patients screen

    btn_3 = modify_patient_screen.button_creator(modify_patient_screen.window, 'Close', 70,
                                                 y_pos=370)  # create button on modify screen
    btn_3.config(width=20, command=close)  # configure button with width and command

    def update():  # define update function
        show_data.delete(count)  # delete from Listbox from the given index
        show_data.insert(count, f'{entry_1.get()},{entry_2.get()},{entry_3.get()}')  # insert value at given index
        show_data.update()  # update Listbox

    btn_4 = modify_patient_screen.button_creator(modify_patient_screen.window, 'Update', 200,
                                                 y_pos=370)  # create button
    btn_4.config(width=20, command=update)  # configure button


def save_data_inf_file():  # define save_data_inf_file
    all_info = show_data.get(0, 'end')  # get all data from Listbox

    with open(filename, 'w') as fileopen:  # open file as fileopen
        for info in all_info:  # iterate through data
            fileopen.write(str(info) + '\n')  # write data in file


main_screen = patient_management_system()  # create object of class patient_management_system

top_left_menu = Menu()  # create object of Menu
top_left_menu_items = Menu(top_left_menu, tearoff=0)  # create object of items of menu bar
top_left_menu_items.add_command(label='Open', command=fileopen_func)  # add label and command of menu bar

top_left_menu_items.add_command(label='New', command=add_patient)  # add label and command of menu bar
top_left_menu_items.add_command(label='Modify', command=modify_patients_data)  # add label and command of menu bar
top_left_menu_items.add_command(label='Save', command=save_data_inf_file)  # add label and command of menu bar
top_left_menu_items.add_separator()  # add seperator
top_left_menu_items.add_command(label='Exit', command=quit)  # add label and command of menu bar

main_screen.window.config(menu=top_left_menu)  # add menu items on menu bar
top_left_menu.add_cascade(label='File', menu=top_left_menu_items)  # add label and command of menu bar
top_left_menu.add_cascade(label='Help')  # add label and command of menu bar

show_data = Listbox()  # create Listbox
main_screen.label_creator(main_screen.window, 'Please load patient file.', 10,
                          10)  # create label on main window with passed values
main_screen.window.mainloop()  # using mainloop to keep the program running
