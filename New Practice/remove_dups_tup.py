def remove_dups_tuples(arr):
    seen = set()
    result = []
    for tup in arr:
        if tup not in seen:
            seen.add(tup)
            result.append(tup)
    return result