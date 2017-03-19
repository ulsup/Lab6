from vigenere_cipher import VigenereCipher
import unittest


class TestVigenereCipher(unittest.TestCase):
    def test_encode_1(self):
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODEDINPYTHON")
        assert encoded == "XECWQXUIVCRKHWA"

    def test_encode_2(self):
        cipher = VigenereCipher("LeaRNinG")
        encoded = cipher.encode("LeaRNINGpyThON")
        assert encoded == "WIAIAQAMACTYBV"

    def test_encode_character(self):
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("E")
        self.assertTrue(encoded == "X")

    def test_encode_spaces(self):
        cipher = VigenereCipher("TRAIN")
        encoded = cipher.encode("ENCODED IN PYTHON")
        self.assertTrue(encoded == "XECWQXUIVCRKHWA")

    def test_encode_lowercase(self):
        cipher = VigenereCipher("TRain")
        encoded = cipher.encode("encoded in Python")
        self.assertTrue(encoded == "XECWQXUIVCRKHWA")

    def test_combine_character_1(self):
        self.assertTrue(VigenereCipher.combine_character("E", "T") == "X")

    def test_combine_character_2(self):
        self.assertTrue(VigenereCipher.combine_character("N", "R") == "E")

    def test_extend_keyword(self):
        cipher = VigenereCipher("TRAIN")
        extended = cipher.extend_keyword(16)
        self.assertTrue(extended == "TRAINTRAINTRAINT")

    def test_separate_character_1(self):
        self.assertTrue(VigenereCipher.separate_character("X", "T") == "E")

    def test_separate_character_2(self):
        self.assertTrue(VigenereCipher.separate_character("E", "R") == "N")

    def test_decode(self):
        cipher = VigenereCipher("TRAIN")
        decoded = cipher.decode("XECWQXUIVCRKHWA")
        self.assertTrue("ENCODEDINPYTHON" == decoded)
