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


    def generate_slip(self):
        da, hra, ta, gross = self.calculate_salary()

        filename = f"{self.name}_salary.txt"

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


class PermanentEmployee(Employee):
    pass


class ContractEmployee(Employee):
    pass


class Intern(Employee):
    pass


# Example usage
emp1 = PermanentEmployee(101, "Rahul", 30000)
emp1.generate_slip()

emp2 = ContractEmployee(102, "Priya", 20000)
emp2.generate_slip()

emp3 = Intern(103, "Aman", 10000)
emp3.generate_slip()
