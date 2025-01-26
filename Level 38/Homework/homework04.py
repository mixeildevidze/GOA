def correct(s):
    corrected_text = []
    for char in s:
        match char:
            case '5':  
                corrected_text.append('S')
            case '0':  
                corrected_text.append('O')
            case '1':
                corrected_text.append('I')
            case _:  
                corrected_text.append(char)
    
    return ''.join(corrected_text)
