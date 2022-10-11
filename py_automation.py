import tkinter as tk
import pyautogui as auto
import time

time.sleep(4)
count = 0

class Auto:
    
    def autoWA(self):
        
        with open("animal.txt") as f:
            
            for i in range(99):
                line = f.readline()
                new = "You Are " + line
                auto.write(new)
                auto.press("enter")
                
obj = Auto()
obj.autoWA()