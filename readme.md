
# Pilgrim's Progress TXT Based Game

This is a text-based adventure game inspired by John Bunyan's "Pilgrim's Progress." The player, named Christian, embarks on a journey from the City of Destruction to the Celestial City, encountering various characters, events, and challenges along the way.

## This is a work in progress.

## Features

- Text-based commands for player interaction.
- Visual representation of locations and characters.
- Random events that affect the player's health (HP) and faith.
- Balanced mix of positive and negative events.
- Map feature to help navigate through different locations.

## Requirements

- Python 3.x
- Pygame library

## Setup

1. **Install Python**: Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install Pygame**: Install the Pygame library using pip:
   ```bash
   pip install pygame
   ```

3. **Clone the repository**: Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/yourusername/pilgrims-progress-mud-game.git](https://github.com/HelloByeLetsNot/Pilgrims-Progress)
   ```

4. **Navigate to the project directory**:
   ```bash
   cd Pilgrims-Progress
   ```

5. **Add required images**: Ensure you have the following images in the project directory:
   - `evangelist.png`
   - `help.png`
   - `goodwill.png`
   - `interpreter.png`
   - `discretion.png`
   - `apollyon.png`
   - `faithful.png`
   - `vanity_merchant.png`
   - `giant_despair.png`
   - `shepherds.png`
   - `city_of_destruction.png`
   - `slough_of_despond.png`
   - `wicket_gate.png`
   - `house_of_interpreter.png`
   - `hill_difficulty.png`
   - `palace_beautiful.png`
   - `valley_of_humiliation.png`
   - `valley_of_shadow.png`
   - `vanity_fair.png`
   - `doubting_castle.png`
   - `delectable_mountains.png`
   - `enchanted_ground.png`
   - `land_of_beulah.png`
   - `celestial_city.png`

## Usage

1. **Run the game**: Start the game by running the `main.py` script:
   ```bash
   python main.py
   ```

2. **Game commands**:
   - `look`: Get a description of the current location.
   - `talk`: Interact with NPCs in the current location.
   - `move`: Move to a different location. You will be prompted to enter the new location's name.
   - `map`: Display the map.
   - `quit`: Exit the game.

3. **Random events**: As you move to different locations, random events will occur that can affect your health (HP) and faith. Positive events will increase your stats, while negative events will decrease them.

## Example Gameplay

```plaintext
Enter your character's name: Christian
Christian, you are in City of Destruction. HP: 100, Faith: 100. Enter a command: look
You are in City of Destruction. A place full of despair and impending doom.

Christian, you are in City of Destruction. HP: 100, Faith: 100. Enter a command: move
Enter the location you want to move to: Slough of Despond
You move to Slough of Despond.
You are sinking in the mud and struggling to get out.
Event effect applied: hp-10

Christian, you are in Slough of Despond. HP: 90, Faith: 100. Enter a command: talk
Help says: Take my hand and I will help you out of the Slough of Despond.
```

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by John Bunyan's "Pilgrim's Progress."
- Developed using Python and Pygames.