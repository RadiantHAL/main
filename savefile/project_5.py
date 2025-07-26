import random
import time
def spin_row():
    symbols=[ "🍒" , "🍉", "🍋" , "🔔" , "⭐"]
    spin=[]
    for i in range(3):
        spin.append(random.choice(symbols))
    return spin
def print_row(spin,balance):
    print("Spinning...")
    time.sleep(5)
    print("***********************")
    print(f"  {spin[0]}  |  {spin[1]}  |  {spin[2]}  ")
    print("***********************")
    if spin[0]==spin[1]==spin[2]:
        print("You have won lotter ")
    else: 
        print("you have lost lotter ")
def get_payout(spin,balance):
    if spin[0]==spin[1]==spin[2]:
        if "⭐" in spin:
            balance+=1000 
        elif "🔔" in spin:
            balance+=500
        elif "🍒" in spin:
            balance+=250
        elif "🍉 " in spin:
            balance+=50
        elif "🍋 " in spin:
            balance+=25
    return balance
def main():
    balance=10000
    print("********************************")
    print(" Welcome to python slot ")
    print(" Symbols:🍒 🍉 🍋 🔔 ⭐ ")
    print("********************************")
    while balance>0:
        print(f"Current balance : {balance} Point ")
        bet=input("Place your bet amount : ")
        if not  bet.isdigit:
            print("Please enter a valid number ")
            continue
        else:
            bet=int(bet)
            if bet > balance :
                print("Insufficient funds")        
                continue
            else:
                if bet <= 0:
                    print("Bet must be greater than 0 ")
                else:
                    balance -= bet
                    output=spin_row()
                    print_row(output,balance)
                    balance=get_payout(output,balance)
        play=input("you what play spin again (y/n)")
        if play.lower()=="n":
            break

if __name__=="__main__":
    main()