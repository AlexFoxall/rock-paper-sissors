#! python3

"""
Create a function that asks the player for their choice
The function should return:
  rock     : 0
  paper    : 1
  scissors : 2

```
Sample Run:
Enter your choice:
rock

Output: 0
"""

def playerChoice():
  print('0 = rock, 1 = paper, 2 = scissors')
  value = input("input rock, paper or scissors")
  player = int(value)
  return player


if __name__ == "__main__":
  player = playerChoice()
  print(player)
