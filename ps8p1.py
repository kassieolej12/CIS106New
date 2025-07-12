class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def bonus(self):
        return self.annual_salary * 0.10
    def __str__(self):
        return (f"Employee: {self.full_name()}\n"
                f"Annual Salary: ${self.annual_salary:,.2f}\n"
                f"Bonus (10%): ${self.bonus():,.2f}")
class Manager(Employee):
    def bonus(self):
        return self.annual_salary * 0.20
    def long_term_bonus(self):
        return self.annual_salary * 0.50
    def __str__(self):
        return (f"Manager: {self.full_name()}\n"
                f"Annual Salary: ${self.annual_salary:,.2f}\n"
                f"Bonus (20%): ${self.bonus():,.2f}\n"
                f"Long-term Bonus (50%): ${self.long_term_bonus():,.2f}")
def main():
    emp = Employee("Alice", "Johnson", 60000)
    print(emp)
    print("\n" + "-" * 40 + "\n")
    mgr = Manager("Bob", "Smith", 100000)
    print(mgr)
if __name__ == "__main__":
    main()