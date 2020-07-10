import datetime

my_date = datetime.date.today()
year, week_num, day_of_week = my_date.isocalendar()

class WeekClass:
    def __init__(self, foodEvents=[
        "Zöldség", "Gyümölcs", "Gabona", "Hús", "Friss hal",
        "Belsöség", "Burgonya", "Édesség", "Magvak", "Üditő",
         "Sport"],
         weekDays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
        weekMin = [0,  0,  0, 0,  1,  0, 0, 0, 3, 0, 15],
        weekMax = [28,14, 21, 14, 14, 2, 3, 2, 3, 2, 50]):

        self.weekyear = year
        self.weekNumber = week_num
        self.foodEvents = foodEvents
        self.weekMin = weekMin
        self.weekMax = weekMax
        self.weekDays = weekDays
        self.data = [[0] * len(weekDays) for i in range(len(foodEvents))]
        
     