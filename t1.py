import unittest
def num_of_pairs():
    file = open("QA_Pairs.txt", "r")
    counter = 0
    for i in file:
        counter += 1
    file.close()
    return counter//2

def num_of_pairs_practice():
    file = open("practice.txt", "r")
    counter = 0
    for i in file:
        counter += 1
    file.close()
    return counter//2

class myTests(unittest.TestCase):
 def test1(self):
     self.assertEqual(num_of_pairs(), 5725)
 def test2(self):
     self.assertEqual(num_of_pairs_practice(), 6)

if __name__ == "__main__":
    unittest.main(exit=True)