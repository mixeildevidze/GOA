words = ["cat", "house", "tree", "car"]
long_words = list(filter(lambda word: len(word) > 4, words))
print(long_words)