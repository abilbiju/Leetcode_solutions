# 4. Median of Two Sorted ArraysSolved

**Difficulty:** Hard

**Language:** python3

## Approach

 The solution first ensures that nums1 is the shorter array, then performs a binary search on its possible partition index i. For each i it computes the complementary partition j = half_len - i in nums2. It adjusts i until the partition satisfies the condition that every element on the left side (max of nums1[i-1] and nums2[j-1]) is less than or equal to every element on the right side (min of nums1[i] and nums2[j]). Once the correct partition is found, the median is derived from the maximum left element and the minimum right element, handling odd and even total lengths separately.

## Complexity

- **Time Complexity:** O(log min(m, n)) – binary search is performed on the smaller array of length m (or n), halving the search space each iteration.
- **Space Complexity:** O(1) – only a constant amount of extra variables are used regardless of input size.

## Topics

 Binary Search, Arrays, Divide and Conquer, Median of Two Sorted Arrays, Partitioning
