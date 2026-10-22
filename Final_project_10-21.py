print ("welcome to The Lost Kingdom!")
print("Enter your name:")
player1_name = input()
print("Welcome", player1_name)

player1_health = 100
player1_attack_damage = 15
player1_gold = 20
player1_armour = 0
player1_potions = 0

class Functions:
    def show_stats ():
        print("--Starting Stats--")
        print("Health =",player1_health, "\n" "Gold =",player1_gold, "\n" "Armour =", player1_armour, "\n" "Potions =",player1_potions )


#Main code

print ("Click any button to start")

input()

Functions.show_stats ()




#mylocations = []



#-----------------------------------------------



locations = {
    "village": {
        "name": "The Village",
        "description": "A quiet village on the edge of a dark forest.",
        "exits": ["forest", "castle"],
        "enemies": []
    },

    "forest": {
        "name": "The Dark Forest",
        "description": "Trees block out the sunlight. You hear something moving nearby.",
        "exits": ["village", "cave"],
        "enemies": ["soldier", "spider", "witch", "wolf"]
    },

    "castle": {
        "name": "The Lost Castle",
        "description": "An ancient castle stands before you.",
        "exits": ["village"]
    },

    "cave": {
        "name": "The Hidden Cave",
        "description": "A dark cave filled with secrets and danger.",
        "exits": ["forest"]
    }
}


locations = {
    "village": {
        "name": "The Village",
        "description": "A quiet village. You see a path leading into the forest.",
        "exits": ["forest"]
    },
    "forest": {
        "name": "The Dark Forest",
        "description": "The trees are dark, and you hear a strange noise.",
        "exits": ["village", "cave"]
    },
    "cave": {
        "name": "The Hidden Cave",
        "description": "You discover a cave filled with mysterious objects.",
        "exits": ["forest"]
    }
}


enemies = {
    "soldier": {
        "name": "Enemy Soldier"
        "health": 20
        "armour": 5
        "attack": 10
        "gold_reward": 5

    },



current_location = "village"

while True:
    location = locations[current_location]

    print("\n==", location["name"], "==")
    print(location["description"])
    print("\nAvailable paths:")

    for number, exit_location in enumerate(location["exits"], start=1):
        print(number, "-", locations[exit_location]["name"])

    print("0 - Quit")

    choice = input("Where would you like to go? ")

    if choice == "0":
        print("Thanks for playing The Lost Kingdom!")
        break

    if choice.isdigit():
        choice = int(choice)

        if 1 <= choice <= len(location["exits"]):
            current_location = location["exits"][choice - 1]
        else:
            print("That is not a valid path.")
    else:
        print("Please enter a number.")