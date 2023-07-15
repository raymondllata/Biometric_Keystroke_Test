import tkinter as tk
import time
import threading
import random
from compute_probabilities import compute_likelihood_stats

PERSON_ONE_DATA = []
PERSON_TWO_DATA = []
MYSTERY_PERSON_DATA = []
PERSON_TRACKER = 0


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
        self.input_entry.bind("<KeyPress>", self.sequence)

        #Can add similarity percentage to each person as a real-time feature

        self.time_label = tk.Label(self.frame, text="Time: 0.00s")
        self.time_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        #implementing reset button
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.started = False

        self.root.mainloop()


    def sequence(self, event):
        if PERSON_TRACKER == 0:
            self.sample_label.config(text="Person A Type Now!")
            PERSON_ONE_DATA.append((event.keycode, self.counter))
        if PERSON_TRACKER == 1:
            self.sample_label.config(text="Person B Type Now!")
            PERSON_TWO_DATA.append((event.keycode, self.counter))
        if PERSON_TRACKER == 2:
            self.sample_label.config(text="Mystery Person Type Now!")
            MYSTERY_PERSON_DATA.append((event.keycode, self.counter))

        if not self.started:
            self.start(event)
        if self.counter >= 5:
            self.started = False
            self.clearSequence()
            print(PERSON_ONE_DATA)



    #start button logic
    def start(self, event):
        #keycodes for shift, alt, ctrl via Google
        if not event.keycode in [16, 17, 18]:
            self.started = True
            t = threading.Thread(target=self.timeThreading)
            t.start()
            #need to add logic to stop after 15 seconds



    #adding timing functionality that runs on a different thread then GUI
    #will need to add data collection here
    def timeThreading(self):
        while self.started and self.counter < 5.0:
            time.sleep(0.1)
            self.counter += 0.1

            timer = self.counter
            self.time_label.config(text=f"Time: {timer:.2f} Seconds")
        self.clearSequence()

    def clearSequence(self):
        self.input_entry.delete(0, tk.END)
        self.counter = 0
        self.started = False
        global PERSON_TRACKER
        PERSON_TRACKER += 1
        if PERSON_TRACKER < 3:
            self.sample_label.config(text="Next Person Type Whenever!")
        else:
            self.sample_label.config(text="Well Done! Computing Probabilities Now")
            #need to import computing logic here
            print(PERSON_ONE_DATA)
            print(PERSON_TWO_DATA)
            print(MYSTERY_PERSON_DATA)
            print("testing...")
            likelihoodStats = compute_likelihood_stats(PERSON_ONE_DATA, PERSON_TWO_DATA, MYSTERY_PERSON_DATA)
            print("Likelihood You Are Person A: " + str(likelihoodStats[0]))
            print("Likelihood You Are Person B: " + str(likelihoodStats[1]))



    #reset test function
    def reset(self):
        pass

dataCollectionGUI()


