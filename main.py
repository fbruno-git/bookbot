def main():
    with open("books/frankenstein.txt") as f:
        file_contents= f.read()
    words = count_words(file_contents)
    letter_count = count_letters(file_contents)
    list_of_letter_count = [value for value in letter_count.values()]
    list_of_letter_count.sort(reverse=True)
    
    print (list_of_letter_count)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print(" ")
    for letter in list_of_letter_count:
        character = ""
        for item in letter_count:
            if letter_count[item] == letter:
                character = item
                print(f"The '{character}' character was found {letter} times ")
    print("--- End report ---")
def count_words(text):
    counter = 0 
    words= text.split()
    for i in words:
        counter += 1
    return counter
    
def count_letters(text):
    result_dict = {}
    to_count=text.lower()
    for character in to_count:
        character = list(character)
        for letter in character:
            if letter.isalpha():
                if letter in result_dict:
                    result_dict[letter] += 1
                else:
                    result_dict[letter] = 1 
    return result_dict

    


main()