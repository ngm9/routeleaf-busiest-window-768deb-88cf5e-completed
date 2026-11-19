# RouteLeaf Busiest Window

## Task Overview

RouteLeaf is a local grocery-delivery startup that records how many orders were delivered on each day. The planning team wants to know the busiest stretch of exactly k consecutive days so it can schedule extra riders for similar periods next season.

Implement `busiest_window(deliveries: list[int], k: int) -> int`. The function receives the daily delivery counts in date order and the window length `k`, and returns the largest total number of deliveries over any `k` consecutive days.

## Examples

**Example 1:**

**Input:** `deliveries = [4, 2, 7, 1, 8, 3], k = 2`

**Output:** `11`

**Explanation:** The last two days total 8 + 3 = 11, which is the largest sum of any two consecutive days.

**Example 2:**

**Input:** `deliveries = [4, 2, 7, 1, 8, 3], k = 3`

**Output:** `16`

**Explanation:** The three days 7 + 1 + 8 = 16 give the largest sum of any three consecutive days.

**Example 3:**

**Input:** `deliveries = [5], k = 1`

**Output:** `5`

**Explanation:** There is only one day, so its count is the only possible window total.

**Example 4:**

**Input:** `deliveries = [0, 0, 0], k = 3`

**Output:** `0`

**Explanation:** Every day has zero deliveries, so the only window total is 0.

## Constraints

- `1 <= k <= len(deliveries) <= 10^5`
- `0 <= deliveries[i] <= 10^4`
- The window must consist of exactly `k` consecutive days.
- When `k` equals the number of days, the only window is the whole list.
- There is always at least one day, so there is always exactly one correct answer.

## How to Verify

- Implement the function in `solution.py`; do not change its name or signature.
- Run `pytest` from the repository root; all tests must pass.
- Your solution is also run against additional hidden tests, including large inputs that run under a time limit.
- Use only the Python standard library.
