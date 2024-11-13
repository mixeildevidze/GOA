def manual_append(lst, item):
    new_list = []  

    for element in lst:
        new_list.append(element)  

    new_list += [item]  
    return new_list