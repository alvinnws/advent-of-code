# Advent-Of-Code 2023

This repository contains my (unoptimised, messy) solutions to the Advent Of Code 2023 by Eric Wastl.

The website can be found [here](https://adventofcode.com/)

My goal with my solutions is not to necessarily have the most optimised answer, but rather to come up with something that works. I am taking this to challenge my problem solving and programming abilities rather than looking to maximise absolute performance.

## Timings:
1-1 and 1-2 - ~10 mins (estimated, did not record timing)  
2-1 and 2-2 - ~20 mins (estimated, did not record timing)  
3-1 and 3-2 - ~30 mins (estimated, did not record timing)  
4-1 - 15 mins  
4-2 - 10 mins  
5-1 - 1 hour  
5-2 - 1 hour 53 mins  
6-1 - 26 mins   
6-2 - 5 mins  
7-1 - 46 mins  
7-2 - 26 mins  
8-1 - 15 mins  
8-2 - 2 hours  
9-1 - 12 min 15s  
9-2 - 1 min 46s  
10-1 - 26 mins  
10-2 - 2 hours 4 mins  
11-1 - 14mins
11-2 - 28mins
12-1 - 1 hour 16 mins
12-2 - DNF -- see reflection
13-1 - 2 hours 47 mins

## Reflections:  
### 4-2
I spent a ridiculous amount of time debugging when in reality I had entered in the answer wrong at first. Final timing was about 25 mins but I had the answer in 10 mins.  
### 5-1
Wow, brute force was not the way. Final time was 59 mins, which is nuts. Using ranges to find my answer was quicker by at least a few hours.
### 5-2 
I had the right method quite quickly, but an uncaught mistake caused me to hunt for a fix in the wrong direction for the longest time. To improve I should review the entire code when the output is incorrect. Even the simplest "cannot be wrong" lines. I attempted brute force here and there, taking more than 10 minutes per run.  
Curiously, my method now obtains the answer in under 400 seeds tested, but continues to add to the queue millions more seeds. I am unsure what the issue could be.
### 6-1
I realised almost immediately as I was reading the puzzle that using a quadratic formula would be ideal. I did some quick googling for rounding up and down, as I used completing the square to solve the quadratic, which in most cases would leave decimals, but created my own simple rounding to fit the question best.
### 6-2
I'm glad I used math rather than brute force, got the correct answer on the first try.  
Day 6 was much easier than day 5.
### 7-1
I would presume there are much better design choices to have taken, unfortunately I ended up recreating bubble sort to sort the hands. Fortunately the computation time remained under 1s.
### 7-2
Oh if it isn't the consequences of my actions. To fit my code from 7-1, I needed to hardcode the effects of all the jokers. This was time consuming but I still got the answer without much issues.
### 8-1
Seemed really direct, spent more time on understanding what the question wanted to be honest. At first read I thought it would be a shortest path type of question, but nevertheless solved fairly quickly
### 8-2
Quick mod of 8-1 code produces a brute force method that would take a casual 300 hours to compute. While initially waiting for the brute force method, I was scrolling online to check that it SHOULD take quite a while, not knowing precisely how long, I came across a comment that hinted at the intended solution. "Think about cycles", yet that comment was enough to get me to change my entire strategy. I'm not sure if I would have thought about it without external assistance, but I'll not look online for the next puzzles.
### 9-1 and 9-2
Super happy with the timing and code complexity. I knew instantly from generating new lines that a recursive function would be ideal. Lucky that part 2 only required changing a few *characters*.
### 10-1
This one was decent, I roughly knew what to do and took my time to implement, getting the correct answer on my first try (after debugging)
### 10-2
I got my ass kicked, struggling for over an hour not knowing what or how to do. I did find an upper limit for the answer by counting the number of characters not part of the main pipe loop AND existing with a direct path to any edge. Eventually, I looked for hints, being pointed to Pick's Theorem and the Shoelace formula. The shoelace formula I had learnt in secondary school, but dismissed it at the time in favour of another method for maths, but I had never heard of Pick's Theorem and would never have come close to it. This is just part of the learning process I suppose
### 11-1
Fairly straightfoward. I am certain I did not use the most efficient method but the answer is correct on the first try anyway
### 11-2
Well a quick mod to continue bruteforcing is... not ideal to say the least. Fortunately, I quickly came up with an alternative and spent more time debugging than implementing. Biggest takeaway is to keep track of my columns and rows (x and y) better. The mixups definitely took a chunk of my time.
### 12-1
Took some time to think on how to do this, ended up bruteforcing by testing all permutations. Created a function to check for validity of each permutation, after testing was 100% accurate. During the second part I swapped it for RegEx, which is what is present now. No effect on function.
### 12-2
Dynamic Programming and Memoization. I need to learn better how to take advantage of such cases especially with recursive functions. Brute forcing would take at minimum 24 hours, if not much more. I consider this as a DNF despite collecting the star as I searched online for a solution that I remade after understanding it. On one hand I feel like I could have done better, not looking at solutions. On the other hand, I have never used dynamic programming before, and so I had never thought about how it works/how to use it. I did come across a method which seemingly does not use dynamic programming, 
### 13-1
Initially had a lot of issues with the code, realising that I cannot be checking for a palindrome line by line. Instead, I needed to check all the lines at the same time. From there, it was an issue of being usure what the input expected, whether or not a mirror could be ON a row/column. e.g. `.#.`, should I return 0 or 1? I adjusted right detection but not left and that stumped my debug for 20 minutes more.