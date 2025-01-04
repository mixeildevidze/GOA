def find_short(s):
    words = s.split()
    
    l = min(len(word) for word in words)
    
    return l