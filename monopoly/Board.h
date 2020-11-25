class Board {
  private:
    int mandatoryPayments[2] = { 4, 38 };
    int payments[40];
    std::string positions[40];

  public:
    // GETTERS AND SETTERS
    void SetPayment(int pos, int amount) {
      payments[pos] = amount;
    }

    void SetPosition(int pos, std::string text) {
      positions[pos] = text;
    }

    void Print() {
      std::cout << "\n---PELILAUTA---\n";
      for (int i=0; i<40; i++) {
        std::cout << positions[i] << ": " << payments[i] << "€\n";
      }
    }
};
