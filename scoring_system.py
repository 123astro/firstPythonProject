def calculate_scores(scores):
    count_a = 0
    count_b = 0
    count_c = 0
    for x in scores:
        if x == "A":
            count_a = count_a + 1
        if x == "B":
            count_b = count_b + 1
        if x == "C":
            count_c = count_c + 1
    all_scores = [count_a, count_b, count_c]
    print(all_scores)


calculate_scores("AABBBCCCB")
