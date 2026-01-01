from stats import get_word_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    return text

#def get_word_count(text):
#    split = text.split()
#    word_count = 0
#    for word in split:
#        word_count += 1
#    txt = f"Found {word_count} total words"
#    print(txt)

def main():
    path_to_file = "books/frankenstein2.txt"
    book_text = get_book_text(path_to_file)
    get_word_count(book_text)



main()
