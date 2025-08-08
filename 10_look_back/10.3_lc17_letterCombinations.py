import copy

num_mapping = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

def letterCombinations(digits):
    """
    100%&5%
    :param digits:
    :return:
    """
    num_mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    num = len(digits)
    result = []
    # s = ''
    def backtrack(my_digits, my_index):
        if my_index == num:
            result.append(copy.deepcopy())
            return
        # for i in range(digits):
        digit = my_digits[my_index]
        string_letter = num_mapping[digit]
        for i in string_letter:
            s += i
            backtrack(my_digits, my_index + 1)
            s = s[:-1]

    s = ''
    backtrack(digits, 0)
    return result






