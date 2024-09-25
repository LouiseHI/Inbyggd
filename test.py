print("Välkommen till multiplikationskalkulatorn!")
def multiplikation():
    tal_val = input("vilka siffror vill du multiplicera?: ").strip().split()
    faktor = [int(tal) for tal in tal_val]

    for tal in faktor:
        print(f"\nMultiplikationstabellen för {tal}:")
        for i in range(1, 11):
            print(f"{tal} * {i} = {tal * i}")

multiplikation()
