'''Реализуйте алгоритм RC4'''

#!/usr/bin/env python

class RC4:
    ''' '''
    def __init__(self):
        
        self._i = 0
        self._j = 0

    def __call__(self, text: bytearray, key: bytearray)->bytearray:
        ''' '''
        S = self._init_s_block(key)
        res_text = bytearray()

        self._i = 0
        self._j = 0

        for byte in text:
            res_text.append(self._generate_k(S) ^ byte)

        return res_text

    def _init_s_block(self, key):
        # random shuffle S
        keylength = len(key)
        S = list(range(256))
        j = 0
        for i in range(256):
            j = (j + S[i] + key[i % keylength]) % 256
            S[i], S[j] = S[j], S[i]  # swap
        return S

    def _generate_k(self, S):
        # Generate k on each step
        self._i = (self._i + 1) % 256
        self._j = (self._j + S[self._i]) % 256
        S[self._i], S[self._j] = S[self._j], S[self._i]  # swap

        k = S[(S[self._i] + S[self._j]) % 256]

        return k

if __name__ == '__main__':
    # test vectors are from http://en.wikipedia.org/wiki/RC4

    # ciphertext should be BBF316E8D940AF0AD3

    RC4 = RC4()
    key = 'Key'
    plaintext = 'Plaintext'

    encr_text = RC4(plaintext.encode('utf-8'), key.encode('utf-8'))
    print(encr_text)
    decr_text = RC4(encr_text, key.encode('utf-8')).decode('utf-8')

    print(decr_text)