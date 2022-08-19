# Implement a class, SubstitutionCipher, with a constructor that takes a string with the 26 uppercase letters in an arbitrary order and uses that for the forward mapping for encryption (akin to the self._forward string in CaesarCipher class). You should derive the backward mapping from the forward version.
import string

class SubstitutionCipher:

    def __init__(self,str):
        "Construct cipher with an arbitrary 26 uppercase letters string."
        alphabet = string.ascii_uppercase
        encoder = list(str)
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
    str = "DBCOEFGJIHKLXNAQPRSTUVWZYM"
    strr = str[::-1]
    cipher = SubstitutionCipher(strr)
    message = "BAIBEY IS MY LOVELY ADORABLE LITTLE CAT."
    coded = cipher.encrypt(message)
    print("Secret: ", coded)
    answer = cipher.decrypt(coded)
    print("Message:", answer)
