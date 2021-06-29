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


def check_pol(values_list):
    # 1, 3
    if not check_empty_values(values_list):
        return return_error(1, 'Empty field')

    val = values_list[0].strip()

    if len(val) > 8:
        return return_error(1, 'Error: len > 8 (not GF256)')

    try:
        val = int(val, 2)
    except:
        return return_error(1, 'Error value')

    return (val, None)


def check_pol_mult(values_list):
    # 1, 3
    if not check_empty_values(values_list):
        return return_error(2, 'Empty field')

    val1 = values_list[0].strip()
    val2 = values_list[1].strip()

    try:
        pol1 = int(val1, 2)
        pol2 = int(val2, 2)
    except:
        return return_error(2, 'Error value')

    return (pol1, pol2, None)
