
def uri(auswahl, schaltung, U, R, I):
    if auswahl == "U":
        output = R * I
        print(output, "V")
        main()
    elif auswahl == "R":
        output = U / I
        print(output, "Ω")
        main()
    elif auswahl == "I":
        output = U / R
        print(output, "A")
        main()
    else:
        print("Fehler bei der Angabe eines Wertes!")
        main()

def werte(auswahl, schaltung):
    U = 0
    R = 0
    I = 0

    if auswahl == "U":
        while True:
            try:
                R = float(input("R: "))
                if R <= 0:
                    print("Huh? Ein negativer Widerstand? Los, probier\'s noch mal:")
                    True
                else:
                    break
            except ValueError:
                print("Bitte nur Zahlen angeben!")
        while True:
            try:
                I = float(input("I: "))
                break
            except ValueError:
                print("Bitte nur Zahlen angeben!")
    elif auswahl == "R":
        while True:
            try:
                U = float(input("U: "))
                break
            except ValueError:
                print("Bitte nur Zahlen angeben!")
        while True:
            try:
                I = float(input("I: "))
                break
            except ValueError:
                print("Bitte nur Zahlen angeben!")
    elif auswahl == "I":
        while True:
            try:
                R = float(input("R: "))
                if R <= 0:
                    print("Huh? Ein negativer Widerstand? Los, probier\'s noch mal:")
                    True
            except ValueError:
                print("Bitte nur Zahlen angeben!")
        while True:
            try:
                U = float(input("U: "))
                break
            except ValueError:
                print("Bitte nur Zahlen angeben!")
    else:
        print("Fehler bei der Auswahl")

    uri(auswahl, schaltung, U, R, I)

def main():
    print("Welchen Wert möchtest du ausrechnen? | U R I")
    auswahl = input().upper()

    print("Parallel/Reihen -schaltung | P R")
    schaltung = input().upper()

    print("Werte ohne Einheit angeben!")
    werte(auswahl, schaltung)
if __name__ == "__main__":
    main()
