user_answer = input(
    "What is the answer to the Great Question of Life, the Universe and Everything?\n").lower().strip()

if user_answer == "42" or user_answer == "forty-two" or user_answer == "forty two":
    print("Yes")
else:
    print("No")
