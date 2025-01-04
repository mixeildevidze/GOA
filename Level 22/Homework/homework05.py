def get_middle(s):
    length = len(s)
    mid = length // 2
    
    if length % 2 == 0:  
        return s[mid-1:mid+1]  
    else:  # If the length is odd
        return s[mid]  