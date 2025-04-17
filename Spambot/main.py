import os
import time
import pyKey
import pyautogui

# Find the path of you
whatPath = "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2514.4.0_x64__cv1g1gvanyjgm\\WhatsApp.exe"

# Get the message to be sent, the destination, and the number of times it should be sent
msg = input("What message would you like to send?\n")
dest = input("Who would you like to send the message to?\n")
reps = int(input("How many times do you want the message to be sent?\n"))

# Run WhatsApp
os.startfile(whatPath)
time.sleep(5)

# Search for the group and open it, and the message typing bar
for l in dest:
    k = "SPACEBAR" if l == " " else l
    pyKey.press(k, 0.01)
time.sleep(1.5)
pyautogui.click(240, 190)
time.sleep(1)
pyautogui.click(1200, 1005)
time.sleep(1)

# Send message(s)
for rep in range(0, reps):
    for l in msg:
        k = "SPACEBAR" if l == " " else l
        pyKey.press(k, 0.01)
    pyKey.press("ENTER", 0.01)
    time.sleep(0.2)

# Close WhatsApp
os.system(f"taskkill /f /im WhatsApp.exe")
