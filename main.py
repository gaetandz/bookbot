def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_word = get_num_words(text)
    print(num_word)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    main()
