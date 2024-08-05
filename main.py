import pygame
import json
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pilgrim's Progress MUD Game")

# Define the Player class
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.hp = 100
        self.faith = 100

    def apply_event(self, event):
        effect = event["effect"]
        if effect.startswith("hp"):
            self.hp += int(effect[3:])
        elif effect.startswith("faith"):
            self.faith += int(effect[6:])
        print(f"Event effect applied: {effect}")

# Define the NPC class
class NPC(pygame.sprite.Sprite):
    def __init__(self, name, image_path, dialog, location):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.dialog = dialog
        self.location = location

    def speak(self):
        return random.choice(self.dialog)

# Load JSON data
def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

npcs_data = load_data("npcs.json")
locations_data = load_data("locations.json")
events_data = load_data("events.json")

# Create NPC objects
npcs = [NPC(npc["name"], npc["image"], npc["dialog"], npc["location"]) for npc in npcs_data]

# Create a dictionary for location descriptions, coordinates, and images
locations = {
    loc["name"]: {
        "description": loc["description"],
        "x": loc["x"],
        "y": loc["y"],
        "image": pygame.image.load(loc["image"])
    }
    for loc in locations_data
}

# Create a dictionary for location events
location_events = {
    event["location"]: event["events"]
    for event in events_data
}

# Main game function
def main():
    player_name = input("Enter your character's name: ")
    player = Player(player_name, "City of Destruction")

    all_sprites = pygame.sprite.Group()
    for npc in npcs:
        all_sprites.add(npc)

    clock = pygame.time.Clock()
    running = True
    font = pygame.font.Font(None, 36)
    dialog = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get player command
        command = input(f"{player.name}, you are in {player.location}. HP: {player.hp}, Faith: {player.faith}. Enter a command: ").lower()

        if command == "look":
            print(f"You are in {player.location}. {locations[player.location]['description']}")
            dialog = f"You are in {player.location}. {locations[player.location]['description']}"
        elif command == "talk":
            for npc in npcs:
                if npc.location == player.location:
                    dialog = npc.speak()
                    print(f"{npc.name} says: {dialog}")
                    break
            else:
                dialog = "There is no one to talk to here."
                print(dialog)
        elif command == "move":
            new_location = input("Enter the location you want to move to: ")
            if new_location in locations:
                player.location = new_location
                print(f"You move to {new_location}.")
                dialog = f"You move to {new_location}."

                # Trigger random event
                if new_location in location_events:
                    event = random.choice(location_events[new_location])
                    print(event["description"])
                    dialog = event["description"]
                    player.apply_event(event)
            else:
                print("Invalid location.")
                dialog = "Invalid location."
        elif command == "map":
            dialog = "Showing map..."
        elif command == "quit":
            running = False
            continue
        else:
            print("Invalid command.")
            dialog = "Invalid command."

        # Clear the screen
        screen.fill(WHITE)

        # Draw the location image
        location_image = locations[player.location]["image"]
        screen.blit(location_image, (0, 0))

        # Draw all sprites in the current location
        for npc in npcs:
            if npc.location == player.location:
                screen.blit(npc.image, npc.rect)

        # Draw the map
        for location, data in locations.items():
            color = BLUE if location == player.location else RED
            pygame.draw.circle(screen, color, (data['x'], data['y']), 10)
            text = font.render(location, True, BLACK)
            screen.blit(text, (data['x'] + 15, data['y'] - 10))

        if dialog:
            text = font.render(dialog, True, BLACK)
            screen.blit(text, (50, 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()