def calculate_tuition(credit_hours, district_code):
    district_code = district_code.upper()
    if district_code == 'I':
        rate = 250
    elif district_code == 'O':
        rate = 550
    else:
        raise ValueError("Invalid district code. Use 'I' for In-district or 'O' for Out-of-district.")
    tuition = credit_hours * rate
    return tuition
def main():
    total_tuition = 0.0
    while True:
        answer = input("Do you want to enter student information? (Yes or No): ").strip().lower()
        if answer != "yes":
            break
        try:
            last_name = input("Enter student's last name: ")
            credit_hours = int(input("Enter number of credit hours: "))
            district_code = input("Enter district code (I for in-district, O for out-of-district): ")
            tuition = calculate_tuition(credit_hours, district_code)
            total_tuition += tuition
            print(f"\nStudent: {last_name}")
            print(f"Tuition Owed: ${tuition:.2f}\n")
        except ValueError as ve:
            print(f"Error: {ve}\n")
    print("========== Tuition Summary ==========")
    print(f"Total Tuition Owed by All Students: ${total_tuition:.2f}")

main()
