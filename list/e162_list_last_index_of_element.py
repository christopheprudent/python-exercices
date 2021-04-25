# https://stackoverflow.com/questions/522372/finding-first-and-last-index-of-some-value-in-a-list-in-python
def rindex(lst, value):
    for i, v in enumerate(reversed(lst)):
        if v == value:
            return len(lst) - i - 1  # return the index in the original list
    return None

# web solution
def last_occurrence(l, ch):
    return ''.join(l).rindex(ch)

if __name__ == '__main__':
    print('liste {}, dernier élément {} : {}'.format([1, 2, 3], 3, rindex([1, 2, 3], 3)))
    print('liste {}, dernier élément {} : {}'.format(['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c'], 'f', rindex(['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c'], 'f')))
    print('liste {}, dernier élément {} : {}'.format(['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c'], 'w', last_occurrence(['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c'], 'w')))
