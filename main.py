from stats import *
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print_report(book_path)


def print_report(book_path):
    book_text = get_book_text(book_path)
    book_num_words = get_num_words(book_text)
    book_char_count = get_char_count(book_text)
    char_count_list = get_list_of_char_counts(book_char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {book_num_words} total words")
    print("--------- Character Count -------")

    for i in char_count_list:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['count']}")

    print("============= END ===============")


main()
