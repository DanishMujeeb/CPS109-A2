import unittest
def getting_frequencies():
    file = open("practice.txt", "r")
    file2 = open("Frequency.txt", "w")
    line = []
    frequency_dict = {}
    for i in file:
        line = i.split()
        for j in line:
            j = j.lower()
            if j not in frequency_dict:
                frequency_dict[j] = 1
            else:
                frequency_dict[j] += 1
    for key, value in frequency_dict.items():
        file2.write(key + ", ")
        file2.write(str(value) + "\n")
    file.close()
    file2.close()
    return frequency_dict

def man_frequency():
    file = open("Frequency.txt", "r")
    correct = False
    for i in file:
        if i.rstrip("\n") == "man, 3":
            correct = True
    file.close()
    return correct

def who_frequency():
    file = open("Frequency.txt", "r")
    correct = False
    for i in file:
        if i.rstrip("\n") == "who, 4":
            correct = True
    file.close()
    return correct

class myTests(unittest.TestCase):
    def test1(self):
        self.assertTrue(man_frequency())
    def test2(self):
        self.assertTrue(who_frequency())

if __name__ == "__main__":
    getting_frequencies()
    unittest.main(exit=True)