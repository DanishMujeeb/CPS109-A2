import unittest
def making_dictionary():
    file = open("unique_QA_Pairs.txt", "r")
    file2 = open("QA_dictionary.txt", "w")
    pairs_list = []
    pairs_dict = {}
    for line in file:
        pairs_list.append(line.rstrip("\n"))
    for i in range(1, len(pairs_list), 2):
        pairs_dict[pairs_list[i]] = pairs_list[i - 1]
    for key, value in pairs_dict.items():
        file2.write(key + ": ")
        file2.write(value + "\n")
    file2.close()
    file.close()
    return pairs_dict

def first_pair():
    return making_dictionary()["question who is arya stark's wife?"]

def second_pair():
    return making_dictionary()["question who escaped the persecution of house stark?"]

class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(first_pair(), "answer lady catelyn stark")
    def test2(self):
        self.assertEqual(second_pair(), "answer house lannister")

if __name__ == "__main__":
    making_dictionary()
    unittest.main(exit=True)