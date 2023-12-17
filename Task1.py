import tkinter as tk
from tkinter import ttk

class Task1(tk.Tk):
    def __init__(self, hub_location=None):
        super().__init__()

        self.hub_location = hub_location

        self.init_ui()

    def init_ui(self):
        self.title("Task1")

        self.jSpinner1 = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)
        self.jSpinner2 = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)
        self.jSpinner3 = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)
        self.jSpinner4 = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)
        self.jSpinner5 = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)
        self.jSpinner6 = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)
        self.jSpinner7 = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)
        self.jSpinner8 = ttk.Spinbox(self, from_=0.0, to=float('inf'), increment=1.0)

        self.btn_solution = ttk.Button(self, text="Solution", command=self.calculate_solution)

        self.label_answer = ttk.Label(self, text="ANSWER IS =")

        self.setup_layout()

    def setup_layout(self):
        self.jSpinner1.grid(row=0, column=1)
        self.jSpinner2.grid(row=1, column=1)
        self.jSpinner3.grid(row=2, column=1)
        self.jSpinner4.grid(row=3, column=1)
        self.jSpinner5.grid(row=4, column=1)
        self.jSpinner6.grid(row=5, column=1)
        self.jSpinner7.grid(row=6, column=1)
        self.jSpinner8.grid(row=7, column=1)

        ttk.Label(self, text="гелиостаты").grid(row=0, column=2)
        ttk.Label(self, text="гелиостатов").grid(row=1, column=2)
        ttk.Label(self, text="макс энерг осв").grid(row=2, column=2)
        ttk.Label(self, text="Коэффициент отражения").grid(row=3, column=2)
        ttk.Label(self, text="Kоэфф поглощения приемника").grid(row=4, column=2)
        ttk.Label(self, text="Макс облуч зеркала").grid(row=5, column=2)
        ttk.Label(self, text="рабочая температура").grid(row=6, column=2)
        ttk.Label(self, text="Степень черноты").grid(row=7, column=2)

        self.btn_solution.grid(row=8, column=0, columnspan=2, pady=10)

        self.label_answer.grid(row=0, column=3, rowspan=9, padx=10)

    def calculate_solution(self):
        value1 = float(self.jSpinner1.get())
        value2 = float(self.jSpinner2.get())
        value3 = float(self.jSpinner3.get())
        value4 = float(self.jSpinner4.get())
        value5 = float(self.jSpinner5.get())
        value6 = float(self.jSpinner6.get())
        value7 = float(self.jSpinner7.get())
        value8 = float(self.jSpinner8.get())

        result = value1 * value2 * value3 * value4 * value5 * value6 * value7 * value8

        self.label_answer.config(text=f"ANSWER IS = {result}")

if __name__ == "__main__":
    app = Task1()
    app.mainloop()
