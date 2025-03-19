
def word_count(book):
    words = len(book.split())
    return words

def char_count(book):
    char_count = {}
    lower_book = book.lower()
    for char in lower_book:
        char_count[char]=char_count.get(char, 0) + 1
    return char_count

def sort_by_count(char_dict):
    return char_dict["count"]

def sort_chars(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        c_dict = {"char": char, "count": count}
        chars_list.append(c_dict)
    chars_list.sort(reverse=True,key=sort_by_count)
    return chars_list