def count_words_in_book(book_text):
    count = 0
    words = book_text.split()
    count = len(words)
    return count


def count_letters_in_book(book_text):
      letter_dict = {}
      book_text = book_text.lower()
      text = [c for c in book_text]

      for c in text:
           if c.isalpha():
            if c not in letter_dict:
                letter_dict[c] = 1
            else:
                letter_dict[c] += 1

      return letter_dict
    



def sort_dict(dict):
        return sorted(dict.items(), key=lambda x: x[1], reverse=True)