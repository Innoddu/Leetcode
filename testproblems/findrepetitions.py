def max_consecutive_repetitions(short_s, long_s):
    if not short_s or not long_s:
        return 0
    
    idx = 0
    max_count = 0
    s_len = len(short_s)
    l_len = len(long_s)
    count = 0
    while idx <= l_len - s_len:

        if long_s[idx: idx + s_len] == short_s:
            count += 1
            idx = idx + s_len
        else:
            idx += 1
            max_count = max(max_count, count)
    
    return max_count


print(max_consecutive_repetitions("ABC", "ABCABCABCASABABABC"))