# 9. Palindrome NumberSolved

**Difficulty:** Hard

**Language:** python3

## Approach

 The function first rejects negative numbers as non‑palindromes. It stores the original value, then builds the reversed integer by repeatedly extracting the last digit (x % 10), appending it to a running reverse (reverse = reverse * 10 + digit), and discarding the processed digit (x //= 10). After the loop finishes, it compares the reversed number with the original to decide if the input is a palindrome.

## Complexity

- **Time Complexity:** O(d) where d is the number of digits in x (equivalently O(log₁₀ n)), because each digit is processed once in the while loop.
- **Space Complexity:** O(1) – only a few integer variables are used regardless of input size.

## Topics

 Math, Number Theory, Arithmetic Operations, Loop
