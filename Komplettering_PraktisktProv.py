print("Välkommen till multiplikationskalkulatorn!")

def multiplikation():
    #la till en "split()" för att kunna dela upp den inmatade strängen
    tal_val = input("Vilket tal vill du multiplicera?: ").split()
    faktor = [int(tal) for tal in tal_val]

    for tal in faktor:
        print(f"\nMultiplikationstabellen för {tal}:")
        for i in range(1, 11):
            print(f"{tal} * {i} = {tal * i}")

multiplikation()
