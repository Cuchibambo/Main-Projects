import matplotlib.pyplot as plt
import numpy as np
import json

try:
    with open("python\EvoSims\Stats.json", "r") as file:
        loaded_data = json.load(file)
        print("JSON file loaded successfully!")
except Exception as e:
    print(f"Error loading file: {e}")

speed = loaded_data[0]
pop = loaded_data[1]
SurvivalRate = loaded_data[2]
x = range(len(pop))
plt.plot(x,pop,'r-')
plt.plot(x,speed,'b-')
plt.plot(x,SurvivalRate,'g-')
plt.show()