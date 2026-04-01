💼 Advanced Employee Payroll & Tax Management System
📌 Overview

This project is a Python-based Object-Oriented Payroll Management System designed for a mid-sized organization. It efficiently manages employee salary calculations, supports multiple employee types, and generates automated salary slips.

The system demonstrates key OOP concepts such as Inheritance, Encapsulation, and Exception Handling.

✨ Features

➤ 👨‍💼 Multiple Employee Types Supported
    ▸ Permanent Employee
    ▸ Contract Employee
    ▸ Intern

➤ 🧮 Automated Salary Calculation
    ▸ Based on Basic Salary
    ▸ DA (92%)
    ▸ HRA (58%)
    ▸ TA (30%)

➤ 📄 Salary Slip Generation
    ▸ Monthly .txt file for each employee

➤ ⚠️ Robust Error Handling
    ▸ Prevents negative salary input
    ▸ Handles file permission issues

🧠 OOP Concepts Used

✦ Classes & Objects
✦ Inheritance
✦ Method Reusability
✦ Exception Handling

⚙️ Salary Calculation Formula

➤ DA = 0.92 × Basic
➤ HRA = 0.58 × Basic
➤ TA = 0.30 × Basic

➤ Gross Salary = Basic + DA + HRA + TA

🏗️ Project Structure
Payroll-System/
│── main.py
│── README.md
│── Yukti_salary.txt
│── Suhani_salary.txt
│── Niharika_salary.txt
🚀 How to Run the Project

➤ Step 1: Install Python (if not installed)

➤ Step 2: Clone the repository
git clone [https://github.com/your-username/payroll-system.git](https://github.com/niharika7206/Python-Project.git)

➤ Step 3: Navigate to the folder
cd payroll-system

➤ Step 4: Run the program
python main.py

🧪 Sample Output
Employee Salary Slip

ID: 101
Name: Yukti
Basic Salary: 30000
DA: 27600.0
HRA: 17400.0
TA: 9000.0
Gross Salary: 84000.0

⚠️ Error Handling

➤ Prevents invalid (negative) salary input
➤ Handles file writing errors (file open / permission issues)

🚀 Future Enhancements

✧ Add Tax Deduction System
✧ GUI using Tkinter or Web Interface
✧ Database integration (MySQL / SQLite)
✧ Full Employee Management Dashboard

👩‍💻 Author

Niharika Sharma

📜 License

This project is for educational purposes.
