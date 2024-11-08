import tkinter as tk
from tkinter import ttk

def calc_u():
    root_u = tk.Tk()
    root_u.title("Just another URI Calc | U")
    root_u.bind('<Escape>', lambda e: root_u.destroy())
    root_u.protocol("WM_DELETE_WINDOW", root_u.iconify)
    root_u.geometry("360x240")

    label1 = ttk.Label(root_u, text='Widerstandswert | R', font=("Arial", 12))
    label1.pack(ipadx=10, ipady=10)

    R = tk.StringVar()
    textbox = ttk.Entry(root_u, textvariable=R)
    textbox.pack(fill='x', expand=True)
    R = label1.get()

    label2 = ttk.Label(root_u, text='Ampere Wert | I', font=("Arial", 12))
    label2.pack(ipadx=10, ipady=10)
    I = tk.StringVar()
    textbox = ttk.Entry(root_u, textvariable=I)
    textbox.pack(fill='x', expand=True)
    I = label2.get()

    output = R * I
    print(output, "V")

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
    root = tk.Tk()
    root.title("Just another URI Calc")
    root.bind('<Escape>', lambda e: root.destroy())
    root.protocol("WM_DELETE_WINDOW", root.iconify)
    root.geometry("720x480")

    label1 = ttk.Label(root, text='Moin!', font=("Arial",16))
    label2 = ttk.Label(root, text='Welchen Wert möchtest du ausrechnen?', font=("Arial", 12))
    label1.pack(ipadx=10, ipady=10)
    label2.pack(ipadx=5, ipady=5)

    button_u = ttk.Button(root, text="U", command=calc_u )
    button_r = ttk.Button(root, text="R", )
    button_i = ttk.Button(root, text="I",)

    button_u.pack(
        ipadx=5,
        ipady=5,
        expand=True,
        side = tk.LEFT
    )
    button_r.pack(
        ipadx=5,
        ipady=5,
        expand=False,
        side=tk.LEFT
    )
    button_i.pack(
        ipadx=5,
        ipady=5,
        expand=True,
        side=tk.LEFT
    )

    root.mainloop()

    print(" | U R I")
    auswahl = input().upper()

    print("Parallel/Reihen -schaltung | P R")
    schaltung = input().upper()

    print("Werte ohne Einheit angeben!")
    werte(auswahl, schaltung)
if __name__ == "__main__":
    main()
