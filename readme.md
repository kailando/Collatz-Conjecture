# CollatzConjecture.py
### What is the Collatz Conjecture (3x+1)?
3x+1 is a **infamous maththimatics problem** among mathmaticians. The 3x+1 statement is that ***every* seed** will eventually reach & get stuck in a `4, 2, 1, 4, 2, 1` loop.
*Note:  The 3x+1 statement is not true for negative numbers. There are 3 loops in the negative side of the number line.*
### How do I calculate the 3x+1 number sequence?
Take any number. Say, 7.
Now, the 3x+1 rule is "If the current number is odd, multiply it by 3 and add 1. If it's even, divide by 2.". 
The progression for the seed is `7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1`.

### The 2 methods to prove it wrong
We *think* that every number as a seed will eventually get stuck in the `4, 2, 1, ...` loop. But, there are 2 methods to *possibly* prove it wrong / contradict it.

#### Method #1: Shoots up to infinity
Method #1 is to find a number sequence that shoots up to infinity and never comes down. It will be a contradiction because it will never reach 4, 2, or 1.

#### Method #2: Find another loop
Method #2 is to find a number sequence that has a different loop than the `4, 2, 1, ...` loop and never ends up in it. If so, it will contradict the 3x+1 rule because of the same reson as Method #1.

### Links
[3x+1 (regular)](./main.py)
[3x+1 (shortened)](./main.shortened.py)
[En Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture)
[De Wikipedia](https://de.wikipedia.org/wiki/Collatz-Problem)
[Es Wikipedia](https://es.wikipedia.org/wiki/Conjetura_de_Collatz)
[Fr Wikipedia](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse)
[It Wikipedia](https://it.wikipedia.org/wiki/Congettura_di_Collatz)
### To do:
1. Plotting
2. Tables(s)
   
   A. Seed/Next (3x+1) table
   
   B. Agent table
   
4. Agent
   
   A. Agent brain
   
   B. Agent read/write to table(s)
