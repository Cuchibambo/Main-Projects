from math import e
import random
import numpy as np
import json
class Neuron:
    def __init__(self) -> None:
        self.num = 0.0
        self.To_edges = []
        self.From_edges = []
        self.bias = 0.0
    def __str__(self) -> str:
        return str(self.num)

class Layer:
    def __init__(self,size) -> None:
        self.size = size
        self.neurons = [Neuron() for _ in range(self.size)]
    def __str__(self) -> str:
        string = []
        for neuron in self.neurons:
            string.append(str(neuron))
        stringToOut = ' '.join(string)
        return "|"+stringToOut+"|"
    def getValuesVector(self):
        vec_out = np.zeros(shape=(self.size,1))
        for k,v in enumerate(self.neurons):
            vec_out[k,0] = v.num
        return vec_out
    def getBiasesVector(self):
        vec_out = np.zeros(shape=(self.size,1))
        for k,v in enumerate(self.neurons):
            vec_out[k,0] = v.bias
        return vec_out
        

class Edge:
    def __init__(self,From_neuron,To_neuron,weight) -> None:
        self.From_neuron = From_neuron
        self.To_neuron = To_neuron
        self.weight = weight

class Network:
    def sigmoid(self,x):
        return 1/(1+(e**(-x)))
    def __init__(self,layers:list[Layer]) -> None:
        self.layers = layers
        self.edges = []
        for k in range(len(self.layers)):
            for From_neuron in self.layers[k].neurons: # type: ignore
                if k+1 != len(self.layers):
                    for To_neuron in self.layers[k+1].neurons: # type: ignore
                        new_edge = Edge(From_neuron,To_neuron,random.random()*20-10)
                        self.edges.append(new_edge)
                        From_neuron.From_edges.append(new_edge)
                        To_neuron.To_edges.append(new_edge)
    def use(self,input_values):
        for k,v in enumerate(input_values):
            self.layers[0].neurons[k].num = v
        for layer in self.layers:
            if layer != self.layers[0]:
                for neuron in layer.neurons:
                    neuron_value = 0
                    for To_edge in neuron.To_edges:
                        neuron_value += To_edge.weight*To_edge.From_neuron.num
                    neuron.num = self.sigmoid(neuron_value-neuron.bias)
    def saveNetwork(self,file_name):
        data = {}
        for k,layer in enumerate(self.layers):
            values = layer.getValuesVector().tolist()
            biases = layer.getBiasesVector().tolist()
            data["layer" + str(k)] = {"values":values,"biases":biases}
        # data = {"layer " + str(k) : layer.getValuesVector() for k,layer in enumerate(self.layers)}
        # print(r"python\neuralnetwork\\" + file_name)
        try:
            with open(r"python\neuralnetwork\\" + file_name + '.json', "w") as f:
                json.dump(data,f)
                print("JSON file saved successfully!")
        except Exception as e: # type: ignore
            print(e)
        
                
if __name__ == "__main__":
    inputLayer = Layer(784)
    HidenLayer1 = Layer(16)
    HidenLayer2 = Layer(16)
    OutputLayer = Layer(10)
    network = Network([inputLayer,HidenLayer1,HidenLayer2,OutputLayer])
    network.saveNetwork("network")
# network.use([1 for _ in range(784)])
# print(inputLayer)
# print(HidenLayer1)
# print(HidenLayer2)
# print(OutputLayer)