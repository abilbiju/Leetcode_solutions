# 5. Longest Palindromic SubstringSolved

**Difficulty:** Hard

**Language:** python3

## Approach

 The solution uses dynamic programming. It builds an n×n boolean table where matrix[i][j] indicates whether the substring s[i..j] is a palindrome. Single characters are marked true, then length‑2 substrings are checked. For longer substrings, it checks if the end characters match and the inner substring (i+1, j-1) is a palindrome. Whenever a palindrome is found, it updates the answer indices. Finally it returns the substring defined by the stored indices.

## Complexity

- **Time Complexity:** O(n^2) – the double loop over all possible start indices i and length differences diff visits each pair (i, j) once.
- **Space Complexity:** O(n^2) – the DP matrix of size n×n is stored.

## Topics

 Dynamic Programming, String, Palindrome, DP Table, Substring
