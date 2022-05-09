names = [False, False, False, False, False, ]


def count_true(lst):
    count = 0
    for x in lst:
        if x.__eq__(True):
            count = count + 1
    print(count)

count_true(names)
