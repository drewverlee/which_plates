import pytest
from pprint import pprint as pp
from collections import Counter
from main import main

def test_main():
    plates = Counter({45:2, 35:2, 25:2, 15:2, 10:2, 5:2, 2.5: 2})
    goal = 100
    path = main(goal, plates)
    # goals should be 20, 40, 60, 80, 100
    pp(path)
    assert path == 'i have no idea thats why i wrote a program'

    

