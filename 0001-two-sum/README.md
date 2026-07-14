# 1. Two Sum

**Difficulty:** Easy

**Language:** python3

## Approach

 Iterate through the list while storing each number's index in a hash map (dictionary). For each element, compute the complement (target - num) and check if this complement already exists in the map. If found, return the pair of indices; otherwise, add the current number and its index to the map.

## Complexity

- **Time Complexity:** O(n) – each element is processed once and dictionary look‑ups are O(1) on average.
- **Space Complexity:** O(n) – in the worst case the dictionary stores all n elements.

## Topics

 Hash Table, Array, Dictionary
