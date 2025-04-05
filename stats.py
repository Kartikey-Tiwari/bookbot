def get_book_text(bookpath):
    book_text = ""
    with open(bookpath) as file:
        book_text = file.read()
    return book_text


def get_num_words(book_text):
    return len(book_text.split())


def get_char_count(book_text):
    letter_count = {}
    for char in book_text:
        letter_count[char.lower()] = letter_count.get(char.lower(), 0) + 1
    return letter_count


def get_list_of_char_counts(char_count_dict):
    char_count_list = [
        {"char": key, "count": char_count_dict[key]} for key in char_count_dict
    ]
    char_count_list.sort(key=lambda x: x["count"], reverse=True)
    return char_count_list
