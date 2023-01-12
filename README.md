# Automatic-Screenshotter-for-Presentations
## About

This script uses the PyAutoGUI and PIL libraries to take screenshots of a specified screen at a specified interval and save them to a specified folder. The script prompts the user for the screen to capture, the interval between screenshots, the folder to save the screenshots, and the percentage change required before a new screenshot is taken. The script then compares the current screenshot to the previous screenshot and saves the current screenshot only if the difference in pixels between the two images exceeds the specified percentage. The script will run indefinitely until the user terminates it.

## Setup

1. Install the necessary libraries by running the following command:
```
pip install -r requirements.txt
```
2. Make sure you have a Python environment set up on your machine.
3. Download or copy the script to your machine and save it in a desired location.
4. Open a command prompt or terminal and navigate to the location where the script is saved.
5. Run the script by typing python script_name.py (replace script_name.py with the actual name of the script file) and press enter.
6. The script will prompt you to enter the following information:
- How many seconds of delay between each screenshot do you want?
- Which screen do you want to take a screenshot of? (Enter 1 for the first screen, 2 for the second screen)
- What folder do you want the screenshot to be saved in?
- What percentage change do you want before it'll screenshot? (enter 40 if you want 40%)
7. After providing the required information, the script will start running and take screenshots at the specified interval. The screenshots will be saved in the specified folder and will only be saved if the difference in pixels between the current screenshot and the previous screenshot exceeds the specified percentage change.
8. To stop the script, use the keyboard interrupt (ctrl + c)

Please note that the script will run indefinitely until you manually stop it.

