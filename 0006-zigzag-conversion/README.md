# 6. Zigzag ConversionSolved

**Difficulty:** Unknown

**Language:** python3

## Approach

 The function first handles trivial cases where the number of rows is 1 or exceeds the string length, returning the original string. It then creates an array of empty strings for each row. While iterating over the characters of the input, it appends each character to the current row, toggles the traversal direction when the top or bottom row is reached, and moves the current row index accordingly. After processing all characters, it concatenates the row strings to produce the final zigzag-converted result.

## Complexity

- **Time Complexity:** O(n) – each character of the input string is visited exactly once.
- **Space Complexity:** O(n) – additional storage for the row strings and the final output together hold all characters of the input.

## Topics

 String manipulation, Simulation, Array, Greedy approach, Zigzag pattern
