def count(items):
    freq = {}

    for i in items:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

    