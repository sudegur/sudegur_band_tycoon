import random
import os

game_state = {
    "band_name": "",
    "money": 1000,
    "popularity": 10,
    "fans": 50,
    "albums_released": 0,
    "day": 1
}
def display_welcome_menu():
    print("===================================")
    print("  Welcome to BAND TYCOON MANAGER ")
    print("===================================")
    print("1. Start a New Journey (New game)")
    print("2. Continue from Last Save (Load Game)")
    print("3. Exit Game")
    print("===================================")

def initialize_new_game():
    print("\n---Starting a New Game ---")
    name = input("Enter your legendary Band Name: ").strip()

    while not name:
        name = input("Band name cannot be empty! Please enter a name: ").strip()
    
    game_state["band_name"] = name
    game_state["money"] = 1000
    game_state["popularity"] = 10
    game_state["fans"] = 50
    game_state["albums_released"] = 0
    game_state["day"] = 1
    print(f"\nRock on! Your band '{name}' has been successfully created.")

def display_status():
    print("\n=========================================")
    print(f" BAND: {game_state['band_name']} | Day: {game_state['day']}")
    print("=========================================")
    print(f" -> Budget: ${game_state['money']}")
    print(f" -> Popularity: {game_state['popularity']}/100")
    print(f" -> Fan Base: {game_state['fans']} fans")
    print(f" -> Albums Released: {game_state['albums_released']}")
    print("=========================================")

def handle_studio():
    cost = 200
    if game_state["money"] < cost:
        print(f"\n[!] Not enough money! You need ${cost} to rent a studio.")
        return False
    game_state["money"] -= cost

    pop_gain = random.randint(5, 12)
    game_state["popularity"] += pop_gain

    if game_state["popularity"] > 100:
        game_state["popularity"] = 100
    game_state["albums_released"] += 1

    print("\n=========================================")
    print(f" STUDIO SESSION SUCCESSFUL!")
    print(f"-> You spent ${cost} on studio rent.")
    print(f"-> Your new single gained popularity: +{pop_gain}")
    print(f"-> Total albums/singles released: {game_state['albums_released']}")
    print("=========================================")
    return True

def handle_concert():
    print("\n--- Organizing a Concert ---")
    print("1. Local Pub Gig (Low risk, low reward)")
    print("2. City Arena (Requires at least 40 Popularity)")

    concert_choice = input("Choose venue size (1-2): ").strip()

    if concert_choice == "1":
        base_income = game_state["popularity"] * random.randint(5, 10)
        new_fans = random.randint(10, 30)

        game_state["money"] += base_income
        game_state["fans"] += new_fans
        game_state["popularity"] += random.randint(1, 3)

        print("=========================================")
        print(f" PUB GIG COMPLETED!")
        print(f"-> Ticket Sales Income: +${base_income}")
        print(f"-> New Fans gained: +{new_fans}")
        print("=========================================")
        return True
    elif concert_choice == "2":
        if game_state["popularity"] < 40:
            print(" You are not famous enough for the Arena yet! (Need 40+ popularity.)")
            return False
        
        base_income = game_state["popularity"] * random.randint(15, 30)
        new_fans = random.randint(100, 300)

        game_state["money"] += base_income
        game_state["fans"] += new_fans
        game_state["popularity"] += random.randint(3, 7)

        print("\n=========================================")
        print(f" ARENA CONCERT WAS A HUGE HIT!")
        print(f"-> Huge Ticket Sales Income: +${base_income}")
        print(f"-> Massive Fan growth: +{new_fans}")
        print("=========================================")
        return True
    else:
        print("[Error] Invalid venue choice.")
        return False

def handle_marketing():
    cost = 100
    if game_state["money"] < cost:
        print(f" [!] Not enough money! Marketing campaigns cost ${cost}.")
        return False
    game_state["money"] -= cost
    pop_gain = random.randint(3, 8)
    fan_gain = random.randint(15, 50)

    game_state["popularity"] += pop_gain
    if game_state["popularity"] > 100:
        game_state["popularity"] = 100
    game_state["fans"] += fan_gain

    print("\n=========================================")
    print(f" SOCIAL MEDIA CAMPAIGN LAUNCHED!")
    print(f"-> Spent ${cost} on Instagram and TikTok ads.")
    print(f"-> Popularity: +{pop_gain} | New Fans: +{fan_gain}")
    print("=========================================")
    return True

def trigger_random_event():
    if random.random() > 0.25:
        return
    
    events = [
        {"text": "Your lead singer caught a cold! Voice medicine cost you $50.", "money": -50, "popularity": 0},
        {"text": "A famous influencer used your track in a TikTok video! Fans +150, Popularity +5.", "money":0, "popularity": 5, "fans": 150},
        {"text": "Your guitarist had a minor fight with a fan. Popularity -4.", "money": 0, "popularity": -4},
        {"text": "You found a forgotten $100 bill in an old guitar case!", "money": 100, "popularity": 0}
    ]
    event = random.choice(events)
    print(" [RANDOM EVENT] " + event["text"])

    if "money" in event: game_state["money"] += event["money"]
    if "popularity" in event: game_state["popularity"] += event["popularity"]
    if "fans" in event: game_state["fans"] += event["fans"]

    if game_state["money"] < 0: game_state["money"] = 0
    if game_state["popularity"] < 0: game_state["popularity"] = 0
    if game_state["popularity"] > 100: game_state["popularity"] = 100

def save_game():
    try:
        with open("save_game.txt", "w", encoding="utf-8") as file:
            for key, value in game_state.items():
                file.write(f"{key}:{value}\n")
        print("\n=========================================")
        print(" GAME SAVED SUCCESSFULLY!")
        print("-> Your progress has been written to 'save_game.txt'.")
        print("=========================================")
    except Exception as e:
        print(f"[Error] Could not save the game: {e}")

def load_game():
    if not os.path.exists("save_game.txt"):
        print(" [!] No saved game found! Please start a New Game first.")
        return False
    
    try:
        with open("save_game.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if ":" in line:
                    key, value = line.split(":", 1)

                    if key in ["money", "popularity", "fans", "albums_released", "day"]:
                        game_state[key] = int(value)
                    else:
                        game_state[key] = value

        print("\n=========================================")
        print(" GAME LOADED SUCCESSFULLY!")
        print(f"-> Welcome back, manager of '{game_state['band_name']}'!")
        print("=========================================")
        return True
    except Exception as e:
        print(f" [ERROR] Could not load the save file: {e}")
        return False


def play_game():

    while True:
        display_status()
        print("What is your next move, manager?")
        print("1. Enter the Studio (Record a single) [- $200]")
        print("2. Organize a Local Concert (Earn Money & Fans)")
        print("3. Run a Social Media Campaign [- $100]")
        print("4. Save Current Progress")
        print("5. Quit to Main Menu")

        choice = input("Select an option (1-5): ").strip()
        action_successful = False

        if choice == "1":
            action_successful = handle_studio()
        elif choice == "2":
            action_successful = handle_concert()
        elif choice == "3":
            action_successful = handle_marketing()
        elif choice == "4":
            save_game()
            action_successful = False
        elif choice == "5":
            confirm = input("Are you sure you want to quit? Unsaved progress will be lost (y/n): ").lower()
            if confirm == "y":
                print("Returning to Main Menu...")
                break
        else:
            print(" [ERROR] Invalid choice! Please enter a number between 1 and 5.")
        
        if action_successful:
            trigger_random_event()
            game_state["day"] += 1

def main():
    while True:
        display_welcome_menu()
        main_choice = input("Enter your choice: ").strip()
        if main_choice == "1":
            initialize_new_game()
            play_game()
        elif main_choice == "2":
            if load_game():
                play_game()
        elif main_choice == "3":
            print(" Thank you for playing Band Tycoon! Goodbye.")
            break
        else:
            print("[ERROR] Invalid input. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()