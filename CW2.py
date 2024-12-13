print("Welcome to online ticket shop!")

def create_receipt(user_name, user_destination, tickets, user_total_price):

    receipt_info = (
        f"\n    * Receipt *\n"
        f"Name: {user_name}\n"
        f"Destination: {user_destination}\n"
        f"Tickets: {tickets}\n"
        f"Your total: £{user_total_price:.2f}\n"
    )

    user_receipt = user_name + ".txt"
    with open(user_receipt, "w") as file:
        file.write(receipt_info)

        print(f"\nYour receipt has been saved on the system as '{user_receipt}'.")

def main():
    
    DESTINATIONS = {
        1: ("London", 10.15),
        2: ("Manchester", 22.50), 
        3: ("Birmingham", 21.40)
    }

    user_name = input("Please enter you name: ")

    print("\nList of Destinations:")
    for num, (user_destination, price) in DESTINATIONS.items():
        print(f"{num}. {user_destination}: £{price:.2f}")
    
    choice = int(input("\nPlease select your destination: "))
    user_destination, price = DESTINATIONS[choice]
    
    tickets = int(input("How many ticket(s) would you like to purchase?: "))

    user_total_price = price * tickets

    print("\n      -Summary-")
    print(f"Name: {user_name}")
    print(f"Destination: {user_destination}")
    print(f"Tickets: {tickets}")
    print(f"Your total: £{user_total_price:.2f}")

    receipt = input("\nWould you like your receipt? (1-yes/2-no): ")
    if receipt == "1":
       create_receipt(user_name, user_destination, tickets, user_total_price)
       print("Thank you, Goodbye!")

if __name__ == "__main__":
    main()