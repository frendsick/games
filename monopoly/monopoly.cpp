#include <iostream>
#include <vector>
#include "Board.h"
#include "Card.h"
#include "Player.h"

#include "init.h"   // newGame() function

int main() {
  Board board;
  Card chanceCards[16];
  Card communityCards[16];
  std::vector<Player> players;

  newGame(board, players, chanceCards, communityCards);

  board.Print();
  for (int i=0; i<16; i++) {
    chanceCards[i].Print();
    communityCards[i].Print();
  }
  for (Player player : players) {
    player.Print();
  }

  return 0;
}
