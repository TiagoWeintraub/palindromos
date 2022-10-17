import unittest

def palindromo(palabra):
    
    if palabra.lower().replace(" ", "") == palabra[::-1].lower().replace(" ", ""):
        return True
    else:
        return False
   


class Testpalindromo(unittest.TestCase):
    def test_1(self):
        resultado = palindromo("ana")
        self.assertEqual(resultado, True)

    def test_2(self):
        resultado = palindromo("Radar")
        self.assertEqual(resultado, True)
    
    def test_3(self):
        resultado = palindromo("Sale El As")
        self.assertEqual(resultado, True)
        

if __name__ == '__main__':
    unittest.main()
