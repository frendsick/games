void throwDices(int (&dices)[2]);
const bool LOVE_JAIL = false;  // Are players in jail as long as possible?

class Player {
  private:
    bool inJail;
    int playerID; 
    int doubleCount;
    int hotelCount;     // How many hotels player has built
    int houseCount;     // How many houses player has built
    int jailThrowCount; // How many times player threw dices while in jail
    int money;          // How much money the player has
    int position;       // Player's position on the game board. 0 = Start, 10 = Jail etc.
    int visitedPositions[40] = {0};
    std::string model;  // Horse, hat, dog etc.
    std::string name;

  public:
    // CONSTRUCTORS
    Player() { doubleCount = 0, hotelCount = 0, houseCount = 0, jailThrowCount = 0; money = 1500; position = 0; inJail = false; }
    Player(std::string m) { model = m; doubleCount = 0, hotelCount = 0, houseCount = 0, jailThrowCount = 0; money = 1500; position = 0; inJail = false; }

    // GETTERS AND SETTERS
    void SetPlayerID(int id) { playerID = id; }
    void SetHotelCount(int c) { hotelCount = c; }
    void SetHouseCount(int c) { houseCount = c; }
    void SetModel(std::string m) { model = m; }
    void SetName(std::string n) { name = n; }
    void UpdateVisitedPositions(int p) { visitedPositions[p]++; }

    std::string GetName() { return name; }
    int GetID() { return playerID; }
    int GetPosition() { return position; }
    int GetPositionVisitedAmount(int p) { return visitedPositions[p]; }

    // METHODS
    
    // Move where card requires
    void CardMove(Card card) {
      if (card.GetMovePosition() < 0) { // Mene 3 askelta taaksepäin
        position -= card.GetMovePosition();
        return;
      }
        
      position = card.GetMovePosition();
      if (position == 10) {
        inJail = true;
        doubleCount = 0;
      }
    }
    
    // Draw Sattuma or Yhteismaa card
    void DrawCard(Card (&cards)[16]) {
      int i = rand() % 16;

      // Move where card requires
      if (cards[i].MustMove())
        CardMove(cards[i]);
    }

    // Calculate player's new position
    void GetNewPosition(int (&dices)[2], Board &board, Card (&chanceCards)[16], Card (&communityCards)[16]) {
      int diceSum = dices[0] + dices[1];
      position = (position + diceSum) % 40;
      std::string squareName = board.GetPosition(position);
      
      if (squareName == "Mene vankilaan") {
        inJail = true;
        position = 10;
        doubleCount = 0;
      }
      else if (squareName == "Sattuma")
        DrawCard(chanceCards);     // Changes players position if Sattuma-card requires it
      else if (squareName == "Yhteismaa")
        DrawCard(communityCards);  // Changes players position if Yhteismaa-card requires it
    }

    void JailMove(int (&dices)[2], Board &board, Card (&chanceCards)[16], Card (&communityCards)[16]) {
      // Player gets to move from jail by throwing a pair or by trying three times in a row
      if (dices[0] == dices[1] || jailThrowCount >= 2) {
        inJail = false;
        jailThrowCount = 0;
        GetNewPosition(dices, board, chanceCards, communityCards);
        return;
      }

      jailThrowCount++;
    }

    void DoubleMove(int (&dices)[2], Board &board, Card (&chanceCards)[16], Card (&communityCards)[16]) {
      // If player threw 3 pairs in a row, go to jail
      if (doubleCount >= 2) {
        position = 10; 
        doubleCount = 0;
        return;
      }
      
      // Move to new position and make a new move
      GetNewPosition(dices, board, chanceCards, communityCards);
      throwDices(dices);
      MakeMove(dices, board, chanceCards, communityCards);
      doubleCount++;
    }

    void NormalMove(int (&dices)[2], Board &board, Card (&chanceCards)[16], Card (&communityCards)[16]){
        doubleCount = 0;
        GetNewPosition(dices, board, chanceCards, communityCards);
    }

    void MakeMove(int (&dices)[2], Board &board, Card (&chanceCards)[16], Card (&communityCards)[16]) {
      // If player is in jail
      if (inJail && LOVE_JAIL)
        JailMove(dices, board, chanceCards, communityCards);    // Player wants to be in jail as long as possible

      // If player threw a pair
      else if (dices[0] == dices[1])
        DoubleMove(dices, board, chanceCards, communityCards);

      else
        NormalMove(dices, board, chanceCards, communityCards);
    }

    void Print() {
      std::cout << name << " | " << model << " | " << money << "€ | Hotels: " << hotelCount << " | Houses: " <<  houseCount << " | Position: " <<  position << std::endl;
    }
};
