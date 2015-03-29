import timeit
from collections import Counter

from state import State, Action

def test_timed_runs():
    N = 1
    times = []
    for n in range(N):
        time = timeit.timeit(
            """
            from a_star_search import a_star_search;
            from priority_que import PriorityQue;
            from conftest import states;
            a_star_search(states()[{n}], PriorityQue);
            """.format(n=n))
        times.append(time)
        print(time)

    print(times)




