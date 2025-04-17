import os
import time
import pyKey
import pyautogui

def sendMessage(whatPath:str, msg:str, dest:str, reps:int = 1):
    """
    Send a whatsapp Message.
    args:
        whatPath (str): Path of the WhatsApp executable
        msg (str): Message to be sent
        dest (str): Group or contact name to send to
        reps (int): Number of times the message should be sent
    """
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
