import random
import colorama
from colorama import Fore

colorama.init()

words = ("farmer","moment","safety","winner","system","throat","recipe","camera","growth",
         "studio","dealer","thanks","theory","poetry","police","extent","person","drawer",
         "county","client","singer","basket","aspect","engine","writer","affair","dinner",
         "health","sample","sister","advice","method","cousin","member","energy","editor",
         "sector","agency","worker","memory","device","tennis","ladder","policy","driver",
         "orange","church","flight","coffee","nature")

hangman = {
    0: ("     ",
        "     ",
        "     "),
    1: (" o   ",
        "     ",
        "     "),
    2: (" o   ",
        " |   ",
        "     "),
    3: (" o   ",
        "/|   ",
        "     "),
    4: (" o   ",
        "/|\\  ",
        "     "),
    5: (" o   ",
        "/|\\  ",
        "/    "),
    6: (" o   ",
        "/|\\  ",
        "/ \\  ")
}

def display_hangman(stage):
    print("\n".join(hangman[stage]))

def hint_color(player, random_word):
    hint = ""
    used_indices = []
    for i in range(6):
        if player[i] == random_word[i]:
            hint += Fore.GREEN + player[i]
            used_indices.append(i)
        else:
            hint += Fore.WHITE+"_" 

    
    for i in range(6):
        if hint[i] != "_":
            continue
        if player[i] in random_word:
            # Check if the letter exists in unused positions
            found = False
            for j in range(6):
                if j not in used_indices and player[i] == random_word[j]:
                    found = True
                    used_indices.append(j)
                    break
            if found:
                hint = hint[:i] + Fore.YELLOW + player[i] + hint[i+1:]
            else:
                hint = hint[:i] + Fore.RED + player[i] + hint[i+1:]
        else:
            hint = hint[:i] + Fore.RED + player[i] + hint[i+1:]

    print(hint + Fore.WHITE)

def main():
    random_word = random.choice(words)
    attempts = 0
    max_attempts = 6

    print("🎮 Welcome to Hangman Wordle!\n")
    while attempts < max_attempts:
        player = input(Fore.WHITE + f"Enter a 6-letter word ({max_attempts - attempts} attempts left): ").lower()
        if player.isalpha() and len(player) == 6:
            hint_color(player, random_word)
            if player == random_word:
                print(Fore.CYAN + "🎉 Congratulations! You guessed it right.")
                break
            else:
                attempts += 1
                display_hangman(attempts)
        else:
            print(Fore.LIGHTRED_EX + "⛔ Please enter a valid 6-letter alphabetic word.")

    else:
        print(Fore.RED + f"\n💀 Game Over! The correct word was: {random_word}")
if __name__=="__main__":
    main()
