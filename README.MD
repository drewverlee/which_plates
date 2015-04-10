The Heuristic
=====================================================
Whats novel (what I discovered) is that their is a simple Heuristic for
the A*Search algorithm that allows for a 'fast enough' solution to the problem
described below.

The Heuristic is as follows. We consider all plates we could add
whose weight plus the weight of those on the bar is less then our current goal.
But we choose to pursue the path with the minimal:

    *((current_goal - total_weight) + total weight-removed-from-the-bar)*


Stating the problem
===================================================
The goal is to minimize the amount of 'un-necessary' weight lifted.
un-necessary weight is any weight that was lifted in putting weight on the 
bar or taking it off.


Setup
===================================================
Before we look at an in example lets, make the math some what easier:

were going to cut the goal weight and number of plates in half. 
so for example, a goal weight of 50 with plates [25, 25] would just be
goal = 25, with plates = [25]

were also going to set our bar weight equal to 0
and we have to decide how to visualize the bar:

    [----- we take weight off the right side of the bar --> ]

so if we have a bar like [25, 15, 5] and we want to remove the top plate we get '5'.

Now for our example:

    goal weight = 200/2 = 100
    bar weight = 0

so then, say you want to lift 100, the sensible thing to do is to warm up
at weights less then 100. So then we really want to lift 20 then 40 then 60 then
80 then finally our goal 100:

    [20, 40, 60 ,80, 100]

and say you have the following plates:

    Two of each of the following weights/plates [2.5, 5, 10, 15, 25, 35, 45]

Example 1
===================================================
Here is a perfectly natural way to load the weights:

    [15, 5]                                   = goal 20
    [15, 5, 15, 5]                            = goal 40
    [15, 5, 15, 5, 10, 10]                    = goal 60

we have to remove a plate now: - 10

    [15, 5, 15, 5, 10, 25, 2.5, 2.5]          = goal 80

we have to remove some more plates... -5

    [15, 5, 15, 5, 10, 25, 25]                = final goal 100

in total we had to move 15 off the bar, not bad? 

  
Example 2
===================================================
here is another way to have loaded the bar

    [10, 10]                              = goal 20
    [10, 10, 15, 5]                       = goal 40
    [10, 10, 15, 5, 15, 5]                = goal 60

have to remove some weight -5

    [10, 10, 15, 5, 15, 25]               = goal 80

we have to remove weight again... -25

    [10, 10, 15, 5, 15, 45]               = final goal 100

in total we removed 30 pounds, twice as bad as our first attempt.


The question is, could we have done better then the first attempt? The first
attempt is actual fairly intelligent, its greedy, it chooses the largest 
weight possible at each step only removing when it has to.
But we can do better?

Example 3 
==================================================
  
    [5, 10, 5] = goal 20

thats not a conventional start, and to make it weirder were going to take off a 5 lb
right now (-5) before we even have to...

    [5, 10, 25] = goal 40
    [5, 10, 25, 15, 5] = goal 60

now we take off another 5 before moving on...

    [5, 10, 25, 15, 25] = goal 80
    [5, 10, 25, 15, 25, 15, 5] = final goal 100

in total we removed 10!


Lets compare:
=================================================

| example | heuristic | cost |
|---------|-----------|------|
| 1       | greedy    | 15   |
| 2       | None      | 30   |
| 3       | A*        | 10   |

What's more, example 3 is *provable* the best you can do 
(though we wont do that here).

so that's is. Feel free to use this idea in your next fitness app.
