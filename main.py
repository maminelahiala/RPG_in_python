import player_class.py as pc
game_title = "Adventurer Life"
game_type = "RPG"

print(f"Welcome to the {game_title} \n"
      f"The game is an {game_type}\n")

player_name = input("What is your name? \n")
player_xp = 0
player_hp = 100
player_mana = 0
player_class = 0

print(f"Hello {player_name} \n")
are_you_ready = (input("Are you ready ? (y/n) \n"))
while are_you_ready != "y" :
    are_you_ready = (input("and now?\n"))
print("Let's start by choosing your class")

if player_class == 0 :
    print("You have 12 choices")
    print("you want to play which type of classe?")
    print(pc.player_archane_list)
