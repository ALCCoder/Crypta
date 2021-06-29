'''

'''
from laba3 import gf256, rijndael
from processing import check_correct_lab3


def pol_form_proc(jsdata):
    #
    values_list = jsdata['values_list']

    val, err = check_correct_lab3.check_pol(values_list)
    if err is None:
        return gf256.to_polynom_form(val)
    return err


def bin_pol_form_proc(jsdata):
    #
    values_list = jsdata['values_list']

    pol1, pol2, err = check_correct_lab3.check_pol_mult(values_list)
    if err is None:
        return gf256.to_polynom_form(gf256.mul(pol1, pol2))
    return err


def mult_inverse_proc(jsdata):
    #
    values_list = jsdata['values_list']

    val, err = check_correct_lab3.check_pol(values_list)
    if err is None:
        res = gf256.inv(val)
        return f'{gf256.to_polynom_form(res)} ({bin(res)[2:]})'
    return err


def encode_file(mgnt, data_file_name, res_file_name):
    #
    with open(data_file_name, 'rb') as f:
        open_text = f.read()
    close_text = mgnt.encode(open_text)
    with open(res_file_name, 'wb') as f:
        f.write(close_text)


def decode_file(mgnt, data_file_name, res_file_name):
    #
    with open(data_file_name, 'rb') as f:
        close_text = f.read()
    open_text = mgnt.decode(close_text)
    with open(res_file_name, 'wb') as f:
        f.write(open_text)


def rijndael_proc(data_file_name, res_file_name, key, c0, mode, block_len, check_ed):
    #
    if check_ed == 'enc':
        func = encode_file
    else:
        func = decode_file

    rij = rijndael.Rijndael(key, block_len)

    if mode == 'ecb':
        rij_mode = rijndael.ECB(rij)
    elif mode == 'cbc':
        rij_mode = rijndael.CBC(rij, c0)
    elif mode == 'cfb':
        rij_mode = rijndael.CFB(rij, c0)
    elif mode == 'ofb':
        rij_mode = rijndael.OFB(rij, c0)

    func(rij_mode, data_file_name, res_file_name)
