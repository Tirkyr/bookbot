def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    words_count = count_words(text)
    letters_count = count_letters(text)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document\n")
    print_report(letters_count)
    print("--- End report ---")


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    result = {}
    for i in text.lower():
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


def get_text(path):
    with open(path) as f:
        return f.read()
    

def print_report(dict_words):
    for key, value in dict_words.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")


main()