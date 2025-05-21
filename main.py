from stats import count_words_in_book, count_letters_in_book, sort_dict
import sys

def get_book_text(book):
    try:
        with open(f"{book}", "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{book}' was not found in the 'books' directory.")
    return text

def print_book_stats(num_words, dict_letter, current_book):
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at books/{current_book}.txt...")
        print(f"Found {num_words} total words") 
        print("--------- Character Count -------")
        for key, val in dict_letter:
             print(f"{key}: {val}")
        
        print("============= END ===============")


def print_instructions():
    print()
     

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
         

    print_instructions()
    current_book = sys.argv[1]
    text = get_book_text(current_book)
    num_words = count_words_in_book(text)
    dict_letters = count_letters_in_book(text)
    dict_letters = sort_dict(dict_letters)
    print_book_stats(num_words, dict_letters, current_book)
    




























main()