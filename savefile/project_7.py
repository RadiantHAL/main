import random
import colorama

word = ("farmer","moment","safety","winner","system","throat","recipe","camera","growth",
         "studio","dealer","thanks","theory","poetry","police","extent","person","drawer",
         "county","client","singer","basket","aspect","engine","writer","affair","dinner",
         "health","sample","sister","advice","method","cousin","member","energy","editor",
         "sector","agency","worker","memory","device","tennis","ladder","policy","driver",
         "orange","church","flight","coffee","nature")

hangman = {
    0: ("     ",
        "     ",
        "     "),         
    1: ("  o  ",
        "     ",
        "     "),         
    2: ("  o  ",
        "  |  ",
        "     "),         
    3: ("  o  ",
        " /|  ",
        "     "),         
    4: ("  o  ",
        " /|\\ ",
        "     "),         
    5: ("  o  ",
        " /|\\ ",
        " /   "),         
    6: ("  o  ",
        " /|\\ ",
        " / \\ ")          
}
#def random_check():
 #randomer=random.choice(word)
         
def hint_color(player,randomer,num):
    again_list=[]
    for i in range(6):
        if player[i]==randomer[i]:
            print(colorama.Fore.GREEN+f"{player[i]}",end="")   
        elif player[i] in randomer:
            if again_list.count(player[i]) < randomer.count(player[i]):
                print(colorama.Fore.YELLOW + f"{player[i]}", end="")
                again_list.append(player[i])
            else:
                print(colorama.Fore.RED + f"{player[i]}", end="")
                again_list.append(player[i])
        else:
            print(colorama.Fore.RED + f"{player[i]}", end="")
            again_list.append(player[i])
    print()
    if again_list!=[]:
        hangman_check(hangman,num)

def hangman_check(hangman,num):
         
     print(colorama.Fore.WHITE+f"{hangman[num][0]}")
     print(colorama.Fore.WHITE+f"{hangman[num][1]}")
     print(colorama.Fore.WHITE+f"{hangman[num][2]}")
         
def main():
         
    num_1=6
    num_2=0
         
    randomer=random.choice(word)
         
    while True:
         print(colorama.Fore.RED+"double check your writing for 2 or more time same aplphabet ")
             
        if num_1<0 :
            print("Game over")
            break 
                 
        player=input(colorama.Fore.WHITE+f"Enter your choice word (only {num_1+1} turn left) : ")

        if player.isalpha() and len(player)==6:
            hint_color(player,randomer,num_2)   
            num_2+=1
            num_1-=1 
                 
            if player==randomer:
                print(colorama.Fore.WHITE+"you have won the gussing game")
                break 
                     
        elif not player.isalpha() and len(player)!=6 and player!="" and player!=" ":
            print(colorama.Fore.WHITE+"Enter in valid")
            print(colorama.Fore.WHITE+"number/symbols/size word don't equal to 6 ") 
              
if __name__=="__main__":
    main()
    main()
