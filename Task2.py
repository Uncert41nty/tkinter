import tkinter as tk
from tkinter import ttk

class Task2(tk.Tk):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.title("Task2")

        self.Cp = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)
        self.Plot = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)
        self.Q = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)
        self.T1 = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)
        self.T2 = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)

        self.btn_solution = ttk.Button(self, text="HEATING", command=self.calculate_solution)

        self.label_result = ttk.Label(self, text="RESULT: ")

        self.setup_layout()

    def setup_layout(self):
        self.label_result.grid(row=0, column=0, columnspan=4, pady=10)

        self.Cp.grid(row=1, column=0, padx=10)
        self.T1.grid(row=1, column=1, padx=10)
        self.Q.grid(row=2, column=0, padx=10)
        self.T2.grid(row=2, column=1, padx=10)
        self.Plot.grid(row=2, column=2, padx=10)

        self.btn_solution.grid(row=3, column=0, columnspan=3, pady=10)

    def calculate_solution(self):
        Q_value = float(self.Q.get())
        Plot_value = float(self.Plot.get())
        Cp_value = float(self.Cp.get())
        T1_value = float(self.T1.get())
        T2_value = float(self.T2.get())

        # Вычислите значение V по формуле
        V_value = Q_value / (Plot_value * Cp_value * (T1_value - T2_value))

        # Отобразите значение V в label_result
        self.label_result.config(text=f"RESULT: {V_value}")

if __name__ == "__main__":
    app = Task2()
    app.mainloop()
