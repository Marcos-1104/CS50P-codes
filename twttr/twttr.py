def main():

    phrase = input("Input: ")
    print("Output: ", shorten(phrase))

def shorten(word):
    for c in word:
        if c in 'aeiouAEIOU':
            word = word.replace(c, '')
    return word

if __name__ == "__main__":
    main()
