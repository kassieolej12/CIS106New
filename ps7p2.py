def compute_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0.0
    return hits / at_bats
def main():
    player_count = 0
    while True:
        answer = input("Do you want to enter player stats? (Yes or No): ").strip().lower()
        if answer != "yes":
            break
        try:
            last_name = input("Enter player's last name: ")
            hits = int(input("Enter number of hits: "))
            at_bats = int(input("Enter number of at bats: "))
            average = compute_batting_average(hits, at_bats)
            player_count += 1
            print(f"\nPlayer: {last_name}")
            print(f"Batting Average: {average:.3f}\n")
        except ValueError:
            print("Invalid input. Please enter integers for hits and at bats.\n")
    print(f"Total number of players entered: {player_count}")
main()