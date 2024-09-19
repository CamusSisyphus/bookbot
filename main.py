def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict =  get_char_count(text)
    print(f'--- Begin report of {book_path} ---')
    print(f'{num_words} words found in the document\n')
    for ch,v in char_dict_tolist(char_dict):
        print(f"The '{ch}' character was found {v} times")
    print('--- End report ---')
    
def char_dict_tolist(char_dict):
    res = []
    for k,v in char_dict.items():
        res.append((k,v))
    res.sort(reverse=True,key=lambda x : x[1])
    return res

def get_char_count(text):
    lowered_text = text.lower()
    count = {}
    for ch in lowered_text:
        if ch.isalpha():
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1

    return count

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
