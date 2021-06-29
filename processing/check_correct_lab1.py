'''

'''


def check_length_32(s: str) -> bool:
    #
    return len(s) <= 32


def check_empty(s: str) -> bool:
    #
    return len(s) > 0


def check_empty_values(values):
    #
    for val in values:
        if not check_empty(val):
            return False
    return True


def return_error(param_count, error):
    '''
    Return tuple with (None * param_count, error)
    Primer: return_error(2, 'Index out of range') -> (None, None, 'Index out of range')
    '''
    return tuple((None for _ in range(param_count))) + (error,)


def check_bit(values_list):
    # 1, 2
    if not check_empty_values(values_list):
        return return_error(2, 'Empty field')

    val1 = values_list[0].strip()
    val2 = values_list[1].strip()

    if len(val1) > 32:
        return return_error(2, 'Error value length (max 32)')

    try:
        val = int(val1, 2)
        bit = int(val2)
    except:
        return return_error(2, 'Error value')

    if bit < 1 or bit > 32:
        return return_error(2, 'Index out of range (1 <= index <= 32)')

    return (val, bit, None)


def check_swap_bits(values_list):
    # 3
    if not check_empty_values(values_list):
        return return_error(3, 'Empty field')

    val1 = values_list[0].strip()
    val2 = values_list[1].strip()
    val3 = values_list[2].strip()

    try:
        val = int(val1, 2)
        i_bit = int(val2)
        j_bit = int(val3)
    except:
        return return_error(3, 'Error value')

    if i_bit < 1 or i_bit > 32:
        return return_error(3, 'Index out of range (1 <= index <= 32)')

    if j_bit < 1 or j_bit > 32:
        return return_error(3, 'Index out of range (1 <= index <= 32)')

    return (val, i_bit, j_bit, None)


def check_zero_bits(values_list):
    # 4
    if not check_empty_values(values_list):
        return return_error(2, 'Empty field')

    try:
        val = int(values_list[0], 2)
        m = int(values_list[1])
    except:
        return return_error(2, 'Error value')

    return (val, m, None)


def check_spmid_bits(values_list):
    # 5, 6
    if not check_empty_values(values_list):
        return return_error(2, 'Empty field')

    val1 = values_list[0].strip()
    val2 = values_list[1].strip()

    try:
        val = int(val1, 2)
        m = int(val2)
    except:
        return_error(2, 'Error value')

    if len(val1) <= 2 * m:
        return return_error(2, 'Error: too big i')

    return (val, m, None)


def check_change_bytes(values_list):
    # 7
    if not check_empty_values(values_list):
        return return_error(2, 'Empty field')

    try:
        val = int(values_list[0], 2)
        rearr = [int(num) for num in values_list[1]]
    except:
        return return_error(2, 'Error value')

    for el in rearr:
        if el < 1 or el > 4:
            return return_error(2, 'Index out of range (1 <= inde <= 4)')

    return (val, rearr, None)


def check_pow_range(values_list):
    # 8, 9
    if not check_empty_values(values_list):
        return return_error(1, 'Empty field')

    try:
        val = int(values_list[0])
    except:
        return return_error(1, 'Error value')

    return (val, None)


def check_xor_all_bits(values_list):
    # 10
    if not check_empty_values(values_list):
        return return_error(1, 'Empty field')

    try:
        val = int(values_list[0], 2)
    except:
        return return_error(1, 'Error value')

    return (val, None)


def check_change_bits(values_list):
    # 11
    if not check_empty_values(values_list):
        return return_error(2, 'Empty field')

    try:
        val = int(values_list[0], 2)
        rearr = [int(num) for num in values_list[1]]
    except:
        return return_error(2, 'Error value')

    return (val, rearr, None)


def check_cycle_shift(values_list):
    # 12, 13
    if not check_empty_values(values_list):
        return return_error(3, 'Empty field')

    try:
        val = int(values_list[0], 2)
        n = int(values_list[1])
        p = int(values_list[2])
    except:
        return return_error(3, 'Error value')

    return (val, n, p, None)
