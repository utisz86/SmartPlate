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


test_sets()
