def compute_trip_data(miles, gallons):
    if gallons == 0:
        mpg = 0.0
    else:
        mpg = miles / gallons
    gas_cost = gallons * 3.00
    return mpg, gas_cost
def main():
    trip_count = 0
    total_miles = 0.0
    total_gas_cost = 0.0
    while True:
        answer = input("Do you want to enter a trip? (Yes or No): ").strip().lower()
        if answer != "yes":
            break
        try:
            destination = input("Enter destination city: ")
            miles = float(input("Enter miles traveled: "))
            gallons = float(input("Enter gallons used: "))
            mpg, cost = compute_trip_data(miles, gallons)
            trip_count += 1
            total_miles += miles
            total_gas_cost += cost
            print(f"\nDestination: {destination}")
            print(f"Miles Traveled: {miles:.1f}")
            print(f"Miles Per Gallon: {mpg:.2f}")
            print(f"Gas Cost: ${cost:.2f}\n")
        except ValueError:
            print("Invalid input. Please enter numeric values for miles and gallons.\n")
    print("========== Summary ==========")
    print(f"Total Trips Entered: {trip_count}")
    print(f"Total Miles Traveled: {total_miles:.1f}")
    print(f"Total Gas Cost: ${total_gas_cost:.2f}")
main()