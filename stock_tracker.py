import tkinter as tk
from tkinter import messagebox, filedialog

# ================= STOCK PRICES =================
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 300
}

portfolio = []

# ================= ADD STOCK =================
def add_stock():
    name = stock_entry.get().upper()
    qty = qty_entry.get()

    if name == "" or qty == "":
        messagebox.showerror("Error", "Enter stock and quantity")
        return

    if name not in stock_prices:
        messagebox.showerror("Error", "Stock not available")
        return

    try:
        qty = int(qty)
    except:
        messagebox.showerror("Error", "Quantity must be number")
        return

    portfolio.append((name, qty))
    listbox.insert(tk.END, f"{name} - {qty}")

    stock_entry.delete(0, tk.END)
    qty_entry.delete(0, tk.END)

# ================= CALCULATE =================
def calculate():
    total = 0

    for stock, qty in portfolio:
        total += stock_prices[stock] * qty

    result_label.config(text=f"Total Investment: ${total}")

# ================= SAVE FILE =================
def save_file():
    if not portfolio:
        messagebox.showerror("Error", "No data to save")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt")

    if file_path:
        with open(file_path, "w") as f:
            for stock, qty in portfolio:
                f.write(f"{stock} - {qty}\n")

        messagebox.showinfo("Saved", "File saved successfully")

# ================= GUI =================
window = tk.Tk()
window.title("📊 Stock Portfolio Tracker")
window.geometry("500x500")
window.config(bg="#e0f2fe")

tk.Label(window, text="📊 Stock Tracker",
         font=("Arial", 20, "bold"),
         bg="#e0f2fe", fg="#0369a1").pack(pady=10)

# Input
tk.Label(window, text="Stock Name",
         bg="#e0f2fe").pack()

stock_entry = tk.Entry(window)
stock_entry.pack(pady=5)

tk.Label(window, text="Quantity",
         bg="#e0f2fe").pack()

qty_entry = tk.Entry(window)
qty_entry.pack(pady=5)

# Buttons
tk.Button(window, text="➕ Add Stock",
          bg="#38bdf8",
          command=add_stock).pack(pady=10)

# List
listbox = tk.Listbox(window)
listbox.pack(pady=10)

# Calculate
tk.Button(window, text="💰 Calculate Total",
          bg="#22c55e",
          command=calculate).pack(pady=10)

# Result
result_label = tk.Label(window, text="",
                        font=("Arial", 14),
                        bg="#e0f2fe")
result_label.pack(pady=10)

# Save
tk.Button(window, text="💾 Save to File",
          bg="#facc15",
          command=save_file).pack(pady=10)

window.mainloop()