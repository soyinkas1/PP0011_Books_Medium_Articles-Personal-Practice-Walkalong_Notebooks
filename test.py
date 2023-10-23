import sys


def test(did_pass):
    """ Print the results of a test"""
    linenumber = sys._getframe(1).f_lineno  # Get the caller's line number
    if did_pass:
        msg = 'Test at the line {0} ok'.format(linenumber)
    else:
        msg = 'Test at the line {0} FAILED'.format(linenumber)
    print(msg)
