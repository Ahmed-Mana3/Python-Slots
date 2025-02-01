import random
import time


def spin_row():
    symbols = ["🍎", "🍇", "🍋", "🍓", "⭐"]
    return [random.choice(symbols) for _ in range(3)]
    


def get_payout(bet, row):
    dictionary = {"🍎":2, "🍇":3, "🍋":4, "🍓":5, "⭐":10}
    if row[0] == row[1] == row[2]:
        return bet * dictionary.get(row[0])
    else:
        return 0



def main():
    balance = 100
    is_running = True
    while is_running:
        print("*************************")
        print("Welcome To Python Slots")
        print("Symbols: 🍎 🍇 🍋 🍓 ⭐")
        print("*************************")
        while balance > 0:
            print(f"Your Balance is: ${balance}")
            bet = input("Enter Your Bet(q to quit): ").lower()

            if not bet.isdigit():
                print("Invalid input")
                continue
            
            if bet == "q":
                is_running = False
                break


            bet = int(bet)

            if bet > balance:
                print("There is no enough money")
                continue

            if bet <= 0:
                print("Bet must be greater than 0")
                continue

            print("Spinning...")
            time.sleep(1)

            print("*************************")
            row = spin_row()
            print("| ", end="")
            for element in row:
                print(f"{element} | ", end="")
            print()
            print("*************************")

            winnings = get_payout(bet, row)

            if winnings > 0:
                print(f"🎉 You Won ${winnings}!")
                balance += winnings
            else:
                print("😞 Sorry, You Lost This Round!")

            balance -= bet

    print("\n💸 Game Over! You ran out of money.")
    print("Thanks for playing! 🎰")


if __name__ == '__main__':
    main()
