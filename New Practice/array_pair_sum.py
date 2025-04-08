def find_pairs(arr, target):
    """
    finds all unique pairs in an array that sum up to a given target

    Args:
        arr: the input array
        target: the target sum

    Returns:
        a llist of tuples representing pairs
    """

    seen = set()
    pairs = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)
    return list(pairs)

array = [1, 2, 3, 4, 5, 6, 7, 8]

target_sum = 10

pairs = find_pairs(array, target_sum)

print(pairs)
