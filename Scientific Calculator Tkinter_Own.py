import tkinter as tk
import math

angle_mode="DEG" #Default mode is degrees

#FUNCTIONS
def sin_func(x):
    return math.sin(math.radians(x)) if angle_mode == "DEG" else math.sin(x)

def cos_func(x):
    return math.cos(math.radians(x)) if angle_mode == "DEG" else math.cos(x)

def tan_func(x):
    return math.tan(math.radians(x)) if angle_mode == "DEG" else math.tan(x)

# Button functions
def press_button(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

def toggle_mode():
    global angle_mode
    angle_mode = "RAD" if angle_mode == "DEG" else "DEG"
    mode_button.config(text=f"Mode: {angle_mode}")

def calculate():
    try:
        expr = entry.get()
        safe_dict = {
            "sin": sin_func,
            "cos": cos_func,
            "tan": tan_func,
            "sqrt": math.sqrt,
            "log": math.log,
            "exp": math.exp,
            "%": lambda a,b: a%b,
            "math": math
        }
        result = eval(expr, {"__builtins__": None}, safe_dict)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

#MAIN WINDOW
root=tk.Tk()
root.title("Scientifc Calculator")

#ENTRY DISPLAY
entry=tk.Entry(root, width=30, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=5)

#BUTTONS LAYOUT
buttons=["7","8","9","/","sin(",
         "4","5","6","*","cos(",
         "1","2","3","-","tan(",
         "0",".","+","**","sqrt(",
         "(",")","log(","exp(","%"]

row=1
col=0
for b in buttons:
    tk.Button(root, text=b, width=8, height=2,
              command=lambda val=b: press_button(val)).grid(row=row, column=col)
    col+=1
    if col>4:
        col=0
        row+=1

#SPECIAL BUTTONS
tk.Button(root, text="Clear", width=8, height=2, command=clear_entry).grid(row=row, column=0)
tk.Button(root, text="=", width=18, height=2, command=calculate).grid(row=row, column=1, columnspan=2)

#MODE TOGGLE BUTTON
mode_button=tk.Button(root, text="Mode: DEG", width=8, height=2, command=toggle_mode)
mode_button.grid(row=row, column=3)

root.mainloop()
