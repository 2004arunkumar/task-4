import tkinter as tk
from tkinter import messagebox

def on_button_click(event):
    current_text = entry.get()
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
    elif text == "C":  # Changed `else if` to `elif`
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("mainflow")

entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.SUNKEN)
entry.grid(row=0, column=0, columnspan=4)

button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0
for text in button_texts:
    button = tk.Button(root, text=text, font="Arial 20", width=4, height=2)
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    button.bind("<Button-1>", on_button_click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
