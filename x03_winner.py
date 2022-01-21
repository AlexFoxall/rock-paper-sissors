#!python3

'''
Create a function that takes 2 input parameters:
int: computer choice
int: player choice

the choices correspond to:
0: rock
1: paper
2: scissors

Based on the classic rules for Rock Paper Scissors, the return value should be an integer value that indicates if the player is the wins, loses or ties
Output:
-1: player loses
0: tie
1: player wins
'''

def playerWins(computer,player):
  count = 0 
  if computer == player:
    count = count
    print('tie')
  elif computer == 0:
    if player == 1:
      print("player wins")
      count = count + 1
    else:
      print('computer wins')
      count = count - 1
  elif computer == 1:
    if player == 2:
      print('player wins')
      count = count + 1
    else:
      print('computer wins')
      count = count - 1
  elif computer == 2:
    if player == 0:
      print('player wins')
      count = count + 1
    else:
      print('computer wins')
      count = count - 1
  return count

x = playerWins(1,2)
print(x)
'''
if __name__ == "__main__":
  assert playerWins(1,1) == 0
  assert playerWins(1,0) == -1
  assert playerWins(1,2) == 1
  assert playerWins(2,1) == -1
'''
