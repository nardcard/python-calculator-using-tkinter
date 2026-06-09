

import tkinter as tk

#window setup
#main window for the calculator
root = tk.Tk()
root.title("calculator")
#size of the window on screen
root.geometry("300x400")

expression=""

#function to handle button clicks
def button_click(value):
    global expression
    #builds expression
    expression += str(value)
    #clears input box
    input_display.delete(0, tk.END)
    #shows the updated expression
    input_display.insert(0, expression)

#function for ac button to clear
def clear():
    global expression
    expression=""
    input_display.delete(0, tk.END)

#function for "=" to work
def evaluate():
    global expression
    #try/except will prevent crashes is an invalid input is input
    try:
        #eval(expression) will read the string as maths
        result = str(eval(expression))
        input_display.delete(0,tk.END)
        input_display.insert(0,result)
        expression=result
    except:
        input_display.delete(0, tk.END)
        input_display.insert(0, "ERROR")
        expression=""

#input display
input_display =tk.Entry(root)
#allows the window to be seen( .grid alignes it wit hmy buttons and makes it visible)
input_display.grid(row=0, column=0, columnspan=4)

#output display
#where results appear later
output_display =tk.Label(root, text="")
output_display.grid(row=1, column=0, columnspan=4)



#buttons and placement.

#end layout for the buttons and display
#row 0:    input display
#row 1:   output display
#Row 2:   AC   ()   %   /
#Row 3:   7    8    9   x
#Row 4:   4    5    6   -
#Row 5:   1    2    3   +
#Row 6:   0    .  back   =

#tk.button creates a clickable button
#.grid puts the buttons into a grid pattern(for me its row=0 column=0 to row=6 column=3)

#ac( clear all) button.    
ac_btn =tk.Button(root, text="AC", command=clear)
ac_btn.grid(row=2, column=0)

#bracket button
bracket_btn =tk.Button(root, text="()")
bracket_btn.grid(row=2, column=1)

#percentage button
percentage_btn =tk.Button(root, text="%")
percentage_btn.grid(row=2, column=2)

#division button
division_btn =tk.Button(root, text="/", command=lambda: button_click("/"))
division_btn.grid(row=2, column=3)


#number 7 button
btn7 =tk.Button(root, text="7", command=lambda: button_click("7"))
btn7.grid(row=3, column=0)

#number 8 button
btn8 =tk.Button(root, text="8", command=lambda: button_click("8"))
btn8.grid(row=3, column=1)

#number 9 button
btn9 =tk.Button(root, text="9", command=lambda: button_click("9"))
btn9.grid(row=3, column=2)

#multiplication button
multiplication_btn =tk.Button(root, text="x", command=lambda: button_click("*"))
multiplication_btn.grid(row=3, column=3)

#number 4 button
btn4 =tk.Button(root, text="4", command=lambda: button_click("4"))
btn4.grid(row=4, column=0)

#number 5 button
btn5 =tk.Button(root, text="5", command=lambda: button_click("5"))
btn5.grid(row=4, column=1)

#number 6 button
btn6 =tk.Button(root, text="6", command=lambda: button_click("6"))
btn6.grid(row=4, column=2)

#subtraction button
subtraction_btn =tk.Button(root, text="-", command=lambda: button_click("-"))
subtraction_btn.grid(row=4, column=3)

#number 1 button
btn1 =tk.Button(root, text="1", command=lambda: button_click("1"))
btn1.grid(row=5, column= 0)

#number 2 button
btn2 =tk.Button(root, text="2", command=lambda: button_click("2"))
btn2.grid(row=5, column=1)

#number 3 button
btn3 =tk.Button(root, text="3", command=lambda: button_click("3"))
btn3.grid(row=5, column=2)

#addition button
addition_btn =tk.Button(root, text="+", command=lambda: button_click("+"))
addition_btn.grid(row=5, column=3)

#number 0 button
btn0 =tk.Button(root, text="0", command=lambda: button_click("0"))
btn0.grid(row=6, column=0)

#decimal point button
decimal_point_btn =tk.Button(root, text=".", command=lambda: button_click("."))
decimal_point_btn.grid(row=6, column=1)

#backspace button
back_btn =tk.Button(root, text="back")
back_btn.grid(row=6, column=2)

#equals button
equals_btn =tk.Button(root, text="=", command=evaluate)
equals_btn.grid(row=6, column=3)














#keep the window open so it doesnt instantly close 
root.mainloop()