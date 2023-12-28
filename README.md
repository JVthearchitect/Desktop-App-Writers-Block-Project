# Writer's Block

Writer's Block is a Python application that helps you overcome writer's block by encouraging continuous typing. The program provides a distraction-free environment for your writing sessions and automatically saves your progress after a set period of inactivity.

## Features

**Distraction-Free Writing**: The application provides a clean and minimalistic interface to help you focus on your writing.

**Auto-Save**: Your work is automatically saved as a text file ("the_next_great_american_novel.txt") after a period of inactivity.

## Requirements

- Python 3.x
- `time`, `keyboard`, `tkinter` modules

## Usage

1. Clone the repository or download the Python script.
2. Run the script using Python
3. Click the "Get Writing!" button to start your writing session.
4. Type continuously, and the application will save your progress if there is no typing activity for 5 seconds (you can change this in the code).

## Configuration

You can customize the allowed characters for typing by modifying the `allowed_characters` variable in the script. By default, it includes lowercase letters, digits, punctuation, and the space character.
**Example Code*** allowed_characters = string.ascii_lowercase + string.digits + string.punctuation + " "


## Acknowledgments

- Thanks to the creators of Python, tkinter, and keyboard libraries for making this project possible.

Happy writing!
