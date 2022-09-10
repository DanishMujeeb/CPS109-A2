from t6 import getting_frequencies
import unittest
def decreasing_frequency(frequency_dict):
    file = open("Decreasing_Frequency.txt", "w")
    sorted_list = []
    sorted_dict = {}
    for i in frequency_dict.values():
        sorted_list.append(i)
    sorted_list.sort()
    for i in sorted_list:
        for j in frequency_dict.keys():
            if frequency_dict[j] == i:
                sorted_dict[j] = i
    for key, value in reversed(sorted_dict.items()):
        file.write(key+", ")
        file.write(str(value)+"\n")
    file.close()

def first_line():
    file = open("Decreasing_Frequency.txt", "r")
    line = file.readline().rstrip("\n")
    correct = False
    if line == "answer, 2729":
        correct = True
    file.close()
    return correct

def second_line():
    file = open("Decreasing_Frequency.txt", "r")
    correct = False
    counter = 0
    for i in file:
        if counter == 1:
            if i.rstrip("\n") == "question, 2727":
                correct = True
                break
        counter += 1
    file.close()
    return correct

class myTests(unittest.TestCase):
    def test1(self):
        self.assertTrue(first_line())
    def test2(self):
        self.assertTrue(second_line())

if __name__ == "__main__":
    decreasing_frequency(getting_frequencies())
    unittest.main(exit=True)