class Card {
  public:
    int cardID;
    int movePosition = -1;  // Position on the board (square)
    int payment;            // Payment on the square
    bool mustMove;          // Does card require the player to move
    bool moveBackwards;     // When card requires the player to move is the direction backwards
    
    std::string cardType;   // Sattuma or Yhteismaa
    std::string text;       // Text on the card

    // Constructor zeroes payment, moveBackwards and mustMove values
    Card() { payment = 0; moveBackwards = false; mustMove = false; }

};
