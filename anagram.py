import string

word_list = [
    "listen", "silent", "enlist", "inlets", "google", "gooGle", "banana",
]

def count_letters(word):
    alphabet = {letter: 0 for letter in string.ascii_lowercase}
    for char in range(len(word)):
        if word.lower()[char] in alphabet:
            alphabet[word.lower()[char]] +=1
    return alphabet

def make_pairs():
    dict_word_counted = {}
    anagram_pairs = []

    for word in range(len(word_list)):
        dict_word_counted[word_list[word]]= count_letters(word_list[word])

    for i in range(len(word_list)):
        for j in range(i+1, len(word_list)):
            if dict_word_counted.get(word_list[i]) == dict_word_counted.get(word_list[j]):
                #print(f"{word_list[i]} , {word_list[j]} match")
                anagram_pairs.append((word_list[i], word_list[j]))
            else:
                #print(f"{word_list[i]} , {word_list[j]} don't match")
                continue
    return anagram_pairs

def group_pairs(pairs):
    grouped = []

    for a, b in pairs:
        if not is_in_any_group(a, grouped) and not is_in_any_group(b, grouped):
            grouped.append([a, b])
        else:
            for group in grouped:
                if a in group or b in group:
                    if a not in group:
                        group.append(a)
                    if b not in group:
                        group.append(b)
                    break

    return grouped


def is_in_any_group(word, groups):
    for group in groups:
        if word in group:
            return True
    return False



def print_groups(grouped):
    print("\nGrouped Anagrams")
    print("****************")
    for i in range(len(grouped)):
        print(f"{i+1}.",end=' ')
        for j in range(len(grouped[i])):
            print(f"{grouped[i][j]}", end = ',' )
        print("")

def menu():
    pairs   = make_pairs()
    grouped = group_pairs(pairs)
    print_groups(grouped)
    
if __name__ == "__main__":
    while menu():
        pass


