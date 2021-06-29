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


def check_val(values_list):
    # 1, 2, 3, 4
    if not check_empty_values(values_list):
        return return_error(1, 'Empty field')

    val = values_list[0].strip()

    try:
        val = int(val)
    except:
        return return_error(1, 'Error value')

    return (val, None)


def check_fast_pow_mod(values_list):
    # 5
    if not check_empty_values(values_list):
        return return_error(3, 'Empty field')

    val1 = values_list[0].strip()
    val2 = values_list[1].strip()
    val3 = values_list[2].strip()

    try:
        a = int(val1)
        b = int(val2)
        m = int(val3)

    except:
        return return_error(3, 'Error value')

    return (a, b, m, None)


def check_euclid(values_list):
    # 6, 7
    if not check_empty_values(values_list):
        return return_error(2, 'Empty field')

    val1 = values_list[0].strip()
    val2 = values_list[1].strip()

    try:
        a = int(val1)
        b = int(val2)
    except:
        return return_error(2, 'Error value')

    return (a, b, None)
