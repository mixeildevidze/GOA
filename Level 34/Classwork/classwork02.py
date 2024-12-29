def manual_filter(func,cvladi):
    result = []
    for item in cvladi:
        if func(item):
            result.append(item)
    manual_filter()