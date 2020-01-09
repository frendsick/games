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
            return st + l.at(1) + "   " + std::to_string(this->cardID+1) + "   " + r.at(1) + eol;
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
