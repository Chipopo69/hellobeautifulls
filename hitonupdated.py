import random

def ask_question(question):
    answer = input(question + " ")
    return answer

def tell_joke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "I wouldn't buy anything with Velcro. It's a total rip-off!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "I'm reading a book about anti-gravity. It's impossible to put down!",
        "Why couldn't the leopard play hide and seek? Because he was always spotted!",
        "Why did the golfer bring two pairs of pants? In case he got a hole-in-one!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "Did you hear about the kidnapping at the playground? They woke up!"
    ]
    random_joke = random.choice(jokes)
    print(random_joke)

def main():
    print("Welcome!")
    while True:
        start = input("Would you like to continue? (yes\/no) ")
        if start.lower() == "yes":
            break
        elif start.lower() == "no":
            print("Okay, let's try again.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    answer1 = ask_question("How are you doing?")
    print("Answer 1:", answer1)

    answer2 = ask_question("Do you like memes? (yes\/no)")
    print("Answer 2:", answer2)

    if answer2.lower() == "yes":
        answer7 = ask_question("Would you like to hear a joke? (yes\/no)")
        print("Answer 7:", answer7)
        if answer7.lower() == "yes":
            tell_joke()

    answer3 = ask_question("What is your favorite song?")
    print("Answer 3:", answer3)

    answer4 = ask_question("What is your favorite book?")
    print("Answer 4:", answer4)

    answer5 = ask_question("What is your favorite color?")
    print("Answer 5:", answer5)

    answer6 = ask_question("What is your favorite subject in school?")
    print("Answer 6:", answer6)

    answer9 = ask_question("I think I've done enough, will you answer my DM? (yes\/no)")
    print("Answer 9:", answer9)

    if answer9.lower() == "yes":
        answer10 = ask_question("Would you like to continue? (yes\/no)")
        print("Answer 10:", answer10)
        if answer10.lower() == "yes":
            print("http:\/\/r.mtdv.me\/jR85HknnTY")  # You can add the correct URL here


if __name__ == "__main__":
    main()

