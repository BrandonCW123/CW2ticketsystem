print("Welcome to online ticket shop!")

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