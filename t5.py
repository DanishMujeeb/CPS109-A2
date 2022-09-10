from t3 import making_dictionary
import unittest
def writing_answers():
    file = open("unique_QA_Pairs.txt", "r")
    file2 = open("Answers.txt", "w")
    for values in making_dictionary().values():
        values = values.replace(values[0:7],"")
        file2.write(values+"\n")

def first_answer():
    file = open("Answers.txt", "r")
    line = file.readline().rstrip("\n")
    file.close()
    return line

def second_answer():
    file = open("Answers.txt", "r")
    counter = 0
    line = ""
    for i in file:
        if counter == 1:
            line = i.rstrip("\n")
            break
        counter += 1
    file.close()
    return line

class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(first_answer(), "lady catelyn stark")
    def test2(self):
        self.assertEqual(second_answer(), "house lannister")

if __name__ == "__main__":
    writing_answers()
    unittest.main(exit=True)