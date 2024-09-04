import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import csv
import random

def generate_data(num_rows, num_cols):
    return [[random.randint(0, 10) for _ in range(num_cols)] for _ in range(num_rows)]

def check_inputs(input1, input2):
    try:
        # Get the input values from the entries
        value1 = int(input1.get())
        value2 = int(input2.get())
        
        return True
        
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter valid numbers in both fields.")
        # If a ValueError occurs, show a warning message
        return False

def generate_csv(data):
    file_path = filedialog.asksaveasfilename(
        title="Save CSV file",
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    
    if file_path:
        # Write the data to the specified CSV file
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"File saved as {file_path}")

def on_button_click(num_rows, num_cols):
    if check_inputs(num_rows, num_cols):
        data = generate_data(int(num_rows.get()), int(num_cols.get()))
        generate_csv(data)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('200x300')
    root.title("CSV generator")

    tk.Label(root, text="Enter Number of Rows", font=('Calibri 10')).pack()
    row_str = tk.Entry(root, width=35)
    row_str.pack(padx=20, pady=20)

    tk.Label(root, text="Enter Number of Columns", font=('Calibri 10')).pack()
    col_str = tk.Entry(root, width=35)
    col_str.pack(padx=20, pady=20)

    generate_button = tk.Button(root, text = "Generate CSV", command=lambda: on_button_click(row_str, col_str))
    generate_button.pack(padx=20, pady=20)

    root.mainloop()