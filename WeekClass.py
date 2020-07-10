import datetime

my_date = datetime.date.today()
year, week_num, day_of_week = my_date.isocalendar()

class WeekClass:
    def __init__(self, foodEvents=["Zöldség", "Gyümölcs", "Gabona", "Hús", "Friss hal","Belsöség", "Édesség", "Magvak", "Üditő", "Sport", "Súly"], weekDays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]):
        self.weekyear = year
        self.weekNumber = week_num
        self.foodEvents = foodEvents
        self.weekDays = weekDays
        self.data = [[0] * len(weekDays) for i in range(len(foodEvents))]
        
     