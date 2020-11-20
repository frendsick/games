class Board {
  private:
    int mandatoryPayments[2];
    int payments[40];
    std::string positions[40];

  public:
    // Constructor
    Board () { mandatoryPayments = { 4, 38 }; } // "Maksa tulovero" and "Maksa lisävero" squares
};
