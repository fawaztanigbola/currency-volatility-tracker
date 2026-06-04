def descending_order(num):

    """
    Your task is to make a function that can take any non-negative integer as an argument and return 
    it with its digits in descending order. Essentially, rearrange the digits to create the highest 
    possible number.

    Examples:
    Input: 42145 Output: 54421

    Input: 145263 Output: 654321

    Input: 123456789 Output: 987654321

    smiles....I completed this kata without joined and sorted

    def descending_order(num):
        if num < 0:
            return None
        
        sorted_digits = sorted(str(num), reverse=True)
        finNum = "".joined(sorted_digits)

        return int(finNum)
    """

    if num < 0:
        return
    if num == 0:
        return 0
    num = str(num)
    s_list = []
    for s_num in num:
        s_list.append(s_num)
    a_list = []
    for each in s_list:
        a_list.append(int(each))
    
    final_num = []
    while len(a_list) > 0:
        m_num = max(a_list)
        final_num.append(m_num)
        if len(a_list) != 0:
            a_list.remove(m_num)
    
    finNum = ""
    for number in final_num:
        finNum += str(number)
    return int(finNum)