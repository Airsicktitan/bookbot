def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = count_strings(text)
    char_dict = count_letters(text)
    chars_sorted = chars_dict_to_sorted_list(char_dict)
    print(f"--- Begin report of {book_path} ---")
    print('{:,}'.format(total_words) + f" words were found in the document")
    print()
    
    for item in chars_sorted:
        if not item['char'].isalpha():
            continue
        print(f"The '{item['char']}' character was found " + '{:,}'.format(item['num']) + " times")

    print('--- End Report ---')
    print()

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_strings(text):
    words = text.split()
    count = 0

    for word in words:
        count += 1
    return count

def count_letters(text):
    letter = {}
    words = text.split()

    for letter1 in words:
        for letter2 in letter1:
            letter_lowered = letter2.lower()

            if(letter_lowered in letter):
                letter[letter_lowered] += 1
            else:
                letter[letter_lowered] = 1
    return letter

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()