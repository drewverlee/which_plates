import timeit
from collections import Counter

from state import _State, _Action

MAX_ALLOWED_SECONDS = 1

def test_timed_runs():
    N = 1
    times = []
    for n in range(N):
        time = timeit.timeit(
            """
            from a_star_search import _a_star_search;
            from priority_queue import _PriorityQueue;
            from conftest import states_for_timming;
            _a_star_search(states_for_timming()[{n}], _PriorityQueue);
            """.format(n=n), number=5)
        times.append(time)


    for time in times:
        assert time < MAX_ALLOWED_SECONDS
    
def test_with_large_problem_should_run_in_under_5_seconds():
    time = timeit.timeit("""
        from a_star_search import _a_star_search;
        from priority_queue import _PriorityQueue;
        from conftest import state_start_large;
        _a_star_search(state_start_large(), _PriorityQueue)""", number=5)

    assert time < MAX_ALLOWED_SECONDS





