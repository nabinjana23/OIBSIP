import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)

        bmi_label.config(text=f"BMI: {bmi:.2f}")

        # Classify into categories
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        category_label.config(text=f"Category: {category}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")

# Create main window
window = tk.Tk()
window.title("BMI Calculator")

# Weight input
label_weight = tk.Label(window, text="Enter Weight (kg):")
label_weight.grid(row=0, column=0, padx=10, pady=10)
entry_weight = tk.Entry(window)
entry_weight.grid(row=0, column=1, padx=10, pady=10)

# Height input
label_height = tk.Label(window, text="Enter Height (m):")
label_height.grid(row=1, column=0, padx=10, pady=10)
entry_height = tk.Entry(window)
entry_height.grid(row=1, column=1, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Display BMI and category
bmi_label = tk.Label(window, text="BMI: ")
bmi_label.grid(row=3, column=0, columnspan=2)

category_label = tk.Label(window, text="Category: ")
category_label.grid(row=4, column=0, columnspan=2)

# Run the Tkinter event loop
window.mainloop()
