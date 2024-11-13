def alternate_case(text):
    result = ""
    for i in range(len(text)):
        if i % 2 == 0:
            result += text[i].lower()
        else:
            result += text[i].upper()
    return result

# Test case
text = "hello"
result = alternate_case(text)
print(result)