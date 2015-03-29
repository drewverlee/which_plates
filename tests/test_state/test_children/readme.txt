tests for States children method

Were going to walk through the steps of a simple A*problem
checking the children along the way. In order to do this were going to
need to check the various states along the way. Which is what our fixtures
setup below. We choose a problem thats linear in fashion, so that
each state only has one child state.

State  action   bar   goal 
0      '',[]    []    0
1      +, [20]  [20]  0
2      l, [20]  [20]  1
3      -, [20]  []    1
4      +, [25]  [25]  1
5      l, [25]  [25]  2
