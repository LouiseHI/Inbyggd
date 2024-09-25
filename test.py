print("Välkommen till multiplikationskalkulatorn!")
def multiplikation():
    tal_val = input("vilka siffror vill du multiplicera?: ").strip().split()
    user_numbers = [int(num) for num in tal_val]

    for num in user_numbers:
        print(f"\nMultiplikationstabellen för {num}:")
        for i in range(1, 11):
            print(f"{num} * {i} = {num * i}")

multiplikation()
