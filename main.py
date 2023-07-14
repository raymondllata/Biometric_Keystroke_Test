import tkinter as tk
import time
import threading
import random

#Class for GUI
class dataCollectionGUI:

    #basic tKinter GUI, can be updated later
    def __init__(self):
        self.root = tk.Tk()
        self.root.title = "Biometric Keystroke Detector"
        self.root.geometry = "800x600"

        self.texts = open("dialogue.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.root)

        self.sample_label = tk.Label(self.frame, text=random.choice(self.texts), font=("Helvetica", 18))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady= 5)

        self.input_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 24))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        #inputing text starts the GUI
        self.input_entry.bind("<KeyDown">, self.start)

        #Can add similarity percentage to each person as a real-time feature

        #implementing reset button
        self.reset_button = tk.button(self.frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.started = False

        self.root.mainloop()

    #start button logic
    def start(self, event):
        if not self.started:
            #keycodes for shift, alt, ctrl via Google
            if not event.keycode in [16, 17, 18]:
                t = threading.Thread(target=self.time_thread)
                t.start()
            #need to add logic to stop after 15 seconds


    #adding timing functionality that runs on a different thread then GUI
    #will need to add data collection here
    def timeThreading(self):
        while self.started:
            time.sleep(0.1)
            self.counter += 0.1



    def reset(self):
        pass

dataCollectionGUI()


