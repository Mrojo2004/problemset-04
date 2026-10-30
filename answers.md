# CMPS 6610 Problem Set 04
## Answers

**Name:** Marcus Rojo


Place all written answers from `problemset-04.md` here for easier grading.




- **1d. (3 pts)**

File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length
----------------------------------------------------------------------
f1.txt    | 1,340                    | 826                | 0.616
alice29.txt    | 1,039,367                    | 676,374               | 0.651
asyoulik.txt    | 876,253            | 606,448               | 0.692
grammar.lsp    | 78,050                    | 56,206               | 0.720
fields.c    | 26,047                    | 17,356               | 0.666

Yes, there is a consistent trend. Huffman coding is cheaper than fixed-length coding on every file, consistently costing about 62-72% of the fixed-length cost. The savings are largest when a few characters account for most of the text. 

- **1e. (3 pts)** Equal frequency Huffman encoding cost.
If every character has the same frequency, Huffman then builds a balanced tree, meaning every character gets a code of around log₂|Σ| bits. The expected cost is about m * log₂|Σ|, where m is the number of characters in the document. When |Σ| is a power of 2, it equals the fixed-length cost. Otherwise it's slightly less, since some codes are ⌊log₂|Σ|⌋ bits and some are ⌈log₂|Σ|⌉.

It is consistent across documents. THe cost only depends on the alphabet size and the document's length rather than its content, and Huffman gives almost no savings over the fixed-length coding because there is no frequency imbalance to exploit. 


- **2a. (5 pts)** Construct a binary min-heap algorithm
First, treat the array as a binary tree (the children of index i are 2i+1 and 2i+2). Leaves are already heaps. With such, go from i = n/2 - 1 down to 0, and for each i, "sift down": swap A[i] with its smaller child if that child is smaller, and keep going until it's smaller than both children or if it hits a leaf. When i = 0 is finished, the whole array is a min-heap.

This is O(n) work because sifting down a node at height h costs O(h), and thre are at most n/2^(h+1) nodes at height h. Summing n/2^(h+1) * h over all heights gives O(n), and this is because the sum of h/2^h is at most 2. 



- **2b. (2 pts)** Span of your algorithm
Nodes at the same height have separate subtrees, so they can all be sifted down in parallel. Each height level takes O(h) span, and there are log n levels, so the total span is O(1 + 2 + ... + log n) = O(log^2 n).



- **3a. (3 pts)** Greedy algorithm for making change
Greedy algorithm: repeatedly take the largest coin 2^i that is less than or equal to the amount remaining, subtract it, and repeat until the remaining amount is 0. 

For i = k down to 0, take floor(N/ 2^i) coins of value 2^i, then set N = N mod 2^i.


- **3b. (3 pts)** Optimality proof
Greedy choice property: Let 2^j be the largest coin less than or equal to N. It is shown that some optimal soultion uses a 2^jcoin.

First, an optimal solution never uses tow coins of the same value 2^i with i < k, because two 2^i coins could be swapped for one 2^(i+1) coin, using fewer coins. In the case that an optimal soultion used no 2^j coin, it can't use any coin bigger than 2^j (those are bigger than N), so it only uses coins smaller than 2^j (each at most once). Their total is at most 2^0 + 2^1 + ... + 2^(j-1) = 2^j - 1 < N, so they can't add up to N as it is a contradiction. As a result, the optimal solution uses 2^j

Optimal structureL If S is an optimal set of coins for N and contains a coin c, then S minus c is optimal for N - c. If there were a smaller set S' for N - c, then S' plus c would make N with fewer coins that S, which would contradict that S is optimal. 

Together, these show that the greedy algorithm is optimal.



- **3c. (2 pts)** Work and span of your algorithm
Using division, we do a constant amount of work for each of the k+1 denominations, so the work is O(k). Each step depends on th eremainder from the previous step, meaning the span is also O(k).


- **4a. (2 pts)** Fortuito counter example proof
Counterexample: coins {1, 3, 4} and N=6.

Greedy takes the largest coin that fits: 4, then 1, then 1, for 3 coins. But 3 + 3 = 6 uses only 2 coins. As a result, greedy is not optimal. 


- **4b. (3 pts)** Optimal substructure property
Optimal substructure: Let OPT(n) be the fewest coins that sum to n.
If an optimal solution for n uses a coin of value D_i, then the remaining coins form an optimal soultion for n - D_i.

Proof: Suppose the remaining coins were not optimal for n - D_i. Then some smaller set S' makes n - D_i. Adding the D_i coin to S' makes n with fewer coins than th eoriginal soultion, which is a contradiction. 

As a result, this gives the recurrence:
OPT(0) = 0
Opt(n) = 1 + min over all D_i at most equal to n of OPT(n - D_i)
OPT(n) = infinity if no coin fits (meaning a change can't be made).



- **4c. (2 pts)** Fortuito dynamic programming algorithm
Bottom-up Dynamic Programming: make a table OPT[0...N]. Set OPT[0] = 0. For n = 1 to N, compute OPT[n] = 1 + min over all D_i <=  n of OPT[n - D_i] (infinity if none). If OPT[N] is infinity, then change evidently can't be made. To get the actual coin, store which D_i gave the min at each n and trace back from N.

Work: N table entries, each checks K demonimations, so O(Nk).
Span: each entry depends on earlier entries, so the N entries are computed in order, but the min over k coins can be done in parallel in O(log k).
So, as a result, the span is O(N log k).



- **5a. (4 pts)** Weighted task selection: Optimal substructure?
Yes, optimal substructure holds.
Sort the tasks by finish time and relabel them 1..n, so f_1 <= f_2 <= ... <= f_n. 
Let p(j) be the largest index i < j with f_i <= s_j (the last task that doesn't overlap task j), or 0 if there is none. Let OPT(j) be the max value using only tasks 1..j-1.

Claim: Let S be an optimal solution for tasks 1..j.
- if S contains task j, then S minus task j is optimal for tasks 1..p(j).
- if S doesn't contain task j, then S is optimal for tasks 1..j-1.

Proof: If S contains j, the rest of S can only use tasks that don't overlap j, which are tasks 1..p(j). If there were a better solution S' for tasks 1..p(j), then S' plus task j would beat S, which is a contradiction. If S doesn't contain j, it's a solution for tasks 1..j , and a better solution there would also beat S for tasks 1..j, which is also a contradiction. 


- **5b. (4 pts)** Does the greedy choice property hold?
No, the greedy choice property does not hold. The two greedy criteria that fail include:

1. Earliest finish time( the unweighted greedy from class):
    Tasks a = (0, 1, value 1) and b = (0, 10, value 100).
    Greedy picks a first (it finishes earliest), then b overlaps, so total = 1.
    Optimal picks b, and the total = 100.

2. Highest value first:
    Tasks a = (0, 10, value 10), b = (0, 5, value 6), c = (5, 10, value 6).
    Greedy picks a (highest value), then b and c overlap it, so total = 10.
    Optimal picks b and c, total = 12.



- **5c. (4 pts)** Dynamic programming algorithm for Weighted Task Selection
Dynamic programming algorithm:
1. Sort taks by finish time.
2. For each j, find p(j) with binary search over the finish times.
3. Opt(0) = 0, and for j = 1 to n:
   OPT (j) = max( v_j + OPT(p(j)), OPT(j-1) )
   (either take task j, or skip it).
4. The answer is OPT(n). To get the actual tasks, you trace back through which choice gave the max at each j.

Work: sorting is O(n log n), finding all p(j) is n binary searches, so O(n log n), and filling the table is O(n). Total work O(n log n).

Span: sorting can be done with O(log^2 n) span, and all p(j) binary searches are independent, so they run in parallel in O(log n). But each OPT(j) depends on OPT(j-1), so the table is filled one entry at a time: O(n).
Total span O(n).