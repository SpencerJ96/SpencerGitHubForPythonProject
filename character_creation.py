def make_choice(options):
	print(options)
	return input("Enter your choice here")

print("Welcome to the dungeon!")
name = input("Enter your character's name: ")
print (f"Greetings {name}! Your adventure begins")

player_class = make_choice("Select as class! Warrior, Rogue or Mage?")
print(f"Hello {name} You selected {player_class}")


weapon_choice = make_choice("Select a weapon!: Axe, Bow, Staff")