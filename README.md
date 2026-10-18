# How to run

### Task 1:

Use `python task1.py <source> <destination>` OR use `python task1.py <source>` for default destination.

### Task 2 and 3:

Just run python file normally.

# Sorting algorithm comparison and time complexity

| Algorithm | Best case | Average and worst case |
|---|---|---|
| Insertion sort | O(n) | O(n²) |
| Merge sort | O(n log n) | O(n log n) |
| Timsort | O(n) | O(n log n) |

Insertion sort is usually much slower on larger random and reversed arrays because its average and worst-case complexity is O(n²).

Merge sort scales better with O(n log n) complexity.

Insertion sort and Timsort can be fast on already sorted data.

Timsort usually performs best because it uses existing ordered parts of the data and combines ideas from insertion sort and merge sort.

#### For normal Python programs, sorted() or list.sort() is usually the best choice.