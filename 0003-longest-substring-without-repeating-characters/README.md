# 3. Longest Substring Without Repeating CharactersSolved

**Difficulty:** Hard

**Language:** python3

## Approach

 The algorithm uses a sliding‑window (two‑pointer) technique. It iterates with a right pointer over the string, storing each character's most recent index in a hash map. When a repeated character is found whose last occurrence lies within the current window, the left boundary is moved just past that previous occurrence. After each step the window size (right‑left+1) is used to update the maximum length of a substring without repeats.

## Complexity

- **Time Complexity:** O(n) – each character is processed at most twice (once by the right pointer and once when the left pointer jumps forward).
- **Space Complexity:** O(min(n, m)) – the hash map stores at most one entry per distinct character, where m is the size of the character set (e.g., 128 for ASCII).

## Topics

 Sliding Window, Hash Table, Two Pointers, String, Dictionary
