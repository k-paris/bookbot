def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_count = {}

    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_characters(char_count):
    list_of_dicts = []
    for k,v in char_count.items():
        list_of_dicts.append({'char': k, 'num': v})

    sorted_list = sorted(list_of_dicts, key=lambda x: x['num'], reverse=True)
    return sorted_list