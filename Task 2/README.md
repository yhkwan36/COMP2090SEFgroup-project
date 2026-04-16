# COMP2090SEF Self-study Project

## Features

### Hash Table
- Separate chaining for collision resolution
- Automatic resizing when load factor exceeds 0.7
- All standard ADT operations: `insert`, `get`, `delete`, `contains`, `size`
- Average time complexity: **O(1)**

### Quicksort
- In-place divide-and-conquer sorting
- Lomuto partition scheme
- Average time complexity: **O(n log n)**

## How to Run

### Prerequisites
- Python 3.6 or higher
- No external libraries required

### Quick Start
1. Clone or download the python file.
2. Open your terminal/command prompt.
3. Navigate to the project folder.
4. Run the demo.py

When you run demo.py, you should see the following output:

=== HASH TABLE DEMO ===

HashTable contents: [[['apple', 1]], [], [['elderberry', 5]], [['cherry', 3]], [['banana', 2], ['date', 4]], [['fig', 6]]]
get('banana') = 2
contains('fig') = True
size() = 6
After deleting cherry, size = 5

=== QUICKSORT DEMO ===

Original: [10, 7, 8, 9, 1, 5]
Sorted: [1, 5, 7, 8, 9, 10]

## What This Output Shows

Hash Table: Successfully inserts 6 items (triggers automatic resizing), handles collisions, and performs lookup, membership check, and deletion correctly.
Quicksort: Correctly sorts the input array in-place.

## References
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to algorithms.* MIT Press.
