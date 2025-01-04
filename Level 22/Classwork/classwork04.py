def get_average(marks):
    if not marks:
        return 0  
    
    return sum(marks) // len(marks)