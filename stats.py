def get_word_count(text):
    split = text.split()
    word_count = 0
    for word in split:
        word_count += 1
    txt = f"Found {word_count} total words"
    print(txt)


