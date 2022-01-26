#!python3

"""
Create a full rock paper scissors game
You can incorporate the other files in this project to help you
"""

from x01_player import *
from x02_computer import *
from x03_winner import *
def main():
  x = playerChoice()
  y = computerChoice()
  z = playerWins(x,y)
  
  
  
  if z == 0:
    print("0: tie")
  if z == 1:
    print('1: player wins')
  if z == -1:
    print('-1: player loses') 
  
  return None
if __name__ == "__main__":
  main()

