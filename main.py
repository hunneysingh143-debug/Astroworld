import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def on_click():
    messagebox.showinfo("Astroworld", "Welcome to Astroworld!")

def main():
    root = tk.Tk()
    root.title("Astroworld")
    root.geometry("400x300")
    root.iconbitmap("assets/app.ico")  # Use your app icon

    label = tk.Label(root, text="Welcome to Astroworld!", font=("Arial", 16))
    label.pack(pady=20)

    btn = tk.Button(root, text="Click Me", command=on_click)
    btn.pack(pady=10)

    try:
        logo = Image.open("assets/app.png")
        logo = logo.resize((100, 100), Image.LANCZOS)
        logo_tk = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(root, image=logo_tk)
        logo_label.image = logo_tk
        logo_label.pack(pady=10)
    except Exception:
        pass

    root.mainloop()

if __name__ == "__main__":
    main()
