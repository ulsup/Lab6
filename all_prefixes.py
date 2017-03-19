def all_prefixes(ryadok):
    '''
    Lays words to prefixes and returns a set of the parts.
    '''
    a = list(ryadok)
    lst = []
    lst.append(ryadok)
    while len(a) > 1:
        del a[-1]
        lst.append(''.join(a))
    lst.sort()
    return set(lst)
