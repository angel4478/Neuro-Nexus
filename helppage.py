def box(pair1, pair2):
    print("-" * 51)
    for i, j in zip(pair1, pair2):
        print("|  " + i + "  ->  " + j + "  |")
    print("-" * 51)
    return

def info():
    cards = [".------.    .------.",
    "|N.--. |    |N.--. |",
    "| :(): |    | :(): |",
    "| ()() |    | ()() |",
    "| '--'N|    | '--'N|",
    "`------'    `------'"]
    backcards = [".------.    .------.",
    "|      |    |      |",
    "|      |    |      |",
    "|      |    |      |",
    "|      |    |      |",
    "`------'    `------'"]
    print("Step 1: Pick Two Cards")
    print("-" * 25)
    for i in backcards:
        print("|  " + i + "  |")
    print("-" * 25)
    
    print("A) If both cards are identical, they will stay face up")
    print("Example: ")
    box(cards, cards)
    
    print("B) If the cards are different, they will face down again")
    print("Example: ")
    box(cards, backcards)

    print("Step 2: Continue picking pairs until all cards are face up")
    return

info()