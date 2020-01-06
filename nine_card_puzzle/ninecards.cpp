#include <iostream>
#include <vector>

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
 *    Side 1 has two tops, R+M  ==> 6  (4 + 2)
 *    Side 2 has one top        ==> 2
 *    Side 3 has two bottoms, R+M ==> -3 (-1 -2)
 *
 *    // INITIALIZATION
 *    Card card4(4, -7, 6, 2, -3);   // Params: cardID, s0, s1, s2, s3
 */

class Card {
  public:
    int cardID;
    int sides[4];
    int direction;  // How many times the card is rotated anticlockwize
    int position;   // This cards position in 3x3 matrix, 0 = UP-LEFT, 2 = UP-RIGHT, 5 = MID-RIGHT etc.
  
    // Default constructor zeroes card's direction
    Card() { direction = 0; }

    // Returns the glass pieces for side rows
    std::string GetSideRow(const char& row) {
      std::string side = "";
      int s = (row == 'R') ? (this->direction + 1) % 4 : (this->direction + 3) % 4; 

      switch (sides[s]) {
        case 2:
          side = " T "; break;
        case 3:
          side = "TT "; break;
        case 6:
          side = " TT"; break;
        case 7:
          side = "TTT"; break;
        case -2:
          side = " B "; break;
        case -3:
          side = " BB"; break;
        case -6:
          side = "BB "; break;
        case -7:
          side = "BBB"; break;
      }

      return side;
    }

    // Return line to ASCII art representation of card
    std::string GetRow(const char& r) {
      std::string row = "";
      std::string el  = " |\n| "; // End line and start a new one
      std::string sp  = "       ";
      std::string st  = "| ";     // Start
    
      // Handle middle rows here
      if (r == 'M') {
        std::string l = this->GetSideRow('L');
        std::string r = this->GetSideRow('R');

        // Construct the rows
        row = st + l.at(0) + sp + r.at(2) + el + l.at(1) + sp + r.at(1) + el + l.at(2) + sp + r.at(0) + " |";
        return row;
      }

      // If bottom row is asked, increment two to direction
      int increment = (r == 'B') ? 2 : 0;

      int side = (this->direction + increment) % 4;

      switch (sides[side]) {
        case 2:
          row = "|     T     |"; break;
        case 3:
          if (r == 'T') {
            row = "|     T T   |"; break;
          }
          row = "|   T T     |"; break;
        case 6:
          if (r == 'T') {
            row = "|   T T     |"; break;
          }
          row = "|     T T   |"; break;
        case 7:
          row = "|   T T T   |"; break;
        case -2:
          row = "|     B     |"; break;
        case -3:
          if (r == 'T') {
            row = "|   B B     |"; break;
          }
          row = "|     B B   |"; break;
        case -6:
          if (r == 'T') {
            row = "|     B B   |"; break;
          }
          row = "|   B B     |"; break;
        case -7:
          row = "|   B B B   |"; break;
      }
      return row;
    }
    
    /* Card ASCII art. x = top or bottom of glass (T/B)
     *  ___________
     * |   x x x   |
     * | x       x |
     * | x       x |
     * | x       x |
     * |   x x x   |
     * |___________|
     */ 

    // Returns T's or B's to ASCII art presentation of a card
    // row ==> 'T' or 'B' (TOP or BOTTOM) or 'M' (THREE MIDDLE ROWS)
    void PrintCard() {

      // Print sides numerically
      std::cout << "\nCard " << cardID << " sides: ";
      for (int side: sides)
        std::cout << side << " ";
      std::cout << std::endl;
      
      // Print card as an ASCII art
      std::cout << " ___________" << std::endl;
      std::cout << this->GetRow('T') << std::endl;
      std::cout << this->GetRow('M') << std::endl;
      std::cout << this->GetRow('B') << std::endl;
      std::cout << "|___________|" << std::endl;
    }
};

class Position {
  public:
    std::vector<Card> cards;

    
};

void initializeCards(Card (&cards)[9]) {
  std::cout << "Initializing cards" << std::endl;

  // Initialize cardID's
  for (int i=0; i<9; i++)
    cards[i].cardID = i;
  
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

  // Print all sides of cards
  for (Card card : cards)
    card.PrintCard();
}

int main() {
  Card cards[9];
  initializeCards(cards); // Initializes all cards with correct values

  return 0;
}
