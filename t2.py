def making_pairs():
    file = open("QA_Pairs.txt", "r", encoding="utf-8-sig")
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

def making_lists(q_a_pairs):
    same = False
    overlapping, unique, identical = [], [], []
    counter = 0
    for i in q_a_pairs:
        counter2 = 0
        for j in q_a_pairs:
            if i == j:
                if counter != counter2:
                    if i not in overlapping:
                        overlapping.append(i)
                        identical.append(j)
                        same = True
            elif i[0] == j[0] or i[1] == j[1]:
                if j not in overlapping and i not in overlapping:
                    overlapping.append(j)
            counter2 += 1
        if not same:
            if i not in overlapping:
                unique.append(i)
        counter += 1
        same = False
    writing_to_file(overlapping, unique)

def writing_to_file(similar, distinct):
    file = open("Overlapping.txt", "w")
    for i in similar:
        for j in i:
            file.write(j+"\n")
    file.close()
    file2 = open("unique_QA_Pairs.txt", "w")
    for i in distinct:
        for j in i:
            file2.write(j+"\n")
    file2.close()

if __name__ == "__main__":
    making_pairs()