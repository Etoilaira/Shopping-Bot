# Get necessary tools for the operation
import sched, time, pause, webbrowser, pyautogui
from datetime import datetime
from selenium import webdriver

# Get = link to website and get user input for web item - create final link
url = input("Type the EXACT page of the item on the website you will be purchasing from: ")

# Create function
def action():
    # Use "webbrowser" to open the final link
    # This will open the product's page.
    webbrowser.open(url)

    time.sleep(2)

    coordx = 1215
    coordy = 642

    pyautogui.click(x=coordx,y=coordy,clicks=2)
        

# Pause the program until specific date (year, month number, day number, hour, min, sec)
pause.until(datetime(2022, 1, 24, 12, 38, 0))
action()
