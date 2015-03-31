import timeit
from collections import Counter

from state import State, Action

MAX_ALLOWED_SECONDS = 1

def test_timed_runs():
    N = 1
    times = []
    for n in range(N):
        time = timeit.timeit(
            """
            from a_star_search import a_star_search;
            from priority_queue import PriorityQueue;
            from conftest import states_for_timming;
            a_star_search(states_for_timming()[{n}], PriorityQueue);
            """.format(n=n), number=5)
        times.append(time)


    for time in times:
        assert time < MAX_ALLOWED_SECONDS
    
def test_with_large_problem_should_run_in_under_5_seconds():
    time = timeit.timeit("""
        from a_star_search import a_star_search;
        from priority_queue import PriorityQueue;
        from conftest import state_start_large;
        a_star_search(state_start_large(), PriorityQueue)""", number=5)

    assert time < MAX_ALLOWED_SECONDS




