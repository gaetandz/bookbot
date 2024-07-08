import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_char(text)
    sorted_list = chars_dict_to_sorted_list(num_chars)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for letters in sorted_list:
        print(f"The '{letters['char']}' character was found {letters['num']} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    char_dict = {}
    lower_text = text.lower()
    list_char = list(lower_text)
    for c in list_char:
        if c.isalpha():
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
    return char_dict

def chars_dict_to_sorted_list(num_chars):
    sorted_list = []
    for c in num_chars:
        sorted_list.append({"char": c, "num": num_chars[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

if __name__ == "__main__":
    main()
