import json
from python.neuralnetwork.Creatingagg import Network
import numpy as np

data = {}

try:
    with open(r'python\neuralnetwork\network.json', 'r') as f:
        loaded_data = json.load(f)
        data.update(loaded_data)
except Exception as e:
    print(e)

network = Network()

layer2Values = np.array(data["layer2"]["values"])
print(layer2Values)