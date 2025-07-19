import sys
from stats import get_total_words
from stats import get_char_dict
from stats import get_report

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    contents = get_book_text(sys.argv[1])
    num_words = get_total_words(contents)
    character_dict = get_char_dict(contents)
    get_report(num_words, character_dict)

main()

