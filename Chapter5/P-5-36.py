# Redesign the CaesarCipher class as a subclass of the SubstitutionCipher from the previous problem.
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

class CaesarCipher(SubstitutionCipher):

    def __init__(self,str,shift):
        super().__init__(str) # initialize class base
        self._shift = shift

    def Caesar(self):
        self._forward = str
        decoder = [None]*26
        for k in range(26):
            decoder[k] = chr((k - self._shift) % 26 + ord("A"))
        self._backward = ''.join(decoder)

if __name__ in "__main__":
    str = "DBCOEFGJIHKLXNAQPRSTUVWZYM"
    strr = str[::-1]
    cipher = CaesarCipher(strr,3)
    message = "BAIBEY IS MY LOVELY ADORABLE LITTLE CAT."
    coded = cipher.encrypt(message)
    print("Secret: ", coded)
    answer = cipher.decrypt(coded)
    print("Message:", answer)
