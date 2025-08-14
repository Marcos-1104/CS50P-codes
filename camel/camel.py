
def convert_to_snake(word_in_camel):
    """
    upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for c in word_in_camel:
        if c in upper_letter:
            word_in_camel = word_in_camel.replace(c,'')

    """
    word_list = [] #starting a empty list
    word = ""  # starting a empty string

    for char in word_in_camel: #iterating through every character into "string prompts"
        if char.isupper() and word: #if a character is an upper letter and the word is not empty
            word_list.append(word)  #add a word to the list
            word = char             #update the variable word, the word now is the current character
        else:
            word += char            #else, concatenating the current word with the current char

    if word:                        #out of the loop, if the current word isn´t empty,
        word_list.append(word)      #add the current word to the list


    return word_list


def main():

    camel = input("Write a word in camel case:\n")
    snake = convert_to_snake(camel)
    print("camelCase:", camel)
    print("snake_case: ", end="")

    for i in range(len(snake)):
        word = snake[i]
        if i > 0:
            print("_", end="")  # Print an underscore before each word except the first one
        print(f"{word.lower()}", end="")

    print("\n")


main()
