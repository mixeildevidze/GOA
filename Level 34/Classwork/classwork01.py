def manual_map(func,cvladi):
    result = []
    for item in cvladi:
        result.append(func(item))
    return result