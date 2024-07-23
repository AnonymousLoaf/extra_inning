import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk
import os
import pandas as pd

class PlayerNominationApp:
    def __init__(self, root, run_callback):
        self.root = root
        self.root.title("Player Nomination Application")
        self.run_callback = run_callback
        self.setup_ui()

    def setup_ui(self):
        self.root.geometry("500x400")
        self.root.style = ttk.Style("darkly")

        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        self.title_label = ttk.Label(frame, text="Player Nomination Ranking", font=("", 18))
        self.title_label.pack(pady=5)

        self.file_label = ttk.Label(frame, text="Select XLSX File:")
        self.file_label.pack(pady=5)

        self.file_entry = ttk.Entry(frame, width=50)
        self.file_entry.pack(pady=5)

        self.browse_button = ttk.Button(frame, text="Browse", command=self.browse_file, bootstyle="info")
        self.browse_button.pack(pady=5)

        self.run_button = ttk.Button(frame, text="Run", command=self.run_callback, bootstyle="success")
        self.run_button.pack(pady=5)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_path)

    def get_file_path(self):
        return self.file_entry.get()
    
    def error_message(self, type):
        if type == "file":
            message = "File does not exist."
        elif type == "wrongFile":
            message = "Please select an Excel file."
        messagebox.showerror("Error: ", message)

    def finish_message(self):
        messagebox.showinfo("Success", "Player nominations have been successfully ranked.")
