def count(s):
    words = s.split()
    freq = {}
    print(words)

    for w in words:
        if w in freq:
            freq[w]+=1
        else:
            freq[w]=1
    return freq

