def convert(to_emotion):
    to_emotion = to_emotion.replace(":)", "🙂")
    to_emotion = to_emotion.replace(":(", "🙁")
    return to_emotion

def main():
    phrase = input("Write a phrase:\n")
    print(convert(phrase))
main ()
