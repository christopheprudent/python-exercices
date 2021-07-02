def classify_number(x):
    _positive = _negative = _zero = 0
    if x > 0:
        _positive += 1
    elif x < 0: 
        _negative += 1
    else:
        _zero += 1

    return _positive, _negative, _zero

L = [1, -2, 9, 0, -10, 2, 3, -4, 0]
print('liste', L)
print('part des éléments positifs, négatifs et nuls')
result = list(map(classify_number, L))
positives = sum(map(lambda x:x[0], result)) / len(L)
negatives = sum(map(lambda x:x[1], result)) / len(L)
zeros = sum(map(lambda x:x[2], result)) / len(L)
print(round(positives, 2), round(negatives, 2), round(zeros, 2))
