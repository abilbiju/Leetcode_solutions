# 2. Add Two Numbers

**Difficulty:** Unknown

**Language:** python3

## Approach

 The function iterates through the two input linked lists digit by digit, adding corresponding node values together with any carry from the previous addition. For each sum it creates a new ListNode containing the digit (sum % 10) and updates the carry (sum // 10). A dummy head node simplifies list construction; the resulting list is returned starting from dummy.next. The loop continues while there are remaining nodes in either list or a non‑zero carry.

## Complexity

- **Time Complexity:** O(max(n, m)) – each node of the longer list is visited exactly once, where n and m are the lengths of l1 and l2.
- **Space Complexity:** O(max(n, m)) – a new linked list of at most max(n, m) + 1 nodes is allocated for the result; auxiliary variables use O(1) extra space.

## Topics

 Linked List, Two Pointers, Simulation, Arithmetic, Data Structures
