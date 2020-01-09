#include <iostream>
#include <vector>
#include <algorithm>
#include "Card.h"     // Every card and card related methods
#include "Position.h" // Single position containing all 9 cards in 3x3 grid

/*  Card has 1 to 3 glass tops or bottoms on each side.
 *  Each side is represented in binary form so that tops and bottoms match:
 *    TOPS:
 *      LEFT = 1,   MID = 2,  RIGHT = 4
 *    BOTTOMS:
 *      LEFT = -4,  MID = -2, RIGHT = -1
 *  
 *  TRDL --> S0 = TOP, S1 = RIGHT, S2 = DOWN, S3 = LEFT
 *  
 *  EXAMPLE CARD:
 *    Side 0 has three bottoms    ==> -7 (-4 -2 -1)
 *    Side 1 has two tops, R+M    ==> 6  (4 + 2)
 *    Side 2 has one top          ==> 2
 *    Side 3 has two bottoms, R+M ==> -3 (-1 -2)
 *
 */

void initializeCards(Card (&cards)[9]) {
  std::cout << "Initializing cards" << std::endl;

  // Initialize cardID's and positions
  for (int i=0; i<9; i++) {
    cards[i].cardID   = i;
    cards[i].position = i;
  }
  
  // TRDL
  const int all_card_sides[9][4] = {
    {-6, -3,  7, -2},
    {-6, -2,  7, -3},
    {-6,  3,  2, -7},
    {-6, -2,  7,  3},
    {-7,  6,  3, -2},
    {-7,  2,  3,  6},
    {-7, -2,  6,  3},
    {-7, -3,  2,  6},
    { 2, -3,  6,  7}};
  
  // Initialize all sides of cards
  for (int i=0; i<9; i++) {
    cards[i].sides[0] = all_card_sides[i][0];
    cards[i].sides[1] = all_card_sides[i][1];
    cards[i].sides[2] = all_card_sides[i][2];
    cards[i].sides[3] = all_card_sides[i][3];
  }

  // Print all sides of cards
  for (Card card : cards)
    card.PrintCard();
  
  std::cout << "All cards are initialized!" << std::endl;
}

// Utility function for sorting Card objects by card positions
bool CompareCardPositions(Card c1, Card c2) { return (c1.position < c2.position); }

// TODO
void BruteForce(Position handled_position) {
  int rounds = 0;
  while (rounds < 9) {
    int current = 0;
    int checking = current + 1;
    int checked_cards = 0;
    bool full_rev = false;

    while (checked_cards < 9) {
      // Rotate card at a time
      for (int i=1; i<9-rounds; i++) {
        handled_position.cards[i].direction++;
        // If current card has rotated full revolution, rotate next card
        if (handled_position.cards[i].direction % 4 != 0)
          break;

        // If last card has rotated full revolution
        else if (i == 8) {
          current++; full_rev = true; handled_position.PrintPosition();
        }
      }

      if (handled_position.IsSolved()) {
        std::cout << "SOLVED!\n";
        handled_position.PrintPosition();
        exit(0);
      }
      else if (current == 9-checked_cards-rounds) {
        checked_cards++;
        current = 1;
      }
      
      // Move current card forward by one spot
      else if (full_rev) {
        handled_position.SwapCards(current, current-1);
        full_rev = false;
      }
    }
    rounds++;
  }
}

int main() {
  Card cards[9];
  initializeCards(cards); // Initializes all cards with correct values
  
  Position position;

  for (Card card : cards)
    position.cards.emplace_back(card);

  position.SortPosition();
  position.PrintPosition();

  Position initial_pos = position;

  BruteForce(position);

  return 0;
}
