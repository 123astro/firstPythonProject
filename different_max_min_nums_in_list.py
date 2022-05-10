num_list = [199, 23, -100, 2, 8, 100]


def difference_max_min(lst):
    num_high = num_list[0]
    num_low = num_list[0]
    # for loop starts comparing index 1 with index 0
    for count, x in enumerate(lst, start=1):
        if x < num_low:
            num_low = x
        if x > num_high:
            num_high = x
    num_dif = num_low - num_high
    print(abs(num_dif))


difference_max_min(num_list)
