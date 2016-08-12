#### Pair Problem

| 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| o |   |   |   | x |

Above is a gameboard of length 4. You start your coin at position 0 and you want to end at position 4. You have N moves. In each move, you have two options, One space forward or stay put. And you can never step outside the board. And at the end of your last move, you want to be at the last square.

Given a board of length M and N moves, calculate the number of possible solutions.

For the example above, M = 4. Let's say N = 5. Then we have,

    FFFFS
    FFFSF
    FFSFF
    FSFFF
    SFFFF
    
That gives a total of 5 solutions.

Write a two functions "def Way(n,m)" and "def Way2(n,m)" that would return the number of possible solutions. One is without recursion and the other with recursion.

This problem is not trivial. So take your time to think, talk and work it out.