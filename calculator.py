

import tkinter as tk


#main window for the calculator
root = tk.Tk()
root.title("calculator")
#size of the window on screen
root.geometry("300x400")

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
ac_btn =tk.Button(root, text="ac")
ac_btn.grid(row=2, column=0)

#bracket button
bracket_btn =tk.Button(root, text="()")
bracket_btn.grid(row=2, column=1)

#percentage button
percentage_btn =tk.Button(root, text="%")
percentage_btn.grid(row=2, column=2)

#division button
division_btn =tk.Button(root, text="/")
division_btn.grid(row=2, column=3)


#number 7 button
btn7 =tk.Button(root, text="7")
btn7.grid(row=3, column=0)

#number 8 button
btn8 =tk.Button(root, text="8")
btn8.grid(row=3, column=1)

#number 9 button
btn9 =tk.Button(root, text="9")
btn9.grid(row=3, column=2)

#multiplication button
multiplication_btn =tk.Button(root, text="x")
multiplication_btn.grid(row=3, column=3)

#number 1 button
btn1 =tk.Button(root, text="1")
btn1.grid(row=4, column= 0)

#number 2 button
btn2 =tk.Button(root, text="2")
btn2.grid(row=4, column=1)

#number 3 button
btn3 =tk.Button(root, text="3")
btn3.grid(row=4, column=2)

#addition button
addition_button =tk.Button(root, text="+")
addition_button.grid(row=4, column=3)

#















#keep the window open so it doesnt instantly close 
root.mainloop()