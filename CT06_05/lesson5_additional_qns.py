1) Centre-Aligned Number Pyramid (Wrap at 9)
-------------------------------------------
Write a program that prints a centre-aligned number pyramid of height n.

Each row:
- Is centred using spaces
- Prints numbers starting from 1
- Wraps around after 9 (e.g. 10 → 0, 11 → 1)

Example (n = 6):
     1
    123
   12345
  1234567
 123456789
12345678901

Rules:
- No if / else
- Nested for loops allowed


2) Diamond Number Pattern
-------------------------
Write a program that prints a diamond using numbers.

Example (n = 4):
   1
  123
 12345
1234567
 12345
  123
   1

Rules:
- No if / else
- Nested for loops allowed


3) Multiplication Grid
----------------------
Write a program that prints an n × n multiplication grid.

Example (n = 5):
1  2  3  4  5
2  4  6  8 10
3  6  9 12 15
4  8 12 16 20
5 10 15 20 25

Rules:
- No if / else
- Nested for loops allowed


4) Staircase of Powers
----------------------
Write a program that prints the following pattern.

Row r should print the first r powers of r.

Example (n = 4):
1
2 4
3 9 27
4 16 64 256

Rules:
- No if / else
- Nested for loops allowed


5) Palindrome Number Pyramid
----------------------------
Write a program that prints a centre-aligned palindrome number pyramid.

Example (n = 4):
   1
  121
 12321
1234321

Rules:
- No if / else
- Nested for loops allowed

1) Alternating Weighted Sum
---------------------------
Write a program that calculates the following value for a given n:

1×1 + 2×2 + 3×3 + ... + n×n

Then print the final total.

Example:
If n = 4
Total = 1 + 4 + 9 + 16 = 30

Rules:
- Use a for loop
- No if / else
- Accumulate the total inside the loop


2) Cumulative Product-Sum
-------------------------
Write a program that calculates the following sum:

(1×2) + (2×3) + (3×4) + ... + (n×(n+1))

Example:
If n = 4
Total = (1×2) + (2×3) + (3×4) + (4×5)
      = 2 + 6 + 12 + 20
      = 40

Rules:
- Use a for loop
- No if / else


3) Running Accumulated Growth
-----------------------------
A number starts at 1.

For each step i from 1 to n:
- Multiply the number by i
- Add the result to a running total

Finally, print the total.

Example:
If n = 4
Step values: 1, 2, 6, 24
Total = 1 + 2 + 6 + 24 = 33

Rules:
- Use a for loop
- No if / else
- Use variables to track both the running product and total

