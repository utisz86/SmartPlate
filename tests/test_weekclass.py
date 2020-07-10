import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'Smartplate')))
from WeekClass import WeekClass
import datetime

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
    now = datetime.datetime.now()
    test(testWeek.weekyear == now.year)
    




test_sets()       