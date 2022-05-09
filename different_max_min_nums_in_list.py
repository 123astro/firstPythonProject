num_list = [10, 4, -50, 2, 8, 91]


def difference_max_min(lst):

    num_low = num_list[0]
    num_high = num_list[0]
    for x in lst:
        if x < num_low:
            num_low = x
        if x > num_low:
            num_high = x
    num_dif = num_low - num_high
    print(num_low)
    print(num_high)
    print(abs(num_dif))


difference_max_min(num_list)
