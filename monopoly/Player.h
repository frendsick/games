class Player {
  private:
    int playerID; 
    int hotelCount;    // How many hotels player has built
    int houseCount;    // How many houses player has built
    int money;          // How much money the player has
    int position;       // Player's position on the game board. 0 = Start, 10 = Jail etc.
    std::string model;  // Horse, hat, dog etc.
    std::string name;

  public:
    // Constructors
    Player() { hotelCount = 0, houseCount = 0, money = 1500; position = 0; }
    Player(std::string m) { model = m; hotelCount = 0, houseCount = 0, money = 1500; position = 0; }

    // Getters and Setters
    void SetPlayerID(int id) {
      playerID = id;
    }

    void SetHotelCount(int c) {
      hotelCount = c;
    }

    void SetHouseCount(int c) {
      houseCount = c;
    }

    void SetModel(std::string m) {
      model = m;
    }

    void SetName(std::string n) {
      name = n;
    }

    // TODO
    void MakeMove () {
      position++; // Just a temporary action
    }
};
