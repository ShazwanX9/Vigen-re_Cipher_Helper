"""
    VigenereCipher refer: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

    Required:
        string - key
        string - alphabet

    Examples:
        abc = "abcdefghijklmnopqrstuvwxyz"
        key = "password"
        c   = VigenereCipher(key, abc)

        c.encode(string) to encrypt
        c.decode(string) to decrypt
"""

class VigenereCipher:
    __doc__ = __doc__

    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.lenKey = len(key)
        self.lenAlphabet = len(alphabet)

        self.ref = {}
        prev = 0
        for ele in sorted(set(self.key)):
            for i in range(prev, self.lenAlphabet):
                if ele == self.alphabet[i]:
                    self.ref[ele] = i
                    prev = i + 1
                    break

    def __repr__(self):
        return "{:9s}: {}\n{:9s}: {}".format("Key", self.key, "Alphabet", self.alphabet)

    def encode(self, text):
        res = ""
        for i, letter in enumerate(text):
            if letter not in self.alphabet:
                res += letter
                continue
            res += self.alphabet[ (self.alphabet.index(letter) + self.ref[self.key[i%self.lenKey]]) % self.lenAlphabet ]
        return res
    
    def decode(self, text):
        res = ""
        for i, letter in enumerate(text):
            if letter not in self.alphabet:
                res += letter
                continue
            res += self.alphabet[ (self.alphabet.index(letter) + self.lenAlphabet - self.ref[self.key[i%self.lenKey]]) % self.lenAlphabet ]
        return res

if __name__ == "__main__":
    print(__doc__, "\n")
    print("Testing for " + __file__)

    abc = "abcdefghijklmnopqrstuvwxyz"
    key = "password"
    c   = VigenereCipher(key, abc)

    print("\n", c, sep='')
    print("c.encode('VigenereCipher')", "ViywjsihCihzaf", c.encode("VigenereCipher") == "ViywjsihCihzaf")
    print("c.decode('ViywjsihCihzaf')", "VigenereCipher", c.decode("ViywjsihCihzaf") == "VigenereCipher")