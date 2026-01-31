leaderboard = []

while True:
    print("\nLeaderboard Menu")
    print("1. Add player score")
    print("2. View leaderboard")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        name = input("Enter player name: ")
        score = int(input("Enter player score: "))
        leaderboard.append((name, score))

    elif choice == "2":
        if not leaderboard:
            print("No scores yet.")
        else:
            print("\nLeaderboard:")
            # Sort by score (highest first)
            sorted_board = sorted(leaderboard, key=lambda x: x[1], reverse=True)
            for i, player in enumerate(sorted_board, start=1):
                print(f"{i}. {player[0]} - {player[1]}")

    elif choice == "3":
        print("Exiting leaderboard. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
