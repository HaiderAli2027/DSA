# Two Pointer Technique

## Overview

Two Pointer is a search space reduction technique that uses two index
variables to scan a data structure — eliminating the need for nested
loops in many problems. Reduces time complexity from O(n²) to O(n).

---

## Three Core Patterns

### 1. Converging Pointers (Opposite Ends)

left = 0, right = n - 1
Move inward based on a condition.

When to use:

- Sorted array + pair/triplet with target sum
- Palindrome validation
- Maximum area / container problems

Template:
left, right = 0, len(arr) - 1
while left < right:
if condition_met(arr[left], arr[right]): # process answer
left += 1
right -= 1
elif need_larger:
left += 1
else:
right -= 1

---

### 2. Same Direction (Fast-Slow)

Both start at beginning, one moves faster.

When to use:

- In-place removal / partitioning
- Linked list middle or cycle detection
- Sliding window (when window condition is simple)

Template:
slow = 0
for fast in range(len(arr)):
if condition(arr[fast]):
arr[slow] = arr[fast]
slow += 1

---

### 3. Two Array Pointers

One pointer per array, both move forward.

When to use:

- Merge two sorted arrays
- Intersection or union of sorted arrays
- Compare two sequences

Template:
i, j = 0, 0
while i < len(a) and j < len(b):
if a[i] == b[j]: # process match
i += 1; j += 1
elif a[i] < b[j]:
i += 1
else:
j += 1

---

## Pattern Recognition Signals

| Problem Signal                              | Pattern                 |
| ------------------------------------------- | ----------------------- |
| Sorted array + find pair with sum X         | Converging              |
| Remove duplicates / partition in-place      | Fast-Slow               |
| Palindrome check                            | Converging              |
| Two sorted arrays merge/intersect           | Two Array               |
| Linked list cycle                           | Floyd's Fast-Slow       |
| Subarray with sum/length condition          | Sliding Window variant  |
| Brute force is two nested loops, same array | Converging or Fast-Slow |

---

## The Invariant Rule

Every correct two pointer solution has an invariant — a property that
remains true throughout all pointer movements. Before coding, state
your invariant explicitly.

Example (Two Sum II):
Invariant: The answer pair, if it exists, always lies within
[left, right]. We never move a pointer in a direction that
could skip the answer.

If you cannot state the invariant, your movement logic is likely wrong.

---

## Complexity

Time: O(n) — each pointer traverses array at most once
O(n log n) if sorting is required as a preprocessing step
Space: O(1) — only index variables, no extra structures

---

## Prerequisite Knowledge

- Array indexing
- Sorting (for problems requiring sorted input)
- Linked list node traversal (for Floyd's pattern)

---

## Problem List (Sorted by Difficulty)

| #   | Problem                           | Pattern    | Difficulty |
| --- | --------------------------------- | ---------- | ---------- |
| 1   | LC 167 - Two Sum II               | Converging | Easy       |
| 2   | LC 344 - Reverse String           | Converging | Easy       |
| 3   | LC 26 - Remove Duplicates         | Fast-Slow  | Easy       |
| 4   | LC 15 - 3Sum                      | Converging | Medium     |
| 5   | LC 11 - Container With Most Water | Converging | Medium     |
| 6   | LC 75 - Sort Colors               | 3 Pointers | Medium     |
| 7   | LC 977 - Squares of Sorted Array  | Converging | Easy/Med   |
| 8   | LC 42 - Trapping Rain Water       | Converging | Hard       |
| 9   | LC 141/142 - Linked List Cycle    | Floyd's    | Med/Hard   |

---

## Common Mistakes

1. Moving both pointers when only one should move
2. Off-by-one in while condition (< vs <=)
3. Not handling duplicates in 3Sum (causes duplicate triplets)
4. Applying two pointer to unsorted data without sorting first
5. Defining no invariant — solution works on examples but fails edge cases

---

## Interview Tips

- Always state the brute force first, then explain why two pointer
  eliminates the redundancy
- Verbalize your pointer movement logic: "I move left because..."
- For 3Sum and beyond, reduce to Two Sum as a subproblem
- Two pointer + sorting is a very common combo — O(n log n) total,
  accepted in most interviews
- If the problem involves a linked list and asks for cycle/middle
  without extra space, Floyd's is the expected answer
