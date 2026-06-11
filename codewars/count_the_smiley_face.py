def count_smileys(arr):
    count = 0
    for smile in arr:
        if len(smile) <= 3:
            if check_smile(smile):
                count += 1
    return count
            

def check_smile(smile):
    length = len(smile)
    
    eyes = [":",";"]
    nose = ["-", "~"]
    mouth = [")", "D"]
    
    if length == 3:
        if (smile[0] in eyes) and (smile[1] in nose) and (smile[2] in mouth):
                return True
    if length == 2:
        if smile[0] in eyes and smile[1] in mouth:
                return True
    return False