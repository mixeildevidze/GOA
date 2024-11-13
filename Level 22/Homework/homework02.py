def manual_replace(lst, old_value, new_value):
    new_list = [] 
    
    for item in lst:
        if item == old_value:
            new_list.append(new_value)  # თუ ელემენტი ემთხვევა old_value-ს, დაამატეთ new_value
        else:
            new_list.append(item)  # სხვაგვარად, დაამატეთ ელემენტი, როგორც არის

    return new_list