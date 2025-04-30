from stats import count_words, count_characters, get_sorted_list
import sys

def get_book_text(path):
    with open(path) as file:
        return file.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words =  count_words(text)
    num_characters = count_characters(text)
    sorted_list = get_sorted_list(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for x in sorted_list:
        if x["char"].isalpha():
            print(f"{x["char"]}: {x["num"]}")

main()