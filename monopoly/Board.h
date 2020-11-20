class Board {
  public:
    int mandatoryPayments[2] = { 4, 38 };
    int payments[40];
    std::string positions[40];

    void Print() {
      std::cout << "\n---PELILAUTA---\n";
      for (int i=0; i<40; i++) {
        std::cout << positions[i] << ": " << payments[i] << "€\n";
      }
    }
};
