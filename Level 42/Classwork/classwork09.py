def maskify(s):
    return s if len(s) <= 4 else '#' * (len(s) - 4) + s[-4:]