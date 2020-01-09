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


bool fitsRight(std::vector<Card> cards, Card& c2) {
  Card c1 = cards.back();
  int c1_score_r = c1.sides[(c1.direction + 1) % 4];
  int c2_score_l = c2.sides[(c2.direction + 3) % 4];
 /* 
  if (cards.back().position > 3) {
    Card card_up = cards[cards.back().position - 3];
    int card_up_score_d = card_up.sides[(c1.direction + 2) % 4];
    int c2_score_u = c2.sides[c2.direction % 4];
    
    return (c1_score_r + c2_score_l == 0 && card_up_score_d + c2_score_u == 0);
  }
*/
  return (c1_score_r + c2_score_l == 0);
}

bool fitsBelow(Card& c1, Card& c2) {
  int c1_score = c1.sides[(c1.direction + 2) % 4];
  int c2_score = c2.sides[c2.direction % 4];
  return (c1_score + c2_score == 0);
}

// c1 left, c2 right
std::vector<Position> getPairs(std::vector<Position>& singles) {
  std::vector<Position> pairs;

  // Test which cards can attach to right of the card
  for (int i=0; i<singles.size(); i++) {
    Card card1 = singles[i].cards[0];
    for (int j=0; j<singles.size(); j++) {
      for (int r1=0; r1<4; r1++) {
        card1.direction++;
        for (int r2=0; r2<4; r2++) {
          Card card2 = singles[j].cards[0];

          // 'card' is left, 'card2' is right
          if (fitsRight(singles[i].cards, card2)) {
            //card1.direction  = (card1.direction  + 1) % 4;
            //card2.direction = (card2.direction + 3) % 4;
            Position pair;
            pair.cards.emplace_back(card1);
            pair.cards.emplace_back(card2);

            pairs.emplace_back(pair);
          }
          card2.direction++;
        }
      }
    }
  }

  return pairs;
}


std::vector<int> getUsedCards(Position& pos) {
  std::vector<int> used;
  for (int i=0; i<pos.cards.size(); i++)
    used.emplace_back( pos.cards[i].cardID );
  return used;
}

std::vector<Position> getBiggerPositions(std::vector<Position>& positions, Card (&cards)[9]) {
  std::vector<Position> new_positions;
  for (Position pos : positions) {
    Card card1;

    // If card is in the right edge of the 3x3 grid
    // the next card should go below the leftmost card
    bool need_right = true;
    if (pos.cards.back().position % 3 == 2) {
      need_right = false;
      card1 = pos.cards[pos.cards.back().position - 2]; // The leftmost card at bottom row
    }

    // Get already used cardID's
    std::vector<int> used = getUsedCards(pos); 

    // Rotate every other card full revolution and test
    // if it fits to the right side of rightmost card
    for (int c=0; c<9; c++) {

      // Do not reuse cards that are already used
      if (std::count(used.begin(), used.end(), c))
        continue;

      Card card2 = cards[c];
      for (int i=0; i<4; i++) {
        bool is_position = false;

        if (need_right)
          is_position = fitsRight(pos.cards, card2);
        else
          is_position = fitsBelow(card1, card2);
          
        if (is_position) {
          Position new_pos;
          new_pos.cards = pos.cards;
          new_pos.cards.emplace_back(card2);
          
          // Update card positions
          for (int p=0; p<new_pos.cards.size(); p++)
            new_pos.cards[p].position = p;

          new_positions.emplace_back(new_pos);
        }
        card2.direction++;
      }
    }
  }
  return new_positions;
}

int main() {
  Card cards[9];
  initializeCards(cards); // Initializes all cards with correct values
  std::vector<Position> positions;
  
  for (Card card : cards) {
    Position pos;
    pos.cards.emplace_back(card); 
    positions.emplace_back(pos);
  }
  
  positions = getPairs(positions);
  int cards_in_grid = 2;
  while (cards_in_grid < 9) {
    positions = getBiggerPositions(positions, cards);
    positions[0].PrintPosition();
    cards_in_grid++;
  }

  for (Position position: positions) {
    if (position.IsSolved()) {
      std::cout << "SOLVED!\n";
      position.PrintPosition();
      return 0;
    }
  }
  
  return 1;
}
/*  //while (positions.size() < 9) {
    //positions = 
  Position pos;


  position.SortPosition();
  position.PrintPosition();

  Position initial_pos = position;

  BruteForce(position);

  return 0;
}*/
