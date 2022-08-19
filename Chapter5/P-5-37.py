# Design a RandomCipher class as a subclass of the SubstitutionCipher from Exercise P-5.35, so that each instance of the class relies on a random permutation of letters for its mapping.

import string
import random

class SubstitutionCipher:

    def __init__(self):
        "Construct cipher with an arbitrary 26 uppercase letters string."
        alphabet = string.ascii_uppercase
        str = list(alphabet)
        random.shuffle(str)
        strr = ""
        for i in range(26):
            strr += str[i]
        encoder = list(strr)
        decoder = [None]*26
        for k in range(26):
            decoder[k] = alphabet[encoder.index(alphabet[k])]
        self._forward = str
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        "Return string representing encripted message."
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        "Return decrypted message given encrypted secret."
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        "Untility to perform transformation based on given code string."
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord("A")
                msg[k] = code[j]
        return ''.join(msg)


if __name__ in "__main__":
    cipher = SubstitutionCipher()
    message = "BAIBEY IS MY LOVELY ADORABLE LITTLE CAT."
    coded = cipher.encrypt(message)
    print("Secret: ", coded)
    answer = cipher.decrypt(coded)
    print("Message:", answer)
