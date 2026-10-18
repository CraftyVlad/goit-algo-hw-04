import random
import timeit


def insertion_sort(a):
    a = a.copy()

    for i in range(1, len(a)):
        x = a[i]
        j = i - 1

        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x

    return a


def merge_sort(a):
    if len(a) < 2:
        return a

    middle = len(a) // 2
    left = merge_sort(a[:middle])
    right = merge_sort(a[middle:])
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


for n in [100, 500, 1000]:
    data = [random.randint(0, n) for _ in range(n)]
    datasets = [
        ("RANDOM", data),
        ("SORTED", sorted(data)),
        ("REVERSED", sorted(data, reverse=True)),
    ]

    for data_name, values in datasets:
        print(f"\n{data_name}, array size: {n}")
        for name, sort in [
            ("insertion sort", insertion_sort),
            ("merge sort", merge_sort),
            ("timsort", sorted),
        ]:
            time = timeit.timeit(lambda: sort(values), number=1)
            print(f"{name}: {time:.6f} s")