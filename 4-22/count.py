from collections import defaultdict, Counter


def count(word):
    count_d = {}
    for i in word:
        if i in count_d:
            count_d[i] += 1
        else:
            count_d[i] = 1

    return count_d


def count_default(word):
    count_dd = defaultdict(int)
    for i in word:
        count_dd[i] += 1

    return count_dd


word = 'harrypotter'
print(count(word))
print(count_default(word))
print(Counter(word))
