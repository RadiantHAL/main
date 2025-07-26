def show_balance(lists):
    print("------------------------")
    print(f"Hello {lists[0]} your balnce is ${lists[1]}")
    print("------------------------")
def deposits(lists):
    deposit=int(input("Enter your deposit : "))
    lists[1]+= deposit
    return lists
def withdraws(lists):
    global withdraw
    withdraw =int(input("Enter your withdraws : "))
    if lists[1]-withdraw<=0:
        lists[1]-= withdraw
        return lists
    else:
        return lists
    
account=["Aaradhya bora",200000]
while True:
    print("---------Accounts---------")
    print("Display your balance 1 ")
    print("Withdraw money 2 ")
    print("Deposit money 3 ")
    print("Exit 4 or more than 4  ")
    print("------------------------")
    values=int(input("Enter your choice 1/2/3/4 or more than 4 : "))
    print("------------------------")
    if values==1:
        show_balance(account)
    elif values==2:
        account=deposits(account)
    elif values==3:
        account=withdraws(account)
        if account[1]-withdraw<0:
            print(f"you cannot withdraw this amount of ${withdraw}")
    else:
        print("------------------------")
        print("thank you ")
        print("have nice day")
        print("bye")
        print("------------------------")
        break