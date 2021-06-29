'''

'''

from processing import check_correct_lab1
from laba1 import bit_operations, vernam, RC4, des


def get_bit_proc(jsdata):
    #
    values_list = jsdata['values_list']

    val, bit, err = check_correct_lab1.check_bit(values_list)
    if err is None:
        return bin(bit_operations.get_bit_k_pos(val, bit))[2:]
    return err


def change_bit_proc(jsdata):
    values_list = jsdata['values_list']

    val, bit, err = check_correct_lab1.check_bit(values_list)
    if err is None:
        return bin(bit_operations.change_bit_k_pos(val, bit))[2:]
    return err


def swap_bits_proc(jsdata):
    values_list = jsdata['values_list']

    val, i_bit, j_bit, err = check_correct_lab1.check_swap_bits(values_list)
    if err is None:
        return bin(bit_operations.swap_bits(val, i_bit, j_bit))[2:]
    return err


def zero_bits_proc(jsdata):
    values_list = jsdata['values_list']

    val, m, err = check_correct_lab1.check_zero_bits(values_list)
    if err is None:
        return bin(bit_operations.zero_bits(val, m))[2:]
    return err


def splice_bits_proc(jsdata):
    values_list = jsdata['values_list']

    val, i, err = check_correct_lab1.check_spmid_bits(values_list)
    if err is None:
        return bin(bit_operations.splice_bits(val, i))[2:]
    return err


def middle_bits_proc(jsdata):
    values_list = jsdata['values_list']

    val, m, err = check_correct_lab1.check_spmid_bits(values_list)
    if err is None:
        return bin(bit_operations.get_middle_bits(val, m))[2:]
    return err


def change_bytes_proc(jsdata):
    values_list = jsdata['values_list']

    val, rearr, err = check_correct_lab1.check_change_bytes(values_list)
    if err is None:
        return bin(bit_operations.change_bytes_order(val, rearr))[2:]
    return err


def max_pow_proc(jsdata):
    values_list = jsdata['values_list']

    val, err = check_correct_lab1.check_pow_range(values_list)
    if err is None:
        return bit_operations.max_div_pow2(val)
    return err


def xor_all_bits_proc(jsdata):
    values_list = jsdata['values_list']

    val, err = check_correct_lab1.check_xor_all_bits(values_list)
    if err is None:
        # !!! Error
        return bit_operations.xor_all_bits(val, 32)
    return err


def within_range_proc(jsdata):
    values_list = jsdata['values_list']

    val, err = check_correct_lab1.check_pow_range(values_list)
    if err is None:
        return bit_operations.within_range(val)
    return err


def change_bits_proc(jsdata):
    values_list = jsdata['values_list']

    val, rearr, err = check_correct_lab1.check_change_bits(values_list)
    if err is None:
        return bin(bit_operations.transpose_bits(val, rearr))[2:]
    return err


def cycle_shift_left_proc(jsdata):
    values_list = jsdata['values_list']

    val, n, p, err = check_correct_lab1.check_cycle_shift(values_list)
    if err is None:
        return bin(bit_operations.cycle_shift_left(
            val & ((1 << p) - 1), n, p))[2:]
    return err


def cycle_shift_right_proc(jsdata):
    values_list = jsdata['values_list']

    val, n, p, err = check_correct_lab1.check_cycle_shift(values_list)
    if err is None:
        return bin(bit_operations.cycle_shift_right(
            val & ((1 << p) - 1), n, p))[2:]
    return err


def vernam_proc(data_file_name, key_file_name, res_file_name):
    #
    with open(data_file_name, 'rb') as f_data:
        data_bytes = f_data.read()

    with open(key_file_name, 'rb') as f_key:
        key_bytes = f_key.read()

    if len(data_bytes) != len(key_bytes):
        raise Exception('Error')

    res = vernam.vernam(data_bytes, key_bytes)

    with open(res_file_name, 'wb') as f_res:
        f_res.write(res)


def rc4_proc(data_file_name, key_file_name, res_file_name):
    with open(data_file_name, 'rb') as f_data:
        data_bytes = f_data.read()

    with open(key_file_name, 'rb') as f_key:
        key_bytes = f_key.read()

    rc4 = RC4.RC4()

    res = rc4(data_bytes, key_bytes)

    with open(res_file_name, 'wb') as f_res:
        f_res.write(res)
