def getting_frequencies():
    file = open("unique_QA_Pairs.txt", "r")
    file2 = open("Frequency.txt", "w")
    line = []
    frequency_dict = {}
    for i in file:
        line = i.split()
        for j in line:
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

if __name__ == "__main__":
    getting_frequencies()