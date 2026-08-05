houses={
  "Gryffindor":0,
  "Hufflepuff":0,
  "Ravenclaw":0,
  "Slytherin":0
}

def award_points(house, points=10, reason="general excellence", ledger=None):
    # Never use ledger={} as a default argument because the same dictionary would be reused across every function call.

    if ledger is None:
        ledger = {}

    ledger[house] = ledger.get(house, 0) + points

    print(f"{house} +{points} ({reason}) -> total {ledger[house]}")

    return ledger


led = award_points("Gryffindor")
led = award_points("Gryffindor", 50, "defeating a troll", led)
led = award_points("Slytherin", 30, ledger=led)
led=award_points("Hufflepuff",60,"defeafing a unicorn",led)

print("Final ledger:", led)