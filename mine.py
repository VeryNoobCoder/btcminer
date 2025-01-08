import random
import time

def generate_random_line(length=60):
    """Generate a random string of uppercase, lowercase, and numbers."""
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(chars) for _ in range(length))

def simulate_bitcoin_miner():
    wallet = input("Enter your Bitcoin Wallet: ")
    print("Starting Bitcoin miner...\n")
    time.sleep(2)  # Simulate a brief pause

    while True:
        # Determine random stopping point between 2000 and 4000 lines
        max_lines = random.randint(2000, 4000)
        print(f"Mining in progress... (Will stop after {max_lines} lines)\n")

        # Generate and display random lines of "code"
        for i in range(max_lines):
            print(f"{i + 1}: {generate_random_line()}")
            time.sleep(0.01)  # Slight delay for realism

        # Display success message
        print("\nSuccessfully mined 1 BTC. Bitcoin deposited to your wallet address.")
        print(f"Wallet: {wallet}\n")

        # Ask the user if they want to continue
        choice = input("Do you want to continue mining? (Y/N): ").strip().upper()
        if choice == 'N':
            print("Mining session ended. Goodbye!")
            break
        elif choice != 'Y':
            print("Invalid input. Please enter 'Y' to continue or 'N' to stop.")

if __name__ == "__main__":
    simulate_bitcoin_miner()
