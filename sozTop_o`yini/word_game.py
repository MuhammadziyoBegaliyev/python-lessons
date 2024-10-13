import random
from uzwords import words


def get_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        print("8-worked")
        word = random.choice(words)
    return word.upper()


def display(user_letters,word):
    display_letter = ""
    for letter in word:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter


    # harflar = "Английский"
    # word = "наемник"
    # display(harflar, word)



def play():
    word = get_word() 
    word_letters = set(word)
    user_letters = ""   
    print(f"Men {len(word)} xonali so`z o`yladim . Topa olasizmi ?")
    while len(word_letters)>0:
        print(display(user_letters,word))
        if len(user_letters)>0:
            print(f"Shu vaqtgacha kiritilgan so`zlar royhati :{user_letters}")
        letter = input("Xarf kiriting :").upper()
        if letter in user_letters:
            print("Bu xarfni avval kiritgansiz !")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} harfi tog`ri .")
        else :
            print("Bunday harf yo`q.")
        user_letters += letter
    print(f"Tabriklayman! {word}so`zini {len(user_letters)} - ta urunishda to`pladingiz.")








play()