import random
#● ┌ ─ ┐ │ └ ┘
dice_art={
1:("┌───────────┐",
  "│           │",
  "│     ●     │",
  "│           │",
  "└───────────┘",),
2:("┌───────────┐",
  "│ ●         │",
  "│           │",
  "│         ● │",
  "└───────────┘",),
3:("┌───────────┐",
  "│ ●         │",
  "│     ●     │",
  "│         ● │",
  "└───────────┘",),
4:("┌───────────┐",
  "│ ●       ● │",
  "│           │",
  "│ ●       ● │",
  "└───────────┘",),
5:("┌───────────┐",
  "│ ●       ● │",
  "│     ●     │",
  "│ ●       ● │",
  "└───────────┘",),
6:("┌───────────┐",
  "│ ●       ● │",
  "│ ●       ● │",
  "│ ●       ● │",
  "└───────────┘",)}

dice = []
total_dice = 0
num_of_dice =int(input("How many dice to roll : "))
for i in range(num_of_dice):
    dice.append(random.randint(1,6))

for i in range(num_of_dice):
    for l in dice_art.get(dice[i]):
        print(l)

for i in dice:
    total_dice += i
print(total_dice)
