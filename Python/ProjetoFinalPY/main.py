# main.py
import tkinter as tk
from gui import GerenciadorTarefasApp

def main():
    root = tk.Tk()
    app = GerenciadorTarefasApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
