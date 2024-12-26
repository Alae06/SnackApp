import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Snack Stand")
window.geometry("800x600")

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

selected_item = tk.StringVar()
quantity = tk.StringVar(value="1")
total = 0.0

def create_widgets():
    global order_text

    left_frame = tk.Frame(window, bg='#FFE4E1', width=400)
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    right_frame = tk.Frame(window, bg='#FFF0F5', width=400)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    menu_label = tk.Label(
        left_frame,
        text="MENU",
        font=('Arial', 20, 'bold'),
        bg='#FF6B6B',
        fg='white',
        pady=10,
        width=20
    )
    menu_label.pack(pady=10)

    menu_frame = tk.Frame(left_frame, bg='#FFE4E1')
    menu_frame.pack(pady=10)

    for item in menu:
        price = menu[item]
        item_frame = tk.Frame(
            menu_frame,
            bg='#FFF0F5',
            padx=10,
            pady=5,
            relief=tk.RAISED,
            borderwidth=2
        )
        item_frame.pack(fill=tk.X, padx=20, pady=5)

        tk.Label(
            item_frame,
            text=item,
            font=('Arial', 12, 'bold'),
            bg='#FFF0F5'
        ).pack(side=tk.LEFT, padx=10)

        tk.Label(
            item_frame,
            text=str(price) + "DH",
            font=('Arial', 12),
            bg='#FFF0F5',
            fg='#FF6B6B'
        ).pack(side=tk.RIGHT, padx=10)

    tk.Label(
        right_frame,
        text="COMMANDER",
        font=('Arial', 20, 'bold'),
        bg='#FF6B6B',
        fg='white',
        pady=10,
        width=20
    ).pack(pady=10)

    order_frame = tk.Frame(right_frame, bg='#FFF0F5')
    order_frame.pack(pady=20)

    tk.Label(
        order_frame,
        text="Choisir un produit:",
        font=('Arial', 12),
        bg='#FFF0F5'
    ).pack(pady=5)

    product_menu = tk.OptionMenu(order_frame, selected_item, *menu.keys())
    product_menu.config(width=15, font=('Arial', 12))
    product_menu.pack(pady=5)

    tk.Label(
        order_frame,
        text="Quantité:",
        font=('Arial', 12),
        bg='#FFF0F5'
    ).pack(pady=5)

    quantity_spinbox = tk.Spinbox(
        order_frame,
        from_=1,
        to=10,
        textvariable=quantity,
        width=5,
        font=('Arial', 12)
    )
    quantity_spinbox.pack(pady=5)

    tk.Button(
        order_frame,
        text="Ajouter à la commande",
        command=add_to_order,
        font=('Arial', 12, 'bold'),
        bg='#FF6B6B',
        fg='white',
        pady=5
    ).pack(pady=20)
    order_text = tk.Text(
        right_frame,
        height=10,
        width=35,
        font=('Arial', 10)
    )
    order_text.pack(pady=10)

    tk.Button(
        right_frame,
        text="Finaliser la commande",
        command=finalize_order,
        font=('Arial', 12, 'bold'),
        bg='#4A4A4A',
        fg='white',
        pady=5
    ).pack(pady=10)

def add_to_order():
    global total
    if selected_item.get() == "":
        messagebox.showwarning("Erreur", "Veuillez sélectionner un produit!")
        return

    item = selected_item.get()
    amount = int(quantity.get())
    price = menu[item]
    subtotal = price * amount

    total = total + subtotal

    order_text.insert(tk.END, item + " x" + str(amount) + " = " + str(subtotal) + "DH\n")

def finalize_order():
    global total
    if total == 0:
        messagebox.showwarning("Erreur", "Votre commande est vide!")
        return

    message = "Total de votre commande: " + str(total) + "DH\nMerci de votre achat!"
    messagebox.showinfo("Commande finalisée", message)

    total = 0
    order_text.delete(1.0, tk.END)
    quantity.set("1")
    selected_item.set("")

create_widgets()

window.mainloop()

