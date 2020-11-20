/* init.h initializes the starting position of the game
 * - Players
 * - Chance cards (Sattuma)
 * - Community Chest cards (Yhteismaa)
 */

void newGame(Board &board, std::vector<Player> &players, Card &chanceCards[16], Card &communityCards[16]) {
  initBoard(board);
  initPlayers(players);
  initChance(chanceCards);
  initCommunity(communityCards);
}

void initBoard(Board &board) {
  // Array of positions (squares) on the board
  std::string positions[40] = {
    "Lähtö",
    "Korkeavuorenkatu",
    "Yhteismaa",
    "Kasarmikatu",
    "Maksa tulovero",
    "Pasilan asema",
    "Rantatie",
    "Sattuma",
    "Kauppatori",
    "Esplanadi",
    "Vankila",
    "Hämeentie",
    "Sähkölaitos",
    "Siltasaari",
    "Kaisaniemenkatu",
    "Sörnäisten asema",
    "Liisankatu",
    "Yhteismaa",
    "Snellmaninkatu",
    "Unioninkatu",
    "Vapaa pysäköinti",
    "Lönnrotinkatu",
    "Sattuma",
    "Annankatu",
    "Simonkatu",
    "Rautatieasema",
    "Mikonkatu",
    "Aleksanterinkatu",
    "Vesilaitos",
    "Keskuskatu",
    "Mene vankilaan",
    "Tehtaankatu",
    "Eira",
    "Yhteismaa",
    "Bulevardi",
    "Tavara-asema",
    "Sattuma",
    "Mannerheimintie",
    "Maksa lisävero",
    "Erottaja"
  };

  board.positions = positions;
}

// TODO
void initPlayers(Player &players) {
  return;
}

void initChance(Card &chanceCards[16]) {
  std::string cardTexts[16] = {
    // Property payments
    "Kaikkia kiinteistöjäsi on korjattava. Maksu kustakin talosta 25€, kustakin hotellista 100€.",
    "Maksa korvausta katujen kunnossapidosta 40€ talosta ja 115€ hotellista.",
    
    // Collect money + perks
    "Maksu rakennuslainastasi, peri 150€.",
    "Olet voittanut ristisanakilpailun, peri 100€.",
    "Saat nostaa pankista säästötilikorkoa 50€.",
    "Vapaudut vankilasta."

    // Move to a location
    "Jatka matkaasi \"lähtö\"-ruutuun.",
    "Jatka matkaasi Erottajalle.",
    "Jatka matkaasi Hämeentielle. Jos kuljet \"lähtö\"-ruudun kautta, saat periä 200€.",
    "Jatka matkaasi Simonkadulle. Jos kuljet \"lähtö\"-ruudun kautta saat periä 200€.",
    "Käväise Sörnäisten-asemalla. Jos kuljet \"lähtö\"-ruudun kautta, saat periä 200€.",
    "Käväise Tavara-asemalla. Jos kuljet \"lähtö\"-ruudun kautta, saat periä 200€."
    "Mene kolme askelta taaksepäin.",
    "Mene vankilaan! Mene suoraan vankilaan kulkematta \"lähtö\"-ruudun kautta.",

    // Payments
    "Maksa sakkoa ylinopeudesta 15€.",
    "Maksa koulumaksuja 150€.",
  };

  int cardPayments[16] = { 0, 0, 150, 100, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, -15, -150 };

  for (int i=0; i<16; i++) {
    card.text = cardTexts[i];
    card.type = "Sattuma";
    card.payment = cardPayments[i];

    // Movement cards are indexes 6-13
    if (i >= 6 && i <= 13) {
      card.mustMove = true;

      switch (i) {
        case 6:
          card.movePosition = 0;  // Start square (Lähtö)
          break;
        case 7:
          card.movePosition = 39; // Erottaja
          break;
        case 8:
          card.movePosition = 11; // Hämeentie
          break;
        case 9:
          card.movePosition = 24; // Simonkatu
          break;
        case 10:
          card.movePosition = 15; // Sörnäisten-asema
          break;
        case 11:
          card.movePosition = 35; // Tavara-asema
          break;
        case 12:
          card.movePosition = -3; // 3 steps backwards
          break;
        case 13:
          card.movePosition = 20; // Vankila
          break;
        default:
          std::cout << "Sattumakortin '" << card.text << "' alustaminen ei onnistunut!" << std::endl;
      }
    }
  }
}

// TODO
void initCommunity(Card &communityCards[16]) {
  
}
