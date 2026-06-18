def cakes(recipe, available):
    
    for rkey in recipe.keys():
        if rkey not in available:
            return 0
            
    array = []
    for akey, aval in recipe.items():
        for bkey, bval in available.items():
            if akey == bkey:
                count = 0
                while bval >= aval:
                    bval -= aval
                    count += 1
                array.append(count)
    return min(array)