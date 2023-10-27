import tkinter as tk
from tkinter import filedialog


def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        print("Selected folder:", folder_path)
    else:
        print("No folder selected.")


root = tk.Tk()
root.title("File Selection Example")

select_button = tk.Button(root, text="Select File", command=select_folder)
select_button.pack(pady=20)

root.mainloop()
