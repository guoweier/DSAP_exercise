# Write a program that can perform Caesar cipher for English messages that inclue both upper- and lowercase characters.

class CaesarCipher:

    def __init__(self, shift):
        "construct Caesar cipher using given integer shift for rotation."
        encoder_u = [None]*26     # temp array for upper- and lowercase encryption
        decoder_u = [None]*26     # temp array for upper- and lowercase decryption
        encoder_l = [None]*26
        decoder_l = [None]*26
        for k in range(26):
            encoder_u[k] = chr((k + shift) % 26 + ord("A"))
            decoder_u[k] = chr((k - shift) % 26 + ord("A"))
            encoder_l[k] = chr((k + shift) % 26 + ord("a"))
            decoder_l[k] = chr((k - shift) % 26 + ord("a"))
        self._forwardu = ''.join(encoder_u)
        self._backwardu = ''.join(decoder_u)
        self._forwardl = ''.join(encoder_l)
        self._backwardl = ''.join(decoder_l)

    def encrypt(self, message):
        "Return string representing encripted message."
        return self._transform(message, self._forwardu, self._forwardl)

    def decrypt(self, secret):
        "Return decrypted message given encrypted secret."
        return self._transform(secret, self._backwardu, self._backwardl)

    def _transform(self, original, codeu, codel):
        "Untility to perform transformation based on given code string."
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord("A")
                msg[k] = codeu[j]
            if msg[k].islower():
                j = ord(msg[k]) - ord("a")
                msg[k] = codel[j]
        return ''.join(msg)

if __name__ in "__main__":
    cipher = CaesarCipher(1)
    message = "Baibey is my lovely adorable little cat. I, Weier Guo, love her very much."
    coded = cipher.encrypt(message)
    print("Secret: ", coded)
    answer = cipher.decrypt(coded)
    print("Message:", answer)
