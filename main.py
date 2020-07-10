from tkinter import Tk, Label, Button, Frame, RAISED, Spinbox
from WeekClass import WeekClass

import datetime
import pickle

class MyFirstGUI:
    def __init__(self, master, weekdata):
        self.master = master
        master.title("Smartplate")

        self.frame = Frame(master=master,
        relief = RAISED,
        borderwidth=1
        )

        # Week days
        for (i, day) in enumerate(["{1}: {0} week".format(weekdata.weekNumber, weekdata.weekyear)]+weekdata.weekDays+["Min", "Max"]):
            self.label = Label(master=master, text=day)
            self.label.grid(row=0, column=i)

        # FoodEvents
        for (j, event) in enumerate(weekdata.foodEvents):
            self.label = Label(master=master, text=event)
            self.label.grid(row=j+1, column=0)

        # Spinboxes
        for (j, event) in enumerate(weekdata.foodEvents):
            for (i, day) in enumerate(weekdata.weekDays):
                # Spinbox default value
                self.spinbox = Spinbox(master, from_=weekdata.data[j][i], to=10, width=5)
                self.spinbox.grid(row=j+1, column=i+1)
                
        # Min-Max value
        for (j, event) in enumerate(weekdata.foodEvents):
            self.label = Label(master=master, text=0)
            self.label.grid(row=j+1, column=len(weekdata.weekDays)+1)

            self.label = Label(master=master, text=0)
            self.label.grid(row=j+1, column=len(weekdata.weekDays)+2)

if __name__ == "__main__":
    # This week data
    my_date = datetime.date.today()
    year, week_num, day_of_week = my_date.isocalendar()

    # Set up data
    # Check is there data for this week
    # if yes: open the file
    try:
        with open("week"+str(year)+str(week_num)+"_data.pkl", "rb") as input:
            weekdata = pickle.load(input)
    # if no: new class and save
    except:
        # Make new data object for the week data
        weekdata = WeekClass()
        # Save this weekdata object to a pickle file
        with open("week"+str(year)+str(week_num)+"_data.pkl", 'wb') as output:
            pickle.dump(weekdata, output, pickle.HIGHEST_PROTOCOL)

    # Set up GUI
    root = Tk()
    my_gui = MyFirstGUI(root, weekdata)
    root.mainloop()
        