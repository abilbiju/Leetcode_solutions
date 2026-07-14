# 1. Two Sum

**Difficulty:** Easy

**Language:** python3

## Approach

 Iterate through the list while storing each number's index in a hash map. For each element compute the complement (target - num) and check if that complement is already in the map; if found, return the stored index and the current index. If not, add the current number and its index to the map.

## Complexity

- **Time Complexity:** O(n) – each element is processed once with constant‑time hash‑map lookups/inserts.
- **Space Complexity:** O(n) – in the worst case the hash map stores all n elements.

## Topics

 Hash Table, Dictionary, Array, Linear Scan
