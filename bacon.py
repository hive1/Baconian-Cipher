class Bacon:
    lookup = {
        "a": "aaaaa",
        "b": "aaaab",
        "c": "aaaba",
        "d": "aaabb",
        "e": "aabaa",
        "f": "aabab",
        "g": "aabba",
        "h": "aabbb",
        "i": "abaaa",
        "j": "abaaa",
        "k": "abaab",
        "l": "ababa",
        "m": "ababb",
        "n": "abbaa",
        "o": "abbab",
        "p": "abbba",
        "q": "abbbb",
        "r": "baaaa",
        "s": "baaab",
        "t": "baaba",
        "u": "baabb",
        "v": "baabb",
        "w": "babaa",
        "x": "babab",
        "y": "babba",
        "z": "babbb"
    }

    @staticmethod
    def encrypt(s):
        punct = ";'.,/`!&*()\"\!@#$%^&+_=-[]\|{}\?"
        for c in s:
            s = s.replace(c, c.lower())

            if c in punct:
                s = s.replace(c, "")

        returned = ""
        for letter in s.lower():

            # checks for space
            if(letter != " "):
                returned += Bacon.lookup[letter]
            else:
                returned += " "
        return returned


    @staticmethod
    def get_key(val):
        for key, value in Bacon.lookup.items():
            if value == val:
                return key

    @staticmethod
    def decrypt(s):
        returned = ""
        words = []

        s = s.replace(" ", "")

        # Break up encryption algorithm into groups of 5
        # words = (s[i:i+5] for i in range(0, len(s), 5))

        for i in range(0, len(s), 5):
             words.append(s[i:i+5])

        words = list(words)

        for word in words:

            print(word)
            # print(str(Bacon.get_key(word)))
            returned += str(Bacon.get_key(word))

        return returned;
