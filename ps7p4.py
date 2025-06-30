def calculate_pay(job_code, hours_worked):
    job_code = job_code.upper()
    if job_code == 'L':
        rate = 25
    elif job_code == 'A':
        rate = 30
    elif job_code == 'J':
        rate = 50
    else:
        raise ValueError("Invalid job code.")
    if hours_worked > 40:
        regular_hours = 40
        overtime_hours = hours_worked - 40
        gross_pay = (regular_hours * rate) + (overtime_hours * rate * 1.5)
    else:
        gross_pay = hours_worked * rate
    return rate, gross_pay
def main():
    total_gross_pay = 0.0
    while True:
        answer = input("Do you want to enter employee data? (Yes or No): ").strip().lower()
        if answer != "yes":
            break
        try:
            last_name = input("Enter employee's last name: ")
            job_code = input("Enter job code (L, A, J): ").strip()
            hours_worked = float(input("Enter hours worked: "))
            rate, gross_pay = calculate_pay(job_code, hours_worked)
            total_gross_pay += gross_pay
            print(f"\nEmployee: {last_name}")
            print(f"Hours Worked: {hours_worked:.2f}")
            print(f"Pay Rate: ${rate:.2f}/hr")
            print(f"Gross Pay: ${gross_pay:.2f}\n")
        except ValueError as ve:
            print(f"Error: {ve}\n")
    print("========== Payroll Summary ==========")
    print(f"Total Gross Pay for All Employees: ${total_gross_pay:.2f}")

main()