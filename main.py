def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    contents = get_book_text("./books/frankenstein.txt")
    return contents

def word_count():
    book = get_book_text("./books/frankenstein.txt")
    words = len(book.split())
    print(f"{words} words found in the document")

word_count()