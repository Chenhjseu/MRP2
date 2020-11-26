import pandas as pd
import numpy as np
import random

# Generate Randomly the feedback of UI and user current emotion state
UI_feedback = random.choice([-1， 0， 1]) # -1:dislike 0: no aciton 1:like
current_emotion_state = random.choice([-1, 0, 1])  # -1:negative 0: nature 1: positive

def update_rating(UI_feedback, current_emotion_state):
    if UI_feedback != 0:
        return UI_feedback
    
    else:
        return current_emotion_state
