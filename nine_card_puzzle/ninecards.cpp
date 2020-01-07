#include <iostream>
#include <vector>
#include <algorithm>

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
    std::string GetRow(const char& rowID) {
      std::string row = "";
      std::string sp  = "       ";
      std::string st  = "| ";     // Start
      std::string eol = " |";
    
      // Handle middle rows here
      if (rowID == '1' || rowID == '2' || rowID == '3') {
        std::string l = this->GetSideRow('L');
        std::string r = this->GetSideRow('R');
        
        // Construct row and return it afterwards
        switch (rowID) {
          case '1':
            return st + l.at(0) + sp + r.at(2) + eol;
          case '2':
            return st + l.at(1) + sp + r.at(1) + eol;
          case '3':
            return st + l.at(2) + sp + r.at(0) + eol; 
        }
      }

      // If bottom row is asked, increment two to direction
      int increment = (rowID == 'B') ? 2 : 0;

      int side = (this->direction + increment) % 4;

      switch (sides[side]) {
        case 2:
          row = "|     T     |"; break;
        case 3:
          if (rowID == 'T') {
            row = "|     T T   |"; break;
          }
          row = "|   T T     |"; break;
        case 6:
          if (rowID == 'T') {
            row = "|   T T     |"; break;
          }
          row = "|     T T   |"; break;
        case 7:
          row = "|   T T T   |"; break;
        case -2:
          row = "|     B     |"; break;
        case -3:
          if (rowID == 'T') {
            row = "|   B B     |"; break;
          }
          row = "|     B B   |"; break;
        case -6:
          if (rowID == 'T') {
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

    void PrintTop() {
      std::cout << " ___________" << std::endl;
      std::cout << this->GetRow('T') << std::endl;
    }

    void Print1Row()  { std::cout << this->GetRow('1') << std::endl; }

    void Print2Row()  { std::cout << this->GetRow('2') << std::endl; }

    void Print3Row()  { std::cout << this->GetRow('3') << std::endl; }

    void PrintBottom() {
      std::cout << this->GetRow('B') << std::endl;
      std::cout << "|___________|" << std::endl;
    }


    // Returns T's or B's to ASCII art presentation of a card
    // row ==> 'T' or 'B' (TOP or BOTTOM) or 'M' (THREE MIDDLE ROWS)
    void PrintCard() {

      /*
      // Print sides numerically
      std::cout << "\nCard " << cardID << " sides: ";
      for (int side: sides)
        std::cout << side << " ";
      std::cout << std::endl;
      */
      
      // Print card as an ASCII art
      this->PrintTop();
      this->Print1Row();
      this->Print2Row();
      this->Print3Row();
      this->PrintBottom();
    }
};

class Position {
  public:
    std::vector<Card> cards;
    
    // This method presumes that cards are sorted by their position
    void PrintPosition() {
      std::string top_line    = "";
      std::string top         = "";
      std::string row1        = "";
      std::string row2        = "";
      std::string row3        = "";
      std::string bottom      = "";
      std::string bottom_line = "";

      std::cout << "\nPrinting current position\n";

      for (int i=0; i<cards.size(); i++) {
        top_line    += " ___________ ";
        top         += cards[i].GetRow('T');
        row1        += cards[i].GetRow('1');
        row2        += cards[i].GetRow('2');
        row3        += cards[i].GetRow('3');
        bottom      += cards[i].GetRow('B');
        bottom_line += "|___________|";
        
        if (i % 3 == 2 || i == cards.size() - 1) {
          std::cout << top_line << std::endl << top << std::endl << row1 << std::endl << row2
            << std::endl << row3 << std::endl << bottom << std::endl << bottom_line << std::endl;
          top_line    = "";
          top         = "";
          row1        = "";
          row2        = "";
          row3        = "";
          bottom      = "";
          bottom_line = "";
        }
      }
    }

    void SortPosition() {
      std::sort(
        this->cards.begin(),
        this->cards.end(),
        [](Card a, Card b) { return a.position < b.position; }
      );
    }

    // TODO
    // I only need to check down and right for a match if I start match checking from UP-LEFT corner
    bool CheckNeighbor(Card card1, Card card2) {

      // std::cout << c1.position << ", " << c2.position << std::endl;
      int c1_score = 1337;
      int c2_score = 9001;
      
      // If cards are next to each other and they
      if (card2.position - card1.position == 1) { 
        c1_score  = card1.sides[(card1.direction + 1) % 4];
        c2_score  = card2.sides[(card2.direction + 3) % 4];
      }
      
      // If cards are on top of each other
      else if (card2.position - card1.position == 3) {
        c1_score  = card1.sides[(card1.direction + 2) % 4];
        c2_score  = card2.sides[card2.direction % 4];
      }
      
      if (c1_score + c2_score == 0) {
        // std::cout << "\n\nCards " << card1.cardID << " and " << card2.cardID << " are matching!\n";
        return true;
      }

      return false;
    }
    
    // Start from UP-LEFT corner and check if every card
    // matches with its rightward and downward neighbor
    bool IsSolved() {
      bool solved = true;
      for (int i=0; i<this->cards.size()-1; i++) {
        // Check every downward neighbor
        if (i < 6) {
          // Break if is not match
          if (!CheckNeighbor(cards[i], cards[i+3])) {
            solved = false; break;
          }
        }
        // Check rightward neighbor for every card exept for the rightmost
        else if (i % 3 != 2) {
          // Break if is not match
          if (!CheckNeighbor(cards[i], cards[i+1])) {
            solved = false; break;
          }
        }
      }

      return solved;
    }

    void SwapCards(int i) {
      Card temp_card;
      cards[i].position++;
      cards[i+1].position--;
      temp_card   = cards[i];
      cards[i]    = cards[i+1];
      cards[i+1]  = temp_card;
    }
    
    // TODO
    void BruteForce() {
      int current = 0;
      int checked_cards = 0;
      bool full_rev = false;

      while (checked_cards < 9) {
        // Rotate card at a time
        for (int i=0; i<9; i++) {
          this->cards[i].direction++;
          // If current card has rotated full revolution, rotate next card
          if (this->cards[i].direction % 4 != 0)
            break;

          // If last card has rotated full revolution
          else if (i == 8) {
            current++; full_rev = true;
          }
        }

        if (this->IsSolved()) {
          std::cout << "SOLVED!\n";
          this->PrintPosition();
          break;
        }
        
        else if (current == 7) {
          this->SwapCards(current);
          checked_cards++;
          current = 1;
        }
        
        // Move current card forward by one spot
        else if (full_rev) {
          this->SwapCards(current);
          this->PrintPosition();
          full_rev = false;
        }
      }
    }
};

// Utility function for sorting Card vectors by card positions
bool CompareCardPositions(Card c1, Card c2) { return (c1.position < c2.position); }

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

int main() {
  Card cards[9];
  initializeCards(cards); // Initializes all cards with correct values
  
  Position pos;
  std::vector<Position> positions;
  positions.emplace_back(pos);

  for (Card card : cards)
    positions[0].cards.emplace_back(card);

  positions[0].SortPosition();

  positions[0].BruteForce();

  return 0;
}
