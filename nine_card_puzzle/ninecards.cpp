#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
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

// GLOBALS for counting comparisons and found possible combinations for each card amount
int AMOUNT_OF_COMPARISONS = 0;
int POSSIBILITIES[9]      = {0}; // Zero all nine elements

void initializeCards(Card (&cards)[9]) {
  std::cout << "Initializing cards..." << std::endl;

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

  std::cout << "All cards are initialized!" << std::endl;
}

int getRotationFromArguments(int argc, char* argv[]) {
  if (argc > 1) {
    #include <cstdlib> // std::strtol
    int rotation = std::strtol(argv[1], nullptr, 10); // The first argument in numerical form
    if (rotation > 4)
      rotation = 4;
    return rotation;
  }
  return 0;
}

// Put every single card to a vector of Position objects
std::vector<Position> cardsToPositions(Card (&cards)[9], int rotations) {
  std::vector<Position> positions;
  for (Card card : cards) { // Loop through cards
    for (int i=0; i<rotations+1; i++) { // Rotate card 4 times to get all combinations
      Position pos;
      pos.cards.emplace_back(card);
      positions.emplace_back(pos);
      card.direction++;
    }
  }
  return positions;
}

bool fitsBelow(Card& c1, Card& c2) {
  int c1_score = c1.sides[(c1.direction + 2) % 4];
  int c2_score = c2.sides[c2.direction % 4];
  return (c1_score + c2_score == 0);
}

// Test can a card be put to the right of rightmost card
bool fitsRight(std::vector<Card>& cards, Card& c2) {
  Card c1 = cards.back();
  int c1_score_r = c1.sides[(c1.direction + 1) % 4];
  int c2_score_l = c2.sides[(c2.direction + 3) % 4];

  // If the last inserted card is at position 3 or onwards
  // then the program checks if the card above mathces as well
  if (c1.position > 3) {
    Card c3 = cards[c1.position - 2];
    return (fitsBelow(c3, c2) && c1_score_r + c2_score_l == 0);
  }
  
  return (c1_score_r + c2_score_l == 0); // Only check horizontal match
}

// Returns vector of integers including all used cards in currently handled position
std::vector<int> getUsedCards(Position& pos) {
  std::vector<int> used;
  for (int i=0; i<pos.cards.size(); i++)
    used.emplace_back( pos.cards[i].cardID );
  return used;
}

// Returns vector of Position objects which includes all possible combinations
// of cards with one more card compared to 'positions' parameter
std::vector<Position> getBiggerPositions(std::vector<Position>& positions, Card (&cards)[9]) {
  std::vector<Position> new_positions;

  // Loop through already known possible combinations of cards
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
        continue; // Go to the next iteration of the FOR loop

      Card card2 = cards[c];
      for (int i=0; i<4; i++) {
        bool is_possible = false; // Can card1 and card2 be neighbors

        if (need_right)
          is_possible = fitsRight(pos.cards, card2);
        else
          is_possible = fitsBelow(card1, card2);
          
        // If card1 and card2 could be neighbors, add card2 to new_positions
        if (is_possible) {
          Position new_pos;
          new_pos.cards = pos.cards;
          new_pos.cards.emplace_back(card2);
          
          // Update card positions
          for (int p=0; p<new_pos.cards.size(); p++)
            new_pos.cards[p].position = p;

          new_positions.emplace_back(new_pos);
        }
        // Rotate tested card for 4 times (for loop)
        card2.direction++;
      }
    }
  }
  return new_positions; // The vector of possible combinations of cards
}

int main(int argc, char* argv[]) {
  
  Card cards[9];
  initializeCards(cards); // Initializes all cards with correct values
  
  int initial_rotations = getRotationFromArguments(argc, argv);
  
  auto start_timer = std::chrono::high_resolution_clock::now(); // Timer for the solve
  
  // Put every all cards to Position vector two different ways
  std::vector<Position> positions = cardsToPositions(cards, initial_rotations);
  
  // getBiggerPositions returns all possible combinations of cards
  // which has one more card inserted right from rightmost card or
  // below the leftmost card if rightmost card is at the edge of 3x3 grid
  for (int i=1; i<9; i++) {
    positions = getBiggerPositions(positions, cards);
    POSSIBILITIES[i] = positions.size();
  }

  // Test all returned 3x3 grids from getBiggerPositions
  // and notify if solution was found
  int solutions = 0;
  for (Position position: positions) {
    if (position.IsSolved()) {
      solutions++;
      std::cout << "\n\nFound solution " << solutions << std::endl;

      position.PrintPosition(); // Print the position
    }
  }
  // End the timer
  auto stop_timer = std::chrono::high_resolution_clock::now();
  auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop_timer - start_timer);

  if (solutions > 0)
    std::cout << "\n\nIt took " << duration.count() << " microseconds to find " << solutions << " solutions\n";
  else
    std::cout << "No solution found :(\n";
  return 0;
}
