import tkinter as tk

window = tk.Tk()
window.title("CashEarn")
window.geometry("400x640")
window.resizable(False, False)
window.config(bg="#232323")

Soldi = 0

def increment_cash():
    global Soldi
    Soldi += 100
    label.config(text=f"Soldi= {Soldi}")

label = tk.Label(text="Soldi= 0", font=("Microsoft YaHei", 13))
label.pack(pady=20)

button = tk.Button(window, text="+100", font=("Microsoft YaHei", 15), bg="#fc0303", fg="white", bd=10, width=20, command=increment_cash)
button.pack(pady=20)

class Negozio():
    label = tk.Label(text="NEGOZIO", font=("Microsoft YaHei", 13))
    label.pack(pady=20)

def Business():
    global Soldi
    Soldi -= 1000
    Soldi += 500
    label.config(text=f"Soldi= {Soldi}")

button = tk.Button(window, text="Compra un business(-1K, +500)", font=("Microsoft YaHei", 13), bg="#fc0303", fg="white", command=Business)
button.pack(pady=20)

def Casa():
    global Soldi
    Soldi -= 10000
    label.config(text=f"Soldi: {Soldi}")

button = tk.Button(window, text="Compra una casa(-10K)", font=("Microsoft YaHei", 13), bg="#fc0303", fg="white", command=Casa)
button.pack(pady=20)

def MiniMarket():
    global Soldi
    Soldi -= 500
    Soldi += 100
    label.config(text=f"Soldi: {Soldi}")

button = tk.Button(window, text="Compra un MiniMarket(-500, +100)", font=("Microsoft YaHei", 13), bg="#fc0303", fg="white", command=MiniMarket)
button.pack(pady=20)

def AgenziaTaxi():
    global Soldi
    Soldi -= 5000
    Soldi += 10000
    label.config(text=f"Soldi: {Soldi}")

button = tk.Button(window, text="Compra un'Agenzia di Taxi(-5K, +10K)", font=("Microsoft YaHei", 13), bg="#fc0303", fg="white", command=AgenziaTaxi)
button.pack(pady=20)













