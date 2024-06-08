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
7-1 - 46mins  
7-2 - 26mins  

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
### 7-1
Oh if it isn't the consequences of my actions. To fit my code from 7-1, I needed to hardcode the effects of all the jokers. This was time consuming but I still got the answer without much issues.
