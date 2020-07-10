from tkinter import Tk, Label, Button, Frame, RAISED, Spinbox

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Smartplate")

        self.frame = Frame(master=master,
        relief = RAISED,
        borderwidth=1
        )

        # Week days
        for (i, day) in enumerate(["{1}: {0} week".format(1, 2020)]+["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]+["Min", "Max"]):
            self.label = Label(master=master, text=day)
            self.label.grid(row=0, column=i)

        # FoodEvents
        for (j, event) in enumerate(["Zöldség", "Gyümölcs", "Gabona", "Hús", "Friss hal","Belsöség", "Édesség", "Magvak", "Üditő", "Sport", "Súly"]):
            self.label = Label(master=master, text=event)
            self.label.grid(row=j+1, column=0)

        # Spinboxes
        for (j, event) in enumerate(["Zöldség", "Gyümölcs", "Gabona", "Hús", "Friss hal","Belsöség", "Édesség", "Magvak", "Üditő", "Sport", "Súly"]):
            for (i, day) in enumerate(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]):
                self.spinbox = Spinbox(master, from_=0, to=10, width=5)
                self.spinbox.grid(row=j+1, column=i+1)
                
        # Min-Max value
        for (j, event) in enumerate(["Zöldség", "Gyümölcs", "Gabona", "Hús", "Friss hal","Belsöség", "Édesség", "Magvak", "Üditő", "Sport", "Súly"]):
            self.label = Label(master=master, text=0)
            self.label.grid(row=j+1, column=8)

            self.label = Label(master=master, text=0)
            self.label.grid(row=j+1, column=9)

if __name__ == "__main__":
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()
        