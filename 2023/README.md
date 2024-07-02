# Advent Of Code 2023
This was my first attempts at the advent of code puzzles.

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
11-1 - 14 mins  
11-2 - 28 mins  
12-1 - 1 hour 16 mins  
12-2 - DNF -- see reflection  
13-1 - 2 hours 47 mins  
13-2 - 5 days, 2.5 day break inbetween   
14-1 - 13 mins  
14-2 - 15 mins 45s  
15-1 - 7 min 40s  
15-2 - 20 mins 5s  
16-1 - 36 min 35s  
16-2 - 10 min 15s  
17-1 - 6 hours, 3.5 hour break  
17-2 - 51 mins  
18-1 - 58 mins  
18-2 - 23 mins 15s  
19-1 - 37 mins 25s  
19-2 - 1 day  
20-1 - 2 hours  
20-2 - 2 hours
21-1 - 25 mins
21-2 - 6 hours 30 mins (3+hours of break)
22-1 - 2 hours 40 mins  
22-2 - 2 hours (read question 2 hours before beginning though)  
23-1 - 31 mins  
23-2 - 1 hour 38 mins  
24-1 - 37 mins  
24-2 - 3 days
25-1 - 3 hours

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
### 13-2
I need to be more precise with my line of thinking when implementing. I redid my code maybe 3-4 times, each time a new mistake would crop up that I have to go in to patch. The issue I resolved last was present in every prior attempt for 13-2, despite my remaking of every line a few times. I did not need to use others' solutions/ideas in the end, but I did go to reddit for extra test inputs. This one felt like such a huge mental block because the final solution is not inherently difficult.
### 14-1
Finishing this fast is a real confidence booster after 13-2. I basically used bubble sort, comparing only '.' and 'O'. Not too complicated, luckily.
### 14-2
Well making me do the same thing 4 billion times is sure to result in brute force not working. However, in my spite I realised that after some time, the total load at the end of one cycle drops into a repeating pattern. I tested the math to figure out which number in the pattern I have on the example input, which worked, then went straight to the full input. It did not take very long to reach the repeating pattern, and from there I calculated the answer. Not exactly a satisfying method to get the answer, however.
### 15-1
Implementing a hashing algorithm, quite simple in contrast to some of the days that came before this.
### 15-2
Honestly, I took a little too long understanding what the question wanted. Implementation was not particularly difficult, a couple of errors that could quickly be spotted and fixed with the example input. Happy about day 15 overall.
### 16-1
Setting up the functions in hope it helps for part 2, but my code got the correct answer first try again today, which is a win to me. I did have to increase the maximum recursion depth as I hit the limit. 
### 16-2
At least I only have to repeat the same thing 12100 times, not a billion. Setting everything as a recursive function definitely sped up the process, I just had to ensure the states were not being reused, and started from a blank slate each time. A little ugly copy pasting for each direction later, I had the answer.
### 17-1
I got spoilt by reddit in knowing today's puzzle intended to use djikstra's algorithm. I was browsing day 16 memes too, how unfortunate. I do not know if I would have thought of using djikstra by myself, but knowing to use djikstra made my thinking very simple. I spent around 1.5 hours trying to implement, getting spaghettier and spaghettier code, then decided I needed a break. Afterwards, I came back and could solve it fairly quickly with some debugging.
### 17-2
What in the overthinking. I literally only needed to change 3 lines, add 1 line and indent a few others. Honestly, should never have taken this long and certainly could have been done in 5 minutes.
### 18-1
This was not that bad. I spent a bunch of time thinking how to most efficiently get the answer, then eventually settled on the easiest to code method. As long as it is correct I suppose. Technically speaking my code would not work on every input, and would require a small adjustment on other inputs.  
<img src="./lavalagoon.png" width="200">  
Picture of my input's lava lagoon  
### 18-2
Of course, break brute force by making you do the same thing but much too many times more. I did think about the shoelace method the for part 1, but somehow figured that would be more work. It was not. My part 2 is of course much more optimised that part 1 as a result. For some reason though, the perimeter was only half counted, not sure about the maths behind that.
### 19-1
I took my time to plan out how everything should function, and that paid off in a simple coding and debugging process, obtaining the answer fairly quickly. I did not feel stuck or lost, which is a positive.
### 19-2
I had the right idea at first, but completely wrong execution. When dealing with ranges, always have your variables record both the start and end, not just one side of it. It then took many hours of debugging, including forgetting to alter a for loop to account for the (now necessary) last item. Frustrating.
### 20-1
Learnt a new thing about python classes that would have saved some trouble -- variables such as dictionaries are shared for all instances of the same class if initialised outside of class functions. Other than that, some faffing about was necessary, and unexpectedly did not find any cycle.
### 20-2
Brute force would really have been impossible -- a casual 229 trillion button presses. My final answer is not a general solution, it requires one to break the input into parts manually. I did check with reddit regarding the method as I wanted to know I was on the right track before scanning the input by hand, and it seems the majority used such a tactic. 5 more days.
### 21-1
A simple BFS algorithm settled this puzzle. Not a stranger to BFS in AOC, and I suspect the next part may ask the man to walk a billion steps or something similar.
### 21-2
Well it was similar to walking a billion times. But 26 million steps in an infite plane. Figured out most of the math, but required external help to cross the line. Most of the issue was in forgetting to account for the offset in starting position (middle rather than 0,0). This was largely a math issue rather than a coding issue for me.
### 22-1
Spending an hour+ debugging only to spot that a single '==' should actually be '=' is fun. I took my time with this one, not coding anything for the first half an hour or so to work out the ideas in my head. Went relatively smoothly
### 22-2
I think this was frustrating because I knew the right concepts but failed to implement efficiently. I took a wrong approach that required dynamic programming, which I did not implement, then waited for the (slower) output to tell me I was wrong. My final approach should have been the one I took from the start, it is simpler and more direct. I needlessly overcomplicated earlier.
### 23-1
Quite happy with this, small simple maze solving algorithm. Luckily the input isn't too large, although I might be stubborn and wait for it to be solved.
### 23-2
Did I attempt to allow the previous algo to do its thing, after discounting the 'v' and '>'s? Yes. Would it have taken forever? Also yes. I spent 45+ minutes waiting on it and also testing optimisations, before deciding it might be worth to pursue an alternative route. Using the junctions instead of the individual paths is much faster, considering there were only 36 junctions but 9000 paths. Overall, today was good as this was finished relatively quickly.
### 24-1
This was just maths, luckily. I took a bit of time to process the question and work out the maths. Programming wise, I need to remember to account for edge cases. Thats about it. Can't wait to have to deal with 3D equations for part 2
### 24-2
This was super frustrating because I knew it was a maths question and I knew I had the knowledge from A levels to solve it. However, I never came across a good, easy solution by myself. I kept thinking to break the given vectors into individual x, y, and z thinking it would make it easier to calculate or simplify. Instead, the simplest solution relies on properties of vectors and conditions of the question. I guess I avoided thinking about vectors and their properties because I have forgotten how to apply them. This sucked.
### 25-1
I knew this was a graph problem, and the problem statement did all but explicitly state this. I thought there would be something to do with cycle detection, or making an undirected graph to find SCCs, or something similar. Eventually, I could not come up with a single solution. That was disappointing. I implemented another person's idea based on their explanation, without referring to any code.
