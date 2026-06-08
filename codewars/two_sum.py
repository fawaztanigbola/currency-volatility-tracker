def two_sum(numbers, target):
    
    index1 = 0
    index2 = 0
    
    for i, o_num in enumerate(numbers):
        for j, s_num in enumerate(numbers[1::]):
            if s_num + o_num == target:
                if i - j != 1 :
                    index1 += i
                    index2 += j+1

                    return (index1,index2)
