def two_sum(numbers, target):
    """
    Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, 
    when added together, give the target value. The indexes of these items should then be returned in a tuple / list (depending on your language) like 
    so: (index1, index2).

    For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.
    
    The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be positive or negative integers; target 
    will always be the sum of two different items from that array).
    
    Based on: https://leetcode.com/problems/two-sum/
    
    two_sum([1, 2, 3], 4) # returns (0, 2) or (2, 0)
    two_sum([3, 2, 4], 6) # returns (1, 2) or (2, 1)
    """
    
    index1 = 0
    index2 = 0
    
    for i, o_num in enumerate(numbers):
        for j, s_num in enumerate(numbers[1::]):
            if s_num + o_num == target:
                if i - j != 1 :
                    index1 += i
                    index2 += j+1

                    return (index1,index2)
