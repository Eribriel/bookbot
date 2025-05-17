




def get_words_as_string(book_path):
    with open(book_path) as file:
        file_contents = file.read()
        return file_contents

def get_word_count(book_path):
    with open(book_path) as file:
        file_contents = file.read()
        word_list = file_contents.split()
    return word_list

def read_file(book_path):
    read_file = get_word_count(book_path)
    word_count = len(read_file)
    return print(f"Found {word_count} total words")





def individual_character_count(book_path):
     characters = []
     character_count = {}
     character_sort = []
     read_file = get_words_as_string(book_path)
     word_split = read_file.lower()

     for letter in word_split:
         if letter not in character_count and letter.isalpha():
            character_count[letter] = 1
         elif letter.isalpha(): character_count[letter] += 1
        
     for char, count in character_count.items():
         char_info = {"char": char, "num": count}
         characters.append(char_info)
     characters.sort(reverse=True, key=lambda d: d["num"])
     
     
    
    

     return characters
     
def sorted_list(book_path):
    content = get_words_as_string(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    read_file(book_path)
    print("--------- Character Count -------")
    for char_dict in individual_character_count(book_path):
        character = char_dict["char"]
        count = char_dict["num"]
        print(f"{character}: {count}")
    print("============= END ===============")