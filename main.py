import pyautogui
import keyboard
import os
import PIL
import numpy as np
from PIL import ImageGrab
from functools import partial
import time
import cv2
from PIL import Image, ImageChops

other_count = 0
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
second_screen_width, second_screen_height = pyautogui.size()
second_screen_x = second_screen_width
second_screen_y = 0
count = 0
start_time = time.time()

cooldown_time = int(
    pyautogui.prompt("How many seconds of delay between each screenshot do you want?")
)

other_count = 0

# Get the size of the second screen
second_screen_width, second_screen_height = pyautogui.size()
second_screen_x = second_screen_width
second_screen_y = 0

count = 0
start_time = time.time()


def compare_images(image1, image2):
    # Open the images
    img1 = Image.open(image1)
    img2 = Image.open(image2)

    # Calculate the absolute difference between the two images
    diff = ImageChops.difference(img1, img2)

    # Convert the image to grayscale, get the pixel values of the image and calculate the percentage of different pixels
    diff = diff.convert("L")
    pixels = diff.getdata()
    n_diff = sum(1 for pix in pixels if pix != 0)
    img_size = img1.size[0] * img1.size[1]
    percent_diff = (n_diff / img_size) * 100
    return percent_diff


def save_screenshot(file_path, diff):
    diff = int(diff)
    global count
    global start_time

    count += 1
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    string = f"{file_path}/{count}.png"
    pyautogui.screenshot(
        string,
        region=(
            second_screen_x,
            second_screen_y,
            second_screen_width,
            second_screen_height,
        ),
    )
    im = Image.open(string)
    im = im.crop((0, 0, second_screen_width, second_screen_height))
    im.save(string)

    # Compare current screenshot to last screenshot and only keep it if they're different
    if count > 1:
        percent_diff = compare_images(
            f"{file_path}/{count}.png", f"{file_path}/{count-1}.png"
        )
        if percent_diff < diff:
            im.save(f"{file_path}/{count-1}.png")
            count -= 1
    start_time = time.time()


screen_prompt = pyautogui.prompt(
    "Which screen do you want to take a screenshot of? (Enter 1 for the first screen, 2 for the second screen)"
)
if screen_prompt == "2":
    # Get the size of the second screen
    second_screen_width, second_screen_height = pyautogui.size()
    second_screen_x = second_screen_width
    second_screen_y = 0
else:
    # Get the size of the primary screen
    second_screen_width, second_screen_height = pyautogui.size()
    second_screen_x = 0
    second_screen_y = 0

file_path = pyautogui.prompt("What folder do you want the screenshot to be saved in?")
file_path = os.path.join(file_path, "")
diff = pyautogui.prompt(
    "What percentage change do you want before it'll screenshot? (enter 40 if you want 40%)"
)
# Take the first screenshot
save_screenshot(file_path, diff)

while True:
    if time.time() - start_time >= cooldown_time:
        save_screenshot(file_path, diff)
        time.sleep(cooldown_time)
