'''
Разработать приложение, шифрующее и дешифрующее файл с помощью
алгоритма Вернама.
'''

import random

def generate_key(ln: int)->bytearray:
    '''Generate key with len as open_text'''

    key = bytearray()
    for _ in range(ln):
        key.append(random.randint(0, 255))
    return key

def vernam(text: bytearray, key: bytearray)-> bytearray:
    '''
    Return bytes decrypt with key.
    '''
    if len(text) != len(key):
        raise Exception('len(text) != len(key)!')

    res_text = bytearray()
    for i, byte in enumerate(text):
        res_text.append(byte ^ key[i])

    return res_text

if __name__ == "__main__":
    s = 'hsjdbcsdHJBEJFNjksdnvjJNl'
    print(s)

    key = generate_key(len(s))
    close = vernam(s.encode('utf-8'), key)

    with open('Enycrypted_File.txt', 'wb') as file:
        file.write(close)

    with open('Enycrypted_File.txt', 'rb') as file:
        res_s = str(vernam(file.read(), key), encoding='utf-8')

    print(res_s)
    # with open('Enycrypted_File.txt', 'w') as file:
    #     file.write(res_s)


