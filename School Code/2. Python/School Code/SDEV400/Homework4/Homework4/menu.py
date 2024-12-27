import user
import leaderboard
import game
import user_guide

def main_menu():
    """
    Main menu function that displays options for the user and handles their selection.
    """
    while True:
        print("\nMain Menu")
        print("1. Register User")
        print("2. Sign In")
        print("3. Play Game as Guest")
        print("4. View Leaderboard")
        print("5. View User Guide")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user.register_user()
        elif choice == '2':
            player_id = user.sign_in()
            if player_id:
                game.start_game(player_id)
        elif choice == '3':
            game.start_game()
        elif choice == '4':
            leaderboard.view_leaderboard()
        elif choice == '5':
            user_guide.print_user_guide()
        elif choice == '6':
            print("Thank you for playing! See you next time.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()