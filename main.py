import tkinter

FONT =("Comic Sans MS", 8, "normal")

#window
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(300, 00)
window.config(padx = 75, pady = 75)

#bmi def
def write_results(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi < 18.5:
        result_string += "Underweight"
    elif 18.5 <= bmi < 25:
        result_string += "Normal"
    elif 25 <= bmi < 30:
        result_string += "Overweight"
    elif 30 <= bmi < 35:
        result_string += "Grade 1 Obesity"
    elif 35 <= bmi < 40:
        result_string += "Grade 2 Obesity"
    elif bmi >= 40:
        result_string += "Grade 3 Obesity"
    return result_string

#label
my_label1 = tkinter.Label(text = "Enter your weight(kg)", font = FONT)

my_label2 = tkinter.Label(text = "Enter your height(cm)", font = FONT)

result_label = tkinter.Label(font = FONT)

#entry
my_entry1 = tkinter.Entry()

my_entry2 = tkinter.Entry()

#click button
def bmi_calculated():
    if my_entry1.get() == "" or my_entry2.get() == "":
        result_label.config(text = "Please enter both your weight and height!")
    else:
        try:
            bmi = float(my_entry1.get()) / (float(my_entry2.get()) / 100) ** 2
            result_string = write_results(bmi)
            result_label.config(text = result_string)

            #metin değiştikten sonra hizala
            #result_label.place(x = window.winfo_width() - result_label.winfo_width(), y = 220 - 10.5)
        except ValueError:
            result_label.config(text = "Enter a valid number!")
            #result_label.place(x = (window.winfo_width() - result_label.winfo_width()), y = 220 - 10.5)

my_button = tkinter.Button(text = "Calculate", font = FONT, command = bmi_calculated)

my_label1.pack()
my_entry1.pack()
my_label2.pack()
my_entry2.pack()
my_button.pack()
result_label.pack()

window.mainloop()