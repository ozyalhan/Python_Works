"""
Facebook Python Programmers Group Questions

1) Write function that takes two args: list of strings and a prefix (string). +
   The function should iterate over the list and find all strings which start with the prefix, then return list of such strings+
2) Write function which takes string AAAAaaBCCCDDe as argument and returns its compressed version A4a2B1C3D2e1 +


23.02.2020 03:27 I sent answers.

"""

#1
def problem1(str_list, prefix):

    matched_list = []
    for i in str_list:
        if i[0] == prefix:
            matched_list.append(i)
    return matched_list
#problem1(["apple","banana","cherry","berry"],"b")


# Write function which takes string AAAAaaBCCCDDe as argument and returns its compressed version A4a2B1C3D2e1
def problem2(value):
    return_str = ""
    checked_i = ""
    counter = 0

    for i in range(0, len(value)):

        if i == 0:
            checked_i = value[i]
            return_str = value[i]
            counter += 1

        if i != 0 and counter != 0:
            if checked_i == value[i]:
                counter += 1
                checked_i == value[i]
            else:
                return_str += str(counter)
                counter = 0
                checked_i == value[i]

        if i != 0 and counter == 0:
            checked_i = value[i]
            return_str += value[i]
            counter += 1

        if i == len(value) - 1:
            return_str += str(counter)

    return return_str

#problem2("AAAAaaBCCCDDe");
#print(problem2("AAAAaaBCCCDDe"));
#print(problem2("AAAAAaaBCCCDDeeee"));
#print(problem2("AaaBCCCDDDDDDDDDDDDD"));
