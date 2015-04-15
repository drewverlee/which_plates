WhichPlates
===================================================

WhichPlates minimizes the amount of weight lifted during the plate 
changing process by choosing the optimal plates to load

Providing a bit more context, 'which plates' helps someone lifting weights 
choose which weight lifting plates to load. Essential, it's a better "warm up 
Calculator". Why Better? WhichPlates has a number of advantages:

* If your plates can't possible be combined to reach a weight, it picks the nearest weight possible.
* It tells you how to load you plates in such a way as to minimize the amount of weight lifted.

To illustrate the second point here is a comparison between several
plate loading algorithms:

Comparing plate loading algorithms:
=================================================

| example | heuristic | cost |
|---------|-----------|------|
| 1       | greedy    | 15   |
| 2       | None      | 30   |
| 3       | A*        | 10   |

The Examples are outlined below in detail. The take away from this is that
WhichPlates saves you energy for what you really need it for "Lifting 
more weight at one time". It also saves you the mental energy of having to
worry about this problem.

The Heuristic
=====================================================
Whats novel (what I discovered) is that their is a simple Heuristic for
the A*Search algorithm that allows for a 'fast enough' solution to the problem
described above.

The Heuristic is as follows:

    *((current_goal - total_weight_on_bar) + total-weight-removed-from-the-bar)*

Once we have chosen the node that best fits this criteria, we expand this path.
To expand the path we consider all plates we could add to the bar
whose weight plus the weight of those already on the bar is less then our current goal.

Setup for examples
===================================================
Before we look at an in example, lets make the process some what easier to visualize
on paper.

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

Check the table at the top for a comparison of the three examples/algorithms.

so that's is. Feel free to use this idea in your next fitness app.

