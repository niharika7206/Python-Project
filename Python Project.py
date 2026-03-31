class Employee:
    def __init__(self, emp_id, name, basic):
        self.emp_id = emp_id
        self.name = name
        self.basic = basic

    def calculate_salary(self):
        try:
            if self.basic < 0:
                raise ValueError("Basic salary cannot be negative")

            da = 0.92 * self.basic
            hra = 0.58 * self.basic
            ta = 0.30 * self.basic

            gross = self.basic + da + hra + ta
            return da, hra, ta, gross

        except Exception as e:
            print("Salary Calculation Error:", e)
            return None   # ✅ important fix


    def generate_slip(self):
        result = self.calculate_salary()

        # ✅ handle error properly
        if result is None:
            print(f"Slip not generated for {self.name}")
            return

        da, hra, ta, gross = result

        filename = f"{self.name}_salary.txt"

        try:
            with open(filename, "w") as file:
                file.write("Employee Salary Slip\n")
                file.write("----------------------\n")
                file.write(f"ID: {self.emp_id}\n")
                file.write(f"Name: {self.name}\n")
                file.write(f"Basic Salary: {self.basic}\n")
                file.write(f"DA: {da}\n")
                file.write(f"HRA: {hra}\n")
                file.write(f"TA: {ta}\n")
                file.write(f"Gross Salary: {gross}\n")

            print("Salary slip generated:", filename)

        except PermissionError:
            print(f"Cannot write file '{filename}'. Close it if open or check permissions.")


class PermanentEmployee(Employee):
    pass


class ContractEmployee(Employee):
    pass


class Intern(Employee):
    pass


# Example usage
emp1 = PermanentEmployee(101, "Yukti", 30000)
emp1.generate_slip()

emp2 = ContractEmployee(102, "Suhani", 20000)
emp2.generate_slip()

emp3 = Intern(103, "Niharika", 10000)
emp3.generate_slip()