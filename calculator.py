import tkinter as tk
from tkinter import messagebox

# ===== Function to calculate loan =====
def calculate_loan():
    try:
        principal = float(entry_amount.get())
        rate = float(entry_rate.get()) / 100 / 12
        term_months = int(entry_term.get()) * 12

        if rate == 0:
            monthly_payment = principal / term_months
        else:
            monthly_payment = principal * rate * (1 + rate) ** term_months / ((1 + rate) ** term_months - 1)

        total_payment = monthly_payment * term_months
        total_interest = total_payment - principal

        result_label.config(text=f"Monthly Payment: ₹{monthly_payment:.2f}\n"
                                 f"Total Payment: ₹{total_payment:.2f}\n"
                                 f"Total Interest: ₹{total_interest:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# ===== GUI Setup =====
loan_app = tk.Tk()
loan_app.title("Loan Calculator")
loan_app.geometry("500x500")
loan_app.configure(bg="#0d1117")

# ===== Header =====
tk.Label(loan_app, text="🏦 Loan Calculator", fg="white", bg="#0d1117",
         font=("Arial", 24, "bold")).pack(pady=20)

# ===== Input Fields =====
input_frame = tk.Frame(loan_app, bg="#0d1117")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Loan Amount (₹)", font=("Arial", 14), fg="white", bg="#0d1117").grid(row=0, column=0, sticky="w", pady=10)
entry_amount = tk.Entry(input_frame, font=("Arial", 14), width=20)
entry_amount.grid(row=0, column=1, pady=10)

tk.Label(input_frame, text="Interest Rate (% annual)", font=("Arial", 14), fg="white", bg="#0d1117").grid(row=1, column=0, sticky="w", pady=10)
entry_rate = tk.Entry(input_frame, font=("Arial", 14), width=20)
entry_rate.grid(row=1, column=1, pady=10)

tk.Label(input_frame, text="Loan Term (years)", font=("Arial", 14), fg="white", bg="#0d1117").grid(row=2, column=0, sticky="w", pady=10)
entry_term = tk.Entry(input_frame, font=("Arial", 14), width=20)
entry_term.grid(row=2, column=1, pady=10)

# ===== Calculate Button =====
tk.Button(loan_app, text="Calculate", font=("Arial", 14), bg="#5c6ac4", fg="white",
          padx=10, pady=5, command=calculate_loan).pack(pady=20)

# ===== Result Display =====
result_label = tk.Label(loan_app, text="", fg="lightgreen", bg="#0d1117", font=("Arial", 14), justify="left")
result_label.pack(pady=10)

# ===== Footer =====
tk.Label(loan_app, text="© 2025 Loan Calculator Project", fg="gray", bg="#0d1117", font=("Arial", 10)).pack(side="bottom", pady=20)

loan_app.mainloop()
