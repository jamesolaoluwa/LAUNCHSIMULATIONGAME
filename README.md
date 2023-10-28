# LAUNCH SIMULATION GAME
NASA Launch Game

## Description
The NASA Control Desk Simulator is a Python-based interactive program, where users can simulate the launch of a spacecraft to different planets. This simple, yet engaging program offers my basic understanding of control desk operations and decision-making processes in Python.

## Features
- **Launch Simulation**: Users can choose a planet for their launch mission. The program then simulates a countdown and randomly determines if the launch is successful.
- **View Launch Successes**: Users can view the history of successful launches.
- **Login System**: Includes a basic login system where user credentials are verified from a text file (`userdata.txt`).
- **Success Recording**: Successful launches are recorded to a text file (`success.txt`).

## How to Use
1. **Start the Program**: Run the script to start the simulation.
2. **Login**: Enter your username and password when prompted.
3. **Choose an Option**:
   - Select `1` to initiate a launch simulation.
   - Select `2` to view the list of successful launches.
   - Select `3` to exit the program.

## Installation
1. Ensure you have Python installed on your machine.
2. Download or clone this repository.
3. Run `python nasa_control.py` in your terminal.

## File Structure
- `nasa_control.py`: The main Python script.
- `userdata.txt`: A text file containing usernames and passwords.
- `success.txt`: A text file where successful launches are recorded.

## Requirements
- Python 3.x
- Two text files: `userdata.txt` and `success.txt` in the same directory as your script.
