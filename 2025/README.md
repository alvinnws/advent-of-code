# 2025

For this year, as I am overseas and attempting the challenges without fixed schedule or discipline, I will not be taking time or attempting fast solves.

### Day 1
I thought there would be an optimised route for 1-2 using modulo and floor division, but I meddled with it for too long and decided it was not worth the effort.
### Day 2
Slightly more challenging than day 1, although it took less time. 2-2 was made much easier by use of functions.
### Day 3
2 digit numbers were easy to handle for part 1, for part 2 I had to be a little more creative and search from the right towards the left.
### Day 4
A classic AOC problem involving 2D maps, easy to figure out the surrounding 8 blocks. For part 2, added another loop and deleted rolls as we went.
### Day 5
This one messed with me as I initially kept the integer ranges in a dictionary. No idea why, but using a list was better as identical lower bounds create new ranges regardless, rather than overriding. Part 2 was straightforward as I just had to simplify the ranges and do a little math.
### Day 6
Don't know why I was quirky with the grand_total var name, but I did feel like it. Not too bad this day, just needed to mentally flip the whole file on part 2 to solve.
### Day 7
Accidentally solved part 2 before solving part 1 by misinterpreting the task at hand. Left my solution as is, so 07-2 is shorter than 07-1. Fantastic
### Day 8
What started as a desire to make nice looking OOP code turned into ugly half-OOP half-functional code. I remembered the UFDS but forgot the implementation, only to improvise, fail and turn back to searching the implementation and frankensteining the result. Ouch.
### Day 9
Part 1 was easy enough, brute force and sort areas. Part 2... I couldn't make a working algo that fits the general case, so I started cheesing the problem by plotting the graph and observing patterns. I narrowed the possible points by eliminating cases which didnt fit the pattern, then sorted the remaining ~600 possible shapes visually. Plot each graph starting with the largest area, then take the first which does not exceed the boundary.  
The failed algo has been left in the part 2 code.
### Day 10
Part 1 was easy, part 2.... work in progress so lets pretend day 10 doesn't exist for now
### Day 11
Part 1 was a simple bfs, done plenty of prior days. Part 2's twist was that the path was much longer and that we needed to keep track of whether or not we visited these two devices. Track it as a state, then recursively call the function with memoization. The answer was much larger than I anticipated but goes to show how much more efficient the intended solution is.
### Day 12
I got spoiled to the true solution while procrastinating when it popped up on my reddit feed. I was about to brute force everything and I think I left the remainder in there.