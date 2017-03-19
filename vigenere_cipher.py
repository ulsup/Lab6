class VigenereCipher:
    def __init__(self, keyword):  # initializes a keyword
        self.keyword = keyword

    def encode(self, plaintext):
        return "XECWQXUIVCRKHWA"

    def combine_character(plain, keyword):
        plain = plain.upper()
        keyword = keyword.upper()  # changes lowercase letters to uppercase
        plain_num = ord(plain) - ord('A')  # changes a string characters to an integer (Unicode code)
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (plain_num + keyword_num) % 26)  # changes back to a string with Unicode (inverse of ord)

    def extend_keyword(self, number):
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    def encode(self, plaintext):
        plaintext = plaintext.replace(" ", "").upper()  # replaces whitespaces with no spaces
        cipher = []
        keyword = self.extend_keyword(len(plaintext))
        for p, k in zip(plaintext, keyword):  # creates tuples of appropriate elements of two lists
            cipher.append(VigenereCipher.combine_character(p, k))  # combines charactes of tuples, adds it to the list
        return "".join(cipher)  # joins all of the elements of a list

    def separate_character(cypher, keyword):
        cypher = cypher.upper()
        keyword = keyword.upper()
        cypher_num = ord(cypher) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (cypher_num - keyword_num) % 26)

    def decode(self, ciphertext):  # decodes a keyword
        plain = []
        keyword = self.extend_keyword(len(ciphertext))
        for p, k in zip(ciphertext, keyword):
            plain.append(VigenereCipher.separate_character(p, k))
        return "".join(plain)
