from tkinter import Tk, Label, Button, Frame, RAISED, Spinbox, DoubleVar
from WeekClass import WeekClass

import datetime
import pickle

from chunks import chunks

class MainGUI:
    def __init__(self, master, weekdata):
        self.master = master
        master.title("Smartplate")

        self.frame = Frame(master=master,
        relief = RAISED,
        borderwidth=1
        )

        self.spinboxs = []

        # Week days
        for (i, day) in enumerate(["{1}: {0} week".format(weekdata.weekNumber, weekdata.weekyear)]+weekdata.weekDays+["Min", "Max"]):
            self.label = Label(master=master, text=day)
            self.label.grid(row=0, column=i)

        # FoodEvents
        for (j, event) in enumerate(weekdata.foodEvents):
            self.label = Label(master=master, text=event)
            self.label.grid(row=j+1, column=0)

        # Min-Max value
        for (j, weekMin) in enumerate(weekdata.weekMin):
            self.label = Label(master=master, text=weekMin)
            self.label.grid(row=j+1, column=len(weekdata.weekDays)+1)
        
        for (j, weekMax) in enumerate(weekdata.weekMax):
            self.label = Label(master=master, text=weekMax)
            self.label.grid(row=j+1, column=len(weekdata.weekDays)+2)

        # Spinboxes
        for (j, event) in enumerate(weekdata.foodEvents):
            for (i, day) in enumerate(weekdata.weekDays):
                # Spinbox default value
                var = DoubleVar(value=weekdata.data[j][i])  # initial value
                self.spinbox = Spinbox(master, from_=0, to=10, width=5, command = self.spinCallBack, textvariable=var)
                self.spinbox.grid(row=j+1, column=i+1)
                self.spinboxs.append(self.spinbox)
                

    # Comand function when spinbox change
    # If spinbox change, read the new data and input into weekdata
    def spinCallBack(self):
        # Refress all of the data
        spin_index = chunks(range(len(self.spinboxs)), len(weekdata.weekDays))
        for (j, event) in enumerate(weekdata.foodEvents):
            for (i, day) in enumerate(weekdata.weekDays):
                weekdata.data[j][i] = self.spinboxs[spin_index[j][i]].get()

        with open("week"+str(year)+str(week_num)+"_data.pkl", 'wb') as output:
            pickle.dump(weekdata, output, pickle.HIGHEST_PROTOCOL)

        
           


        

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
    my_gui = MainGUI(root, weekdata)
    root.mainloop()
        