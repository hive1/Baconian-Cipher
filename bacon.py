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
        returned = ""
        for letter in s:

            # checks for space
            if(letter != " "):
                returned += lookup[letter]
            else:
                returned += " "
        return returned


    def get_key(val):
        for key, value in lookup.get_dict():
            if value == val:
                return key

    @staticmethod
    def decrypt(s):
        returned = ""
        words = [(string[i:i+5]) for i in range(0, len(string), n)]

        for word in words:
            returned += get_key(word)

        return returned;
