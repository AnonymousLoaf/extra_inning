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
        self.root.geometry("550x400")

        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)

        self.title_label = ttk.Label(
            frame,
            text="Player Nomination Ranking",
            font=("Times New Roman", 18, "bold"),
        )
        self.title_label.pack(pady=5)

        self.file_label = ttk.Label(
            frame, text="Select Raw Excel File:", font=("Times New Roman", 14)
        )
        self.file_label.pack(pady=5)

        self.file_entry = ttk.Entry(frame, width=50)
        self.file_entry.pack(pady=5)

        self.browse_button = ttk.Button(
            frame, text="Browse", command=self.browse_file, bootstyle="info"
        )
        self.browse_button.pack(pady=5)

        # Checkbox Frame
        self.checkbox_frame = ttk.LabelFrame(frame, text="Select Exports", padding=10)
        self.checkbox_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Variables for checkboxes
        self.var_all_positions = tk.IntVar(value=0)
        self.var_pitchers = tk.IntVar(value=0)
        self.var_catchers = tk.IntVar(value=0)
        self.var_infield = tk.IntVar(value=0)
        self.var_outfield = tk.IntVar(value=0)
        self.var_batting = tk.IntVar(value=0)
        self.var_gpa = tk.IntVar(value=0)

        self.check_all_positions = ttk.Checkbutton(self.checkbox_frame, text="All Files", variable=self.var_all_positions, command=self.update_checkboxes)
        self.check_pitchers = ttk.Checkbutton(self.checkbox_frame, text="Pitchers", variable=self.var_pitchers)
        self.check_catchers = ttk.Checkbutton(self.checkbox_frame, text="Catchers", variable=self.var_catchers)
        self.check_infield = ttk.Checkbutton(self.checkbox_frame, text="Infield", variable=self.var_infield)
        self.check_outfield = ttk.Checkbutton(self.checkbox_frame, text="Outfield", variable=self.var_outfield)
        self.check_batting = ttk.Checkbutton(self.checkbox_frame, text="Batting", variable=self.var_batting)
        self.check_gpa = ttk.Checkbutton(self.checkbox_frame, text="GPA", variable=self.var_gpa)

        # Packing checkboxes horizontally
        self.check_all_positions.pack(side=tk.LEFT, padx=5)
        self.check_pitchers.pack(side=tk.LEFT, padx=5)
        self.check_catchers.pack(side=tk.LEFT, padx=5)
        self.check_infield.pack(side=tk.LEFT, padx=5)
        self.check_outfield.pack(side=tk.LEFT, padx=5)
        self.check_batting.pack(side=tk.LEFT, padx=5)
        self.check_gpa.pack(side=tk.LEFT, padx=5)

        self.run_button = ttk.Button(
            frame,
            text="Run",
            command=lambda: self.run_callback(self),
            bootstyle="success",
        )
        self.run_button.pack(pady=5)

    def update_checkboxes(self):
        if self.var_all_positions.get() == 1:
            # Check all other checkboxes
            self.var_pitchers.set(1)
            self.var_catchers.set(1)
            self.var_infield.set(1)
            self.var_outfield.set(1)
            self.var_batting.set(1)
            self.var_gpa.set(1)
        else:
            # Uncheck all other checkboxes
            self.var_pitchers.set(0)
            self.var_catchers.set(0)
            self.var_infield.set(0)
            self.var_outfield.set(0)
            self.var_batting.set(0)
            self.var_gpa.set(0)

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
        elif type == "empty":
            message = "Please select a file."
        messagebox.showerror("Error: ", message)

    def finish_message(self):
        messagebox.showinfo(
            "Success", "Player nominations have been successfully ranked."
        )

    def get_file(self):
        if not os.path.isfile(self.file_entry.get()):
            self.error_message("file")
            return None
        elif not self.file_entry.get().endswith(".xlsx"):
            self.error_message("wrongFile")
            return None
        elif self.file_entry.get() == "":
            self.error_error("empty")
            return None
        return self.file_entry.get()

    def get_selected_options(self):
        return {
            "all_positions": self.var_all_positions.get(),
            "pitchers": self.var_pitchers.get(),
            "catchers": self.var_catchers.get(),
            "infield": self.var_infield.get(),
            "outfield": self.var_outfield.get(),
            "batting": self.var_batting.get(),
            "gpa": self.var_gpa.get(),
    }
