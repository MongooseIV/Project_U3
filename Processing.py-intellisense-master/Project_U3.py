if False:
    from lib.Processing3 import *

# Toki Pona flashcards
val_lst = ["language", "good", "bad", "big", "place", "me", "you", "them", "thing", "person", "food,eat", "cute/sweet",
           "small", "water", "sun", "tool", "fruit", "this/that", "bug", "break", "is/are", "seperator", "shop",
           "see", "have", "give", "work/make", "want", "hear", "sound", "strange", "of", "book", "group", "time",
           "gross", "hair/rope", "hand/arm", "foot/leg", "head/control", "parent"]  # definitions
key_lst = ["toki", "pona", "ike", "suli", "ma", "mi", "sina", "ona", "ijo", "jan", "moku", "suwi", "lili", "telo",
           "suno", "ilo", "kili", "ni", "pipi", "pakala", "li", "e", "esun", "lukin", "jo", "pana", "pali", "wile",
           "kute", "kalama", "nasa", "pi", "lipu", "kulupu", "tenpo", "jaki", "linja", "luka", "noka", "lawa",
           "mama"]  # words in TP
# the following two lists are originals for reference
val_lst_2 = ["language", "good", "bad", "big", "place", "me", "you", "them", "thing", "person", "food,eat",
             "cute/sweet",
             "small", "water", "sun", "tool", "fruit", "this/that", "bug", "break", "is/are", "seperator", "shop",
             "see", "have", "give", "work/make", "want", "hear", "sound", "strange", "of", "book", "group", "time",
             "gross", "hair/rope", "hand/arm", "foot/leg", "head/control", "parent"]  # definitions
key_lst_2 = ["toki", "pona", "ike", "suli", "ma", "mi", "sina", "ona", "ijo", "jan", "moku", "suwi", "lili", "telo",
             "suno", "ilo", "kili", "ni", "pipi", "pakala", "li", "e", "esun", "lukin", "jo", "pana", "pali", "wile",
             "kute", "kalama", "nasa", "pi", "lipu", "kulupu", "tenpo", "jaki", "linja", "luka", "noka", "lawa",
             "mama"]  # words in TP
flip_card = False
time_counter = int(random(len(val_lst)))  # index variable
is_valid = False
is_second = False
while not is_valid:
    if is_second:
        print("")
        print("Please enter a valid response.")
    print("Do you want to: \n1) Guess the definition\n2) Guess the word")
    quiz_type = raw_input("1 or 2: ")  # lets the user decide whether they want to guess the word or the def
    if quiz_type == "1" or quiz_type == "2":
        is_valid = True
    else:
        is_second = True


def setup():
    size(400, 400)
    background(245, 225, 225)


def draw():
    background(245, 225, 225)
    global flip_card
    f = createFont("Arial", 15, False)
    textFont(f)
    fill(200, 0, 0)
    rect(325, 350, 100, 50)  # creates "next" button
    rect(0, 350, 150, 50)  # creates list button
    rect(175, 350, 120, 50)  # creates search button
    fill(0)
    text("Next", 350, 380)
    text("Print Vocab List", 15, 380)
    text("Search words", 185, 380)
    f = createFont("Arial", 24, False)
    textFont(f)
    fill(255)
    rect(100, 85, 200, 200)  # creates flashcard
    fill(200, 0, 0)
    text("  T O K I  P O N A\nF L A S H C A R D S", 95, 35)  # title
    fill(0)
    global time_counter
    if quiz_type == "1":  # guess the definition
        text(key_lst[time_counter], 170, 160)
        if flip_card:
            card_text(val_lst[time_counter])
    else:  # guess the word
        text(val_lst[time_counter], 170, 160)
        if flip_card:
            card_text(key_lst[time_counter])


def card_text(s):  # resets the text on the card
    fill(0, 125, 0)
    rect(100, 85, 200, 200)
    fill(0)
    text(s, 170, 160)


def mousePressed():  # controls buttons
    global flip_card
    global time_counter
    if mouseX > 325 and mouseY > 350:  # calls the next button
        next_button()
    elif mouseX < 150 and mouseY > 350:  # calls the list button
        print_lst()
    elif 175 < mouseX < 295 and mouseY > 350:  # calls the search button
        search_words()


def next_button():
    global flip_card
    global time_counter
    flip_card = True
    if mouseX > 325 and mouseY > 350:  # changes what card you see
        if flip_card:
            flip_card = False
            val_lst.remove(val_lst[time_counter])  # removes previously used cards from the list
            key_lst.remove(key_lst[time_counter])
            if len(val_lst) == 0:  # ends the program if all cards are used
                card_text("Finished!")
                exit()
            time_counter = int(random(len(val_lst)))  # picks a new card
        elif not flip_card:  # flips the card
            flip_card = True


def print_lst():
    print("")
    for i in range(len(val_lst_2)):
        print(key_lst_2[i] + ": " + val_lst_2[i])


def search_words():
    global raw_input
    search_term = raw_input("\nEnter a word: ")
    for i in range(len(val_lst_2)):
        if key_lst_2[i] == search_term:
            print("")
            print(key_lst_2[i] + ": " + val_lst_2[i])
