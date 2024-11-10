import tkinter as tk
from tkinter import ttk, messagebox

def get_solv():
    if calc == 1:
        R = float(r.get())
        I = float(i.get())

        output = R * I

        root_get_u = tk.Tk()
        root_get_u.title("Just another URI Calc | Solve")
        root_get_u.bind('<Escape>', lambda e: root_get_u.destroy())
        root_get_u.protocol("WM_DELETE_WINDOW", root_get_u.destroy)
        root_get_u.geometry("360x240")

        label1 = ttk.Label(root_get_u, text=str(output) + " V", font=("Arial", 16))
        label1.pack(ipadx=10, ipady=10)

    elif calc == 2:
        U = float(u.get())
        I = float(i.get())

        output = U / I

        root_get_u = tk.Tk()
        root_get_u.title("Just another URI Calc | Solve")
        root_get_u.bind('<Escape>', lambda e: root_get_u.destroy())
        root_get_u.protocol("WM_DELETE_WINDOW", root_get_u.destroy)
        root_get_u.geometry("360x240")

        label1 = ttk.Label(root_get_u, text=str(output) + " Ω", font=("Arial", 16))
        label1.pack(ipadx=10, ipady=10)

    elif calc == 3:
        U = float(u.get())
        R = float(r.get())

        output = U / R

        root_get_u = tk.Tk()
        root_get_u.title("Just another URI Calc | Solve")
        root_get_u.bind('<Escape>', lambda e: root_get_u.destroy())
        root_get_u.protocol("WM_DELETE_WINDOW", root_get_u.destroy)
        root_get_u.geometry("360x240")

        label1 = ttk.Label(root_get_u, text=str(output) + " A", font=("Arial", 16))
        label1.pack(ipadx=10, ipady=10)

def calc_u():
    global calc, r, i
    root_u = tk.Tk()
    root_u.title("Just another URI Calc | U")
    root_u.bind('<Escape>', lambda e: root_u.destroy())
    root_u.protocol("WM_DELETE_WINDOW", root_u.destroy)
    root_u.geometry("360x240")

    calc = 1

    label1 = ttk.Label(root_u, text='Widerstand | R', font=("Arial", 12))
    label1.pack(ipadx=10, ipady=10)

    r = ttk.Entry(root_u)
    r.pack(expand=True)

    label2 = ttk.Label(root_u, text='Ampere | I', font=("Arial", 12))
    label2.pack(ipadx=10, ipady=10)

    i = ttk.Entry(root_u)
    i.pack(expand=True)

    button = ttk.Button(root_u, text="Lösung", command=get_solv)
    button.pack(pady=10)

def calc_r():
    global calc, u, i
    root_u = tk.Tk()
    root_u.title("Just another URI Calc | R")
    root_u.bind('<Escape>', lambda e: root_u.destroy())
    root_u.protocol("WM_DELETE_WINDOW", root_u.destroy)
    root_u.geometry("360x240")

    calc = 2

    label1 = ttk.Label(root_u, text='Spannung | U', font=("Arial", 12))
    label1.pack(ipadx=10, ipady=10)

    u = ttk.Entry(root_u)
    u.pack(expand=True)

    label2 = ttk.Label(root_u, text='Ampere | I', font=("Arial", 12))
    label2.pack(ipadx=10, ipady=10)

    i = ttk.Entry(root_u)
    i.pack(expand=True)

    button = ttk.Button(root_u, text="Lösung", command=get_solv)
    button.pack(pady=10)

def calc_i():
    global calc, u, r
    root_u = tk.Tk()
    root_u.title("Just another URI Calc | R")
    root_u.bind('<Escape>', lambda e: root_u.destroy())
    root_u.protocol("WM_DELETE_WINDOW", root_u.destroy)
    root_u.geometry("360x240")

    calc = 3

    label1 = ttk.Label(root_u, text='Spannung | U', font=("Arial", 12))
    label1.pack(ipadx=10, ipady=10)

    u = ttk.Entry(root_u)
    u.pack(expand=True)

    label2 = ttk.Label(root_u, text='Widerstand | R', font=("Arial", 12))
    label2.pack(ipadx=10, ipady=10)

    r = ttk.Entry(root_u)
    r.pack(expand=True)

    button = ttk.Button(root_u, text="Lösung", command=get_solv)
    button.pack(pady=10)

def main():
    def window_exit():
        close = messagebox.askyesno("Exit?", "Are you sure you want to exit?")

        if close:
            root.destroy()

    root = tk.Tk()
    root.title("Just another URI Calc")
    root.bind('<Escape>', lambda e: root.destroy())
    root.protocol("WM_DELETE_WINDOW", window_exit)
    root.geometry("720x480")

    label1 = ttk.Label(root, text='Moin!', font=("Arial",16))
    label2 = ttk.Label(root, text='Welchen Wert möchtest du ausrechnen?', font=("Arial", 12))
    label1.pack(ipadx=10, ipady=10)
    label2.pack(ipadx=5, ipady=5)

    button_u = ttk.Button(root, text="U", command=calc_u)
    button_r = ttk.Button(root, text="R",command=calc_r)
    button_i = ttk.Button(root, text="I", command=calc_i)

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
if __name__ == "__main__":
    main()
