from ctypes import windll
from tkinter import *
windll.shcore.SetProcessDpiAwareness(1)

#window
my_window = Tk()
my_window.title("BMI Calculator")
my_window.minsize(width=370 , height=300)
my_window.config(bg="orange")

my_label2 = Label(text='BMI Calculator', font=('arial', 15, 'bold'), bg='orange')

my_label2.pack()

#label_for_height
my_label = Label(text='Enter Your Height(cm)', font=('arial', 10, 'bold'), bg='orange')
my_label.place(x=100,y=55)

#heightwindow_entry
my_height = Entry(width=20)
my_height.place(x=110,y=80)
my_height.config(fg="black")

#weightwindow
my_weight = Entry(width=20)
my_weight.place(x=110,y=150)
my_weight.config(fg="black")

#label_for_weight
my_label = Label(text='Enter Your Weight(kg)', font=('arial', 10, 'bold'), bg='orange')
my_label.place(x=100,y=120)

#result_label
result_label = Label(font=('arial', 10, 'bold'),bg="orange")
result_label.place(x=32,y=230)


#calculate button weight/height*2 =BMI
def p_button():
    try:
        a2=float(my_weight.get())
        a1=float(my_height.get())
        bmi = (a2 / ((a1/100)**2))
        result_string = write_result(bmi)
        result_label.config(text=result_string)
        write_result(bmi)
    except ValueError:
        result_label.config(text="Please enter a number ! .")
        my_weight.delete(0,END)
        my_height.delete(0,END)

button = Button(text="Calculate")
button.config(padx= 0.2 , pady= 0.2,bg="blue",font=('arial', 10, 'bold'),command=p_button)

button.place(x=150,y=180)

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        result_string += "normal weight"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string



my_window.mainloop()