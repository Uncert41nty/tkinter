import tkinter as tk
from tkinter import ttk

from Task1 import Task1


class HubLocation(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Хаб Локация")
        self.geometry("400x400")

        self.current_panel = ttk.Frame(self)
        self.current_panel.pack(side="top", fill="both", expand=True)

        button_panel = ttk.Frame(self)
        task1_button = ttk.Button(button_panel, text="Задача 1", command=self.open_task1_window)
        task2_button = ttk.Button(button_panel, text="Задача 2", command=self.open_task2_window)

        task1_button.pack(side="left", padx=10)
        task2_button.pack(side="left", padx=10)

        button_panel.pack(side="top", fill="x")

    def open_task1_window(self):
        task1_window = Task1(self)
        task1_window.title("Задача 1")
        task1_window.geometry("400x400")
        task1_window.pack(side="top", fill="both", expand=True)
        self.current_panel.pack_forget()
        self.current_panel = task1_window

    def open_task2_window(self):
        task2_window = tk.Toplevel(self)  # Use Toplevel for additional windows
        task2_window.title("Задача 2")
        task2_window.geometry("400x400")

        task2_frame = Task2(task2_window)
        task2_frame.pack(side="top", fill="both", expand=True)

        self.current_panel.pack_forget()
        self.current_panel = task2_frame

class Task2(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.init_ui()

    def init_ui(self):
        self.Solution = ttk.Button(self, text="HEATING", command=self.calculate_solution)
        self.V = ttk.Label(self, text="RESULT: ")

        self.Solution.grid(row=0, column=0, columnspan=3, pady=10)
        self.V.grid(row=1, column=0, columnspan=3, pady=10)

        self.Cp = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)
        self.Plot = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)
        self.Q = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)
        self.T1 = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)
        self.T2 = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)

        self.Cp.grid(row=2, column=0, padx=10)
        self.T1.grid(row=2, column=1, padx=10)
        self.Q.grid(row=3, column=0, padx=10)
        self.T2.grid(row=3, column=1, padx=10)
        self.Plot.grid(row=3, column=2, padx=10)

    def calculate_solution(self):
        Q_value = float(self.Q.get())
        Plot_value = float(self.Plot.get())
        Cp_value = float(self.Cp.get())
        T1_value = float(self.T1.get())
        T2_value = float(self.T2.get())

        V_value = Q_value / (Plot_value * Cp_value * (T1_value - T2_value))
        self.V.config(text=f"RESULT: {V_value}")

if __name__ == "__main__":
    app = HubLocation()
    app.mainloop()
