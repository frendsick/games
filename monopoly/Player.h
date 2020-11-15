class Player {
  private:
    int playerID;
    int position;       // Player's position on the game board. 0 = Start, 10 = Jail etc.
    int money;          // How much money the player has
    std::string model;  // Horse, hat, dog etc.

  public:
  // Default constructor zeroes player's position and sets money count to 1500
    Player() { position = 0; money = 1500; }

  // TODO
  void MakeMove () {
    position++; // Just a temporary action}
  }
