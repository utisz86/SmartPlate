import sys

def test(successful_test):
    """ The print of test results.    """
    sorszam = sys._getframe(1).f_lineno
    if successful_test:
        msg = "The row of {0}. passed successfully.".format(sorszam)
    else:
        msg = ("The row of {0}. FAILED.".format(sorszam))

    print(msg)

def test_sets():
    """ Run the test set for this module. """
    test(abs(-5) == 5)
    #
    testWeek = WeekClass(foodEvents=["Zöldség", "Gyümölcs", "Gabona"], weekDays =["Monday","Tuesday","Wednesday","Thursday"] )
    test(testWeek.data == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    testWeek = WeekClass()

class WeekClass:
    

    def __init__(self, foodEvents=["Zöldség", "Gyümölcs", "Gabona", "Hús", "Friss hal","Belsöség", "Édesség", "Magvak", "Üditő", "Sport", "Súly"], weekDays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]):
        self.foodEvents = foodEvents
        self.weekDays = weekDays
        self.data = [[0] * len(weekDays) for i in range(len(foodEvents))]
        

test_sets()        