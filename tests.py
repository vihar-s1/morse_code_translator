#!/usr/bin/env python3
import unittest
import MorseCoder


class Test_Translator(unittest.TestCase):
    def test_EmptyString(self):
        self.assertTrue(MorseCoder.encode("") == "")

    def test_NoneType(self):
        self.assertTrue(MorseCoder.encode(None) == "")
    

    def test_encoder1(self):
        self.assertTrue(MorseCoder.encode("Hello") == ".... . .-.. .-.. --- ")

    def test_encoder2(self):
        self.assertTrue(MorseCoder.encode("hElLo") == ".... . .-.. .-.. --- ")


    def test_decoder1(self):
        self.assertTrue(MorseCoder.decode(".... . .-.. .-.. --- ") == "HELLO")
    
    def test_decoder2(self):
        self.assertTrue(MorseCoder.decode(".... . .-.. .-.. --- ! ") == "HELLO! ")
    
    def test_decoder3(self):
        self.assertTrue( MorseCoder.decode(".... . .-.. .-.. ---  .-- --- .-. .-.. -.. ") == "HELLO WORLD")


unittest.main()