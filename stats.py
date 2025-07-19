def get_total_words(content):
    content_arr = content.split()
    return len(content_arr)

def get_char_dict(content):
    char_dict = {}
    for char in content:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] =  char_dict[lower_char] + 1
        else:
            char_dict[lower_char] = 1
    return char_dict

def sort_on(item):
    return item[1]

def get_report(total_words, dict_items):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    items = list(dict_items.items())
    items.sort(reverse=True, key=sort_on)
    for key, val in items:
        print(f"{key}: {val}")
    
    print("============= END ===============")
