import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        return ""
    except Exception as e:
        print(f"Error reading the file: {e}")
        return ""
    
def print_report(sorted_characters, filepath, num_words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Character Count -------")
    for item in sorted_characters:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")    


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    if book_text:
        num_words = count_words(book_text)
        char_count = count_characters(book_text)
        sorted_characters = sort_characters(char_count)
        print_report(sorted_characters, filepath, num_words)

if __name__ == "__main__":
    main()
