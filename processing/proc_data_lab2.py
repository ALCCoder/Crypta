'''

'''
from laba2 import algebra, rsa_new
from processing import check_correct_lab2


def simple_numbers_proc(jsdata):
    # Здесь нужно выводить файлом !!!
    values_list = jsdata['values_list']

    val, err = check_correct_lab2.check_val(values_list)
    if err is None:
        return algebra.find_all_simple_divider(val)
    return err


def ded_system_proc(jsdata):
    #
    values_list = jsdata['values_list']

    val, err = check_correct_lab2.check_val(values_list)
    if err is None:
        return algebra.red_deduction_system(val)
    return err


def euler_function_proc(jsdata):
    #
    values_list = jsdata['values_list']

    val, err = check_correct_lab2.check_val(values_list)
    if err is None:
        return algebra.euler(val)
    return err


def decomposition_proc(jsdata):
    #
    values_list = jsdata['values_list']

    val, err = check_correct_lab2.check_val(values_list)
    if err is None:
        return algebra.factorization(val)
    return err


def fast_pow_mod_proc(jsdata):
    #
    values_list = jsdata['values_list']

    a, b, n, err = check_correct_lab2.check_fast_pow_mod(values_list)
    if err is None:
        return algebra.fast_pow_mod(a, b, n)
    return err


def euclid_alg_proc(jsdata):
    #
    values_list = jsdata['values_list']

    a, b, err = check_correct_lab2.check_euclid(values_list)
    if err is None:
        return algebra.euclid(a, b)
    return err


def bin_euclid_alg_proc(jsdata):
    #
    values_list = jsdata['values_list']

    a, b, err = check_correct_lab2.check_euclid(values_list)
    if err is None:
        a, b, c = algebra.euclid_ex_bin(a, b)
        return f'{a}, {b}, {c}'
    return err


def rsa_proc(data_file_name, key_file_name, res_file_name, mod):
    #

    if mod == 'enc':
        # Encode
        rs = rsa_new.RSA()
        arr = []
        with open(data_file_name, 'rb') as f:
            open_text = f.read()
            for i in range(0, len(open_text), 255):
                arr.append(open_text[i:i + 255])

        enc = bytearray()
        for a in arr:
            e = rs.encode(a)
            enc.extend(e)
        with open(res_file_name, 'wb') as f:
            f.write(enc)

        with open(key_file_name, 'wb') as f:
            f.write(rs.get_key()[0].to_bytes(256, byteorder='little'))
            f.write(rs.get_key()[1].to_bytes(256, byteorder='little'))
    else:
        rs = rsa_new.RSA()
        arr = []
        with open(data_file_name, 'rb') as f:
            close_text = f.read()
            for i in range(0, len(close_text), 256):
                arr.append(close_text[i:i + 256])

        # Read key
        with open(key_file_name, 'rb') as f:
            d = int.from_bytes(f.read(256), byteorder='little')
            n = int.from_bytes(f.read(256), byteorder='little')

        # Decode
        dec = bytearray()
        for a in arr:
            block = rs.decode(a, d, n)
            dec.extend(block)

        while dec[-1] == 0:
            del dec[-1]

        with open(res_file_name, 'wb') as f:
            f.write(dec)
