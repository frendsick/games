void drawCard(int &position, Card (&cards)[16]);

class Player {
  private:
    int playerID; 
    int doubleCount;
    int hotelCount;    // How many hotels player has built
    int houseCount;    // How many houses player has built
    int money;          // How much money the player has
    int position;       // Player's position on the game board. 0 = Start, 10 = Jail etc.
    int visitedPositions[40] = {0};
    std::string model;  // Horse, hat, dog etc.
    std::string name;

  public:
    // CONSTRUCTORS
    Player() { doubleCount = 0, hotelCount = 0, houseCount = 0, money = 1500; position = 0; }
    Player(std::string m) { model = m; doubleCount = 0, hotelCount = 0, houseCount = 0, money = 1500; position = 0; }

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
    void MakeMove(int (&dices)[2], Board &board, Card (&chanceCards)[16], Card (&communityCards)[16]) {
      // Test if player threw a pair
      if (dices[0] == dices[1]) {
        if (doubleCount < 2)
          doubleCount++;
        else {
          position = 10;  // If player threw 3 pairs in a row, go to jail
          doubleCount = 0;
          return;
        }
      }
      else
        doubleCount = 0;
      
      int diceSum = dices[0] + dices[1];
      position = (position + diceSum) % 40;
      std::string squareName = board.GetPosition(position);
      
      if (squareName == "Mene vankilaan")
        position = 10;
      else if (squareName == "Sattuma")
        drawCard(position, chanceCards);     // Changes players position if Sattuma-card requires it
      else if (squareName == "Yhteismaa")
        drawCard(position, communityCards);  // Changes players position if Yhteismaa-card requires it
    }

    void Print() {
      std::cout << name << " | " << model << " | " << money << "€ | Hotels: " << hotelCount << " | Houses: " <<  houseCount << " | Position: " <<  position << std::endl;
    }
};
