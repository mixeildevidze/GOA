def manual_max(listn):
    
    max_num = listn[0]

    for i in listn:
        if max_num < i:
            max_num = i

    return max_num