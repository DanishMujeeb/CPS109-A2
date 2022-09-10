import unittest
from t2 import making_lists
def making_pairs():
    file = open("practice.txt", "r", encoding="utf-8-sig")
    q_a, pairs, j = [], [], 0
    for i in file:
        i = i.lower()
        if j == 2:
            pairs.append(q_a)
            q_a = []
            j = 0
        j += 1
        q_a.append(i.rstrip("\n"))
    file.close()
    pairs.append(q_a)
    making_lists(pairs)

def overlapping_pairs():
    file = open("Overlapping.txt", "r")
    counter = 0
    for i in file:
        counter += 1
    file.close()
    return counter//2

def unique_pairs():
    file = open("unique_QA_Pairs.txt", "r")
    counter = 0
    for i in file:
        counter += 1
    file.close()
    return counter//2

class myTests(unittest.TestCase):
 def test1(self):
     self.assertEqual(overlapping_pairs(), 2)
 def test2(self):
     self.assertTrue(unique_pairs(), 3)

if __name__ == "__main__":
    making_pairs()
    unittest.main(exit=True)