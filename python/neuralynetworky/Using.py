from Creating import Network, Layer
import json
import numpy as np




def error(vec_gotten,vec_expected):
    return np.square(vec_gotten-vec_expected).sum()

def getErrorOfNetwork(network,images_per_number):
    
    errors = 0
    for i in range(10):
        for j in range(images_per_number):
            
            error_gotten = error(vec_out,expected_vectors[i])
            errors += error_gotten
            
    return errors/(images_per_number*10)



network = loadNetwork()

# print(getErrorOfNetwork(network,12))

# For every edge this is its impact on the error
# 2*From_neuron_value*dsigmoid(weight*From_neuron_value+To_neuron_bias)*(To_neuron_value-To_neuron_expected_value)