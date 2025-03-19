from stats import word_count, char_count, sort_chars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    contents = get_book_text(filepath)
    words = word_count(contents)
    chars = char_count(contents)
    sort = sort_chars(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    for char_data in sort:
        char = char_data["char"]
        count = char_data["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()