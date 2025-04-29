import customtkinter as ctk


# main window
ctk.set_appearance_mode("Dark")

root = ctk.CTk()
root.configure(fg_color="#000000")
root.geometry("400x380")
root.title("Four Function Calculator")
root.resizable(False, False)

# make the entry field where the value will be shown
display_box = ctk.CTkEntry(master=root, height=50, justify="right",
                           font=("Helvetica", 40, "bold"), fg_color="#000000", text_color="#FFFFFF")
display_box.pack(padx=5, fill="x")


# display update function
def display_update(t):
    display_box.configure(state="normal")
    display_box.delete(0, "end")
    display_box.insert(0, t)
    display_box.configure(state="readonly")

# setting the initial display to 0
display_update("0")

# make the buttons
frame = ctk.CTkFrame(master=root, fg_color="#000000")
frame.pack(pady=10)

btn_counter = 0

buttons = [
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "x",
    "AC", "0", "=", "/"
]

for i in range(4):
    for j in range(4): # since we want 4x4
        text = buttons[btn_counter]

        if text in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            button = ctk.CTkButton(master=frame, text=text, 
                                height=65, width=80, 
                                fg_color="#333333", text_color="#FFFFFF", hover_color="#555555",
                                font=("Helvetica", 24, "bold"), corner_radius=30,
                                command=lambda t=text: calculate(t))
            button.grid(row=i, column=j, padx=5, pady=5)

        elif text in ["+", "-", "x", "/"]:
            button = ctk.CTkButton(master=frame, text=text, 
                                height=65, width=80, 
                                fg_color="#F5A623", text_color="#FFFFFF", hover_color="#E08E1E",
                                font=("Helvetica", 24, "bold"), corner_radius=30,
                                command=lambda t=text: calculate(t))
        
            button.grid(row=i, column=j, padx=5, pady=5)
        elif text == "AC":
            button = ctk.CTkButton(master=frame, text=text, 
                                height=65, width=80, 
                                fg_color="#A5A5A5", text_color="#000000", hover_color="#8C8C8C",
                                font=("Helvetica", 24, "bold"), corner_radius=30,
                                command=lambda t=text: calculate(t))
        
            button.grid(row=i, column=j, padx=5, pady=5)
        elif text == "=":
            button = ctk.CTkButton(master=frame, text=text, 
                                height=65, width=80, 
                                fg_color="#F5A623", text_color="#FFFFFF", hover_color="#E08E1E",
                                font=("Helvetica", 24, "bold"), corner_radius=30,
                                command=lambda t=text: calculate(t))
        
            button.grid(row=i, column=j, padx=5, pady=5)

        btn_counter += 1

# calculation 
# variable for the 2 numbers and operative
first_num = ""
second_num = ""
operator = ""
first_done = False

# creating the reset eveything function
def reset():
    global first_num, second_num, operator, first_done

    first_num = ""
    second_num = ""
    operator = ""
    first_done = False


def calculate(t):
    global first_num, second_num, operator, first_done
    # check for numbers
    if t in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        # if first_done = False, keep catanating first_num
        if first_done == False:
            first_num = first_num + t
            # update display with first_num
            display_update(first_num)

        # else keep catanating second_num
        elif first_done == True:
            second_num = second_num + t
            # update display with second_num
            display_update(second_num)

    # else if check for operator
    elif t in ["+", "-", "x", "/"]:
        display_update(t) # updating the display with the operator
        operator = t # storing the operator
        first_done = True # marking the end of first num


    # else if check for AC
    elif t == "AC":
        # reset all variables
        reset()
        # set the display_box back to "0"
        display_update("0")

    # else if check for =
    elif t == "=":
        # get the result
        try:
            first = float(first_num)
            second = float(second_num)

            if operator == "+":
                result = first + second
            elif operator == "-":
                result = first - second
            elif operator == "x":
                result = first * second
            if operator == "/":
                result = first / second
                
            # display the value
            result = str(result)
            display_update(result)
            reset() # reseting everything after the result so that nothing shows up on display box
        except (ValueError, ZeroDivisionError):
            display_update("Error")
            reset()


# keeping the main window
root.mainloop()