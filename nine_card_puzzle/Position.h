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

      for (int i=0; i<this->cards.size(); i++) {
        top_line    += " ___________ ";
        top         += cards[i].GetRow('T');
        row1        += cards[i].GetRow('1');
        row2        += cards[i].GetRow('2');
        row3        += cards[i].GetRow('3');
        bottom      += cards[i].GetRow('B');
        bottom_line += "|___________|";
        
        if (i % 3 == 2 || i == this->cards.size() - 1) {
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
        if (i % 3 != 2) {
          // Break if is not match
          if (!CheckNeighbor(cards[i], cards[i+1])) {
            solved = false; break;
          }
        }
      }

      return solved;
    }

    void SwapCards(int i, int j) {
      int temp_pos = this->cards[i].position;
      this->cards[i].position = this->cards[j].position;
      this->cards[j].position = temp_pos;
      std::swap(this->cards[i], this->cards[j]);
    }
    
};
