#include <stdlib.h>
#include <ctime>
#include <iostream>
#include <vector>
#include "Board.h"
#include "Card.h"
#include "Player.h"

const int MOVE_AMOUNT = 50;
const int PLAYER_AMOUNT = 10000;

#include "init.h"   // newGame() function

// Throw two dices
void throwDices(int (&dices)[2]) {
  dices[0] = 1 + (rand() % 6);
  dices[1] = 1 + (rand() % 6);
}

// Generates all moves for all players
void generateMoves(Board &board, std::vector<Player> &players, Card (&chanceCards)[16], Card (&communityCards)[16]) {
  int dices[2] = {0};

  for (int i=0; i<MOVE_AMOUNT; i++) {
    for (int p=0; p<players.size(); p++) {
      throwDices(dices);
      players[p].MakeMove(dices, board, chanceCards, communityCards);
      players[p].UpdateVisitedPositions(players[p].GetPosition());
    }
  }
}

// Draw Sattuma or Yhteismaa card
void drawCard(int &position, Card (&cards)[16]) {
  int i = rand() % 16;
  if (cards[i].MustMove()) {
    if (cards[i].GetMovePosition() < 0) // Mene 3 askelta taaksepäin
      position -= cards[i].GetMovePosition();
    else
      position = cards[i].GetMovePosition();
  }
}

/*
void printVisits(std::vector<Player> &players) {
  for (Player player : players) {
    std::cout << "PELAAJAN " << player.GetID() << " KÄYDYT RUUDUT:";
    for (int i=0; i<40; i++) {
      std::cout << player.GetPositionVisitedAmount(i) << " ";
    }
    std::cout << "\n\n";
  }
}
*/

void printSquarePercentages(std::vector<Player> &players, Board &board) {
  float squarePercentage;
  std::cout << PLAYER_AMOUNT << " PELAAJAN KÄYTYJEN RUUTUJEN JAKAUMIEN KESKIARVOT KUN PELI KESTÄÄ " << MOVE_AMOUNT << " HEITTOVUOROA:\n";

  for (int i=0; i<40; i++) {
    int squareTotal = 0;
    for (Player player : players) {
      squareTotal += player.GetPositionVisitedAmount(i);
    }
    squarePercentage = (float)squareTotal / ((float)MOVE_AMOUNT * (float)PLAYER_AMOUNT) * 100;
    std::cout << board.GetPosition(i) << ": " << squarePercentage << "%\n";
  }
}

int main() {
  srand((unsigned) time(0));
  Board board;
  Card chanceCards[16];
  Card communityCards[16];
  std::vector<Player> players;

  newGame(board, players, chanceCards, communityCards);
  generateMoves(board, players, chanceCards, communityCards);
  // printVisits(players);
  printSquarePercentages(players, board);

  return 0;
}
