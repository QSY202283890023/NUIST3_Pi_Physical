# Author: Qin Siyuan
# Date: 2025-04-02  
# Description: Interactive Python quiz with LED feedback.  
# For each correct answer, the green LED (GPIO17) lights up;  
# for each incorrect answer, the red LED (GPIO18) lights up.  
# Make sure the circuit uses two 'positive' GPIO pins:  
# the green LED is connected to GPIO17 and the red LED is connected to GPIO18.  
# Both LEDs share ground connections through the Raspberry Pi.  

import RPi.GPIO as GPIO  # Import the Raspberry Pi GPIO library  
import time              # Import the time module for delays  

# Initialize GPIO settings  
GPIO.setmode(GPIO.BCM)     # Use Broadcom pin numbering  
GPIO.setwarnings(False)    # Disable warnings  

# Set up LED pins as outputs (adjust according to your circuit)  
GREEN_LED_PIN = 17  # Green LED for correct answers  
RED_LED_PIN   = 18  # Red LED for incorrect answers  

GPIO.setup(GREEN_LED_PIN, GPIO.OUT)  
GPIO.setup(RED_LED_PIN, GPIO.OUT)  

# Function to provide LED feedback based on answer evaluation  
def led_feedback(correct=True):  
    if correct:  
        print("Green LED On (Correct Answer)")  
        GPIO.output(GREEN_LED_PIN, GPIO.HIGH)  # Turn on green LED  
        time.sleep(1)  
        GPIO.output(GREEN_LED_PIN, GPIO.LOW)   # Turn off green LED  
    else:  
        print("Red LED On (Incorrect Answer)")  
        GPIO.output(RED_LED_PIN, GPIO.HIGH)      # Turn on red LED  
        time.sleep(1)  
        GPIO.output(RED_LED_PIN, GPIO.LOW)       # Turn off red LED  

# Define quiz questions  
questions = [  
    {  
        "question": "1) Which of the following is NOT a python data type?\n   a) int\n   b) float\n   c) rational\n   d) string\n   e) bool\nYour answer: ",  
        "correct": "c"  
    },  
    {  
        "question": "2) Which of the following is NOT a built-in operation in Python?\n   a) +\n   b) %\n   c) abs()\n   d) sqrt()\nYour answer: ",  
        "correct": "d"  
    },  
    {  
        "question": "3) In a mixed-type expression involving ints and floats, Python will convert:\n   a) floats to ints\n   b) ints to strings\n   c) floats and ints to strings\n   d) ints to floats\nYour answer: ",  
        "correct": "d"  
    },  
    {  
        "question": "4) The best structure for implementing a multi-way decision in Python is:\n   a) if\n   b) if-else\n   c) if-elif-else\n   d) try\nYour answer: ",  
        "correct": "c"  
    },  
    {  
        "question": "5) What statement can be executed in the body of a loop to cause it to terminate?\n   a) if\n   b) exit\n   c) continue\n   d) break\nYour answer: ",  
        "correct": "d"  
    }  
]  

def run_quiz():  
    score = 0  
    print("Welcome to the Python Quiz!\n")  
    for q in questions:  
        answer = input(q["question"]).strip().lower()  
        if answer == q["correct"]:  
            print("Correct!\n")  
            score += 1  
            led_feedback(correct=True)   # Light up green LED for correct answer  
        else:  
            print("Wrong answer. The correct answer is:", q["correct"], "\n")  
            led_feedback(correct=False)  # Light up red LED for incorrect answer  
    print("You scored {}/{}.\n".format(score, len(questions)))  

if __name__ == '__main__':  
    try:  
        run_quiz()  
    finally:  
        GPIO.cleanup()  # Clean up GPIO resources when done
