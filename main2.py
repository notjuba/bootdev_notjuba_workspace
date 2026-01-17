def get_book_text (filepath):
    try:
        with open(filepath) as f:
            return f.read()
    except FileNotFoundError:
        Print("Error File not found.")

def word_number(txt):
    num = txt.split()
    return len(num)
    

def main():
    the_print = get_book_text("books/frankenstein.txt")
    print(the_print)
    number = word_number()
    print(number)
    print(f'{num} words found in the document')

main()
