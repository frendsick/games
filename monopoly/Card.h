class Card {
  private:
    int cardID;
    int movePosition = -1;  // Position on the board (square)
    int payment;            // Payment on the square
    bool mustMove;          // Does card require the player to move
    bool moveBackwards;     // When card requires the player to move is the direction backwards
    
    std::string type;       // Sattuma or Yhteismaa
    std::string text;       // Text on the card

  public:
    // Constructor zeroes payment, moveBackwards and mustMove values
    Card() { payment = 0; moveBackwards = false; mustMove = false; }
    
    // GETTERS AND SETTERS
    void SetCardID(int id) { cardID = id; }
    void SetMovePosition(int pos) { movePosition = pos; }
    void SetPayment(int p) { payment = p; }
    void SetMustMove() { mustMove = true; }
    void SetMoveBackwards() { moveBackwards = true; }
    void SetType(std::string t) { type = t; }
    void SetText(std::string t) { text = t; }

    int GetMovePosition() { return movePosition; }
    bool MustMove() { return mustMove; }
    std::string GetText() { return text; }
    std::string GetType() { return type; }
    

    // METHODS
    void Print() {
      std::cout << text << " : " << type << " : " << payment << "€";

      if (mustMove)
        std::cout << " : Liiku ruutuun " << movePosition;
      std::cout << std::endl;
    }
};
