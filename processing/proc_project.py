'''

'''

from project import cbc, cfb, ecb, ofb


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

def magenta_proc(data_file_name, res_file_name, key, c0, mode, check_ed):
    #
    if check_ed == 'enc':
        func = encode_file
    else:
        func = decode_file

    if mode == 'ecb':
        mgnt_mode = ecb.ECB(key)
    elif mode == 'cbc':
        mgnt_mode = cbc.CBC(key, c0)
    elif mode == 'cfb':
        mgnt_mode = cfb.CFB(key, c0)
    elif mode == 'ofb':
        mgnt_mode = ofb.OFB(key, c0)

    func(mgnt_mode, data_file_name, res_file_name)
