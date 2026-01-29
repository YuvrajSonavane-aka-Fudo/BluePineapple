
#*find all words starting with a and e in a given string

def words_starting_with_a_and_e(str1):
    ''' Returns a list of words starting with a or e in a given string'''
    result = []
    list1 = str1.split(" ")
    for i in list1:
        if i[0] == "a" or i[0] == "e":
            result.append(i)
    return result

print(words_starting_with_a_and_e("hello i am under the water"))
