def programmers(one, two, three):
    num_list = [one, two, three]
    num_low = num_list[0]
    num_high = 0
    for x in num_list:
        if x < num_low:
            num_low = x
        if x > num_low:
            num_high = x
    num_dif = num_low - num_high
    print(abs(num_dif))


programmers(150, 300, 150)
