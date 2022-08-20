import tkinter

window = tkinter.Tk()
window.title("GUI Test 1")
window.minsize(width=500, height=500)

def button_clicked():
    new_text = round(int(miles_entry.get()) * 1.6, 3)
    converted_km.config(text=new_text)

miles_entry = tkinter.Entry(width=10)
miles_entry.insert(0, string="0")
miles_entry.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0,column=2)

text_label = tkinter.Label(text="is equal to")
text_label.grid(row=1,column=0)

converted_km = tkinter.Label(text="0")
converted_km.grid(row=1, column=1)

kilo_label = tkinter.Label(text="Km")
kilo_label.grid(row=1,column=2)

convert_button = tkinter.Button(text="click me", command=button_clicked)
convert_button.grid(row=2,column=1)


window.mainloop()