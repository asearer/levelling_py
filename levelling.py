import random

class Character:
    """Represents a character in the game."""
    def __init__(self, name, health, attack_power, magic_power, experience=0, level=1):
        """
        Initializes a character with the given attributes.

        Args:
            name (str): The character's name.
            health (int): The character's health points.
            attack_power (int): The character's attack power.
            magic_power (int): The character's magic power.
            experience (int, optional): The character's experience points (default is 0).
            level (int, optional): The character's level (default is 1).
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.magic_power = magic_power
        self.experience = experience
        self.level = level

    def attack(self, target):
        """
        Performs a physical attack on the target character.

        Args:
            target (Character): The character to attack.
        """
        damage = random.randint(1, self.attack_power + 1)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def cast_spell(self, target):
        """
        Casts a magic spell on the target character.

        Args:
            target (Character): The character to cast the spell on.
        """
        if self.magic_power >= 20:
            spell_damage = random.randint(10, 31)
            print(f"{self.name} casts a spell on {target.name} for {spell_damage} magic damage!")
            target.take_magic_damage(spell_damage)
            self.magic_power -= 20
        else:
            print(f"{self.name} doesn't have enough magic power to cast a spell!")

    def take_damage(self, damage):
        """
        Reduces the character's health by the given amount of damage.

        Args:
            damage (int): The amount of damage to take.
        """
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has {self.health} health remaining.")

    def take_magic_damage(self, damage):
        """
        Reduces the character's health by the given amount of magic damage.

        Args:
            damage (int): The amount of magic damage to take.
        """
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated by magic!")
        else:
            print(f"{self.name} has {self.health} health remaining after the magic attack.")

    def gain_experience(self, xp):
        """
        Increases the character's experience points by the given amount.

        Args:
            xp (int): The amount of experience points to gain.
        """
        self.experience += xp
        print(f"{self.name} gains {xp} experience points! Total XP: {self.experience}")

class LevelingSystem:
    """Handles character leveling and experience requirements."""
    def __init__(self):
        """Initializes the leveling system."""
        self.xp_to_level_up = {
            1: 100,
            2: 200,
            3: 300,
            4: 400
            # Add more levels and XP requirements as needed
        }

    def level_up(self, character):
        """
        Checks if a character should level up and updates their attributes accordingly.

        Args:
            character (Character): The character to check for leveling up.
        """
        current_level = character.level
        current_xp = character.experience

        xp_required = self.xp_to_level_up.get(current_level)

        if xp_required is not None and current_xp >= xp_required:
            character.level += 1
            character.magic_power += 10  # Increase magic power on level up
            character.attack_power += 10  # Increase attack power on level up
            print(f"{character.name} leveled up to level {character.level}!")

def main():
    leveling_system = LevelingSystem()  # Create an instance of the leveling system

    # Create two characters
    player = Character("Player", 100, 20, 50)
    enemy = Character("Enemy", 80, 15, 40)

    print(f"A wild {enemy.name} appears! It's time for battle!")

    # Main game loop
    is_player_turn = True
    while player.health > 0 and enemy.health > 0:
        if is_player_turn:
            # Player's turn
            print(f"Your turn, {player.name}!")
            print("Choose your action: (1) Attack, (2) Cast Spell")
            choice = input("Enter your choice: ")

            if choice == "1":
                player.attack(enemy)
                if enemy.health <= 0:
                    xp_gain = random.randint(10, 21)
                    player.gain_experience(xp_gain)
                    leveling_system.level_up(player)  # Check for level up
            elif choice == "2":
                player.cast_spell(enemy)
                if enemy.health <= 0:
                    xp_gain = random.randint(10, 21)
                    player.gain_experience(xp_gain)
                    leveling_system.level_up(player)  # Check for level up
            else:
                print("Invalid choice. Player loses a turn.")
        else:
            # Enemy's turn
            print(f"It's {enemy.name}'s turn!")
            enemy.attack(player)

        # Toggle turns
        is_player_turn = not is_player_turn

    # Determine the winner
    if player.health <= 0:
        print(f"Game over! {enemy.name} wins!")
    else:
        print(f"Victory! {player.name} wins!")

if __name__ == "__main__":
    main()
