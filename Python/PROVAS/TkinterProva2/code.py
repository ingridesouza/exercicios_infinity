import tkinter as tk
from tkinter import messagebox

def login():
    email = entry_email.get()
    password = entry_password.get()

    match password:
        case p if len(p) < 6:
            messagebox.showerror("Erro", "A senha deve ter pelo menos 6 caracteres.")
        case _:
            match email:
                case e if "@" not in e:
                    messagebox.showerror("Erro", "O e-mail deve conter o caractere '@'.")
                case _:
                    messagebox.showinfo("Sucesso", "Login realizado com sucesso!")

root = tk.Tk()
root.title("Login")


bg_color = "#f0f0f0"
font_style = ("Helvetica", 12)

root.configure(bg=bg_color)

label_email = tk.Label(root, text="E-mail:", bg=bg_color, font=font_style)
label_email.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_email = tk.Entry(root)
entry_email.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Senha:", bg=bg_color, font=font_style)
label_password.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

button_login = tk.Button(root, text="Login", command=login, bg="#007bff", fg="white", font=font_style)
button_login.grid(row=2, columnspan=2, padx=10, pady=5)

root.mainloop()
