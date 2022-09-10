from t3 import making_dictionary
import unittest
def writing_questions():
    file = open("unique_QA_Pairs.txt", "r")
    file2 = open("Questions.txt", "w")
    for keys in making_dictionary().keys():
        keys = keys.replace(keys[0:9],"")
        file2.write(keys+"\n")

def first_question():
    file = open("Questions.txt", "r")
    line = file.readline().rstrip("\n")
    file.close()
    return line

def second_question():
    file = open("Questions.txt", "r")
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
     self.assertEqual(first_question(), "who is arya stark's wife?")
 def test2(self):
     self.assertEqual(second_question(), "who escaped the persecution of house stark?")

if __name__ == "__main__":
    writing_questions()
    unittest.main(exit=True)