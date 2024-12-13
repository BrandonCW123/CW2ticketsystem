# Welcome message
print("Welcome to online ticket shop!")

# Function that creates a receipt 
def create_receipt(user_name, user_destination, tickets, user_total_price):

    receipt_info = (
        f"\n    * Receipt *\n"
        f"Name: {user_name}\n"
        f"Destination: {user_destination}\n"
        f"Tickets: {tickets}\n"
        f"Your total: £{user_total_price:.2f}\n"
    )

# Makes a file name based on the user's name + .txt 
    user_receipt = user_name + ".txt"
    with open(user_receipt, "w") as file:
        file.write(receipt_info)

        print(f"\nYour receipt has been saved on the system as '{user_receipt}'.")

# Main function 
def main():
    
# Identifies the available destinations and prices
    DESTINATIONS = {
        1: ("London", 10.15),
        2: ("Manchester", 22.50), 
        3: ("Birmingham", 21.40)
    }

# Collects the users name
    user_name = input("Please enter you name: ")

# Shows the available destinations and prices
    print("\nList of Destinations:")
    for num, (user_destination, price) in DESTINATIONS.items():
        print(f"{num}. {user_destination}: £{price:.2f}")

# Asks the user to choose their destination    
    choice = int(input("\nPlease select your destination: "))
    user_destination, price = DESTINATIONS[choice] # Takes the selected destination and its prices
    
# Asks the user to put the ticket quantity
    tickets = int(input("How many ticket(s) would you like to purchase?: "))

# Calculates the total price of the ticket
    user_total_price = price * tickets

# Displays the summary
    print("\n      -Summary-")
    print(f"Name: {user_name}")
    print(f"Destination: {user_destination}")
    print(f"Tickets: {tickets}")
    print(f"Your total: £{user_total_price:.2f}")

# Asks the user if they want a receipt
    receipt = input("\nWould you like your receipt? (1-yes/2-no): ")
    if receipt == "1":
       create_receipt(user_name, user_destination, tickets, user_total_price) # Creates a receipt as a txt file
       print("Thank you, Goodbye!") # End of program message

# Programs entry point
if __name__ == "__main__":
    main()