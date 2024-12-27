import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Snack")
window.configure(bg='#FFE4E1')

menu = {
    "Pizza": 40.00,
    "Tacos": 49.00,
    "Sandwich": 30.00,
    "Burger": 32.00,
    "Frites": 15.00,
    "Nuggets": 35.00,
    "Soda": 15.00,
    "Limonade": 18.00
}

A = {}

titre = tk.Label(
    window,
    text="Menu de snack",
    font=('Arial', 24, 'bold'),
    bg='#FF6B6B',
    fg='white',
    pady=10,
    width=30
)
titre.pack(pady=10)

menu_affichage = tk.Frame(window, bg='#FFE4E1')
menu_affichage.pack(padx=20, pady=10)

row = 0
col = 0
for item in menu:
    item_frame = tk.Frame(
        menu_affichage,
        bg='#FFF0F5',
        padx=10,
        pady=10,
        relief=tk.RAISED,
        borderwidth=2
    )
    item_frame.grid(row=row, column=col, padx=10, pady=5)

    tk.Label(
        item_frame,
        text=item,
        font=('Arial', 12, 'bold'),
        bg='#FFF0F5',
        fg='#4A4A4A'
    ).pack()

    tk.Label(
        item_frame,
        text=str(menu[item]) + "DH",
        font=('Arial', 11),
        bg='#FFF0F5',
        fg='#FF6B6B'
    ).pack()

    spinbox = tk.Spinbox(
        item_frame,
        from_=0,
        to=10,
        width=5,
        font=('Arial', 10),
        bg='white',
    )
    spinbox.pack(pady=5)
    A[item] = spinbox

    col = col + 1
    if col > 3:
        col = 0
        row = row + 1

def calculer_totale():
    totale = 0
    commande = "AJOUTER:\n\n"
    items = False

    for item in A:
        quantité = int(A[item].get())
        if quantité > 0:
            items = True
            item_total = quantité * menu[item]
            totale = totale + item_total
            commande = commande + f"{item}: {quantité} x {menu[item]}DH = {item_total}DH\n"

    if items == False:
        messagebox.showwarning("commande", "SELECTIONNER QUELQUE CHOSE!")
        return

    commande = commande + f"\nTotale: {totale}DH"
    messagebox.showinfo("Totale", commande)

def annuler_commande():
    for item in A:
        A[item].delete(0, tk.END)
        A[item].insert(0, "0")

calcule_button = tk.Button(
    window,
    text="Calculer Total",
    command=calculer_totale,
    font=('Arial', 12, 'bold'),
    bg='#FF6B6B',
    fg='white',
    padx=20,
    pady=10,
)
calcule_button.pack(pady=20)

annuler_button = tk.Button(
    window,
    text="SUPPRIMER",
    command=annuler_commande,
    font=('Arial', 12),
    bg='#4A4A4A',
    fg='white',
    padx=20,
    pady=5,
)
annuler_button.pack(pady=10)

window.mainloop()

