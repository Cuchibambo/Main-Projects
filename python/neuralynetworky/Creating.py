import numpy as np
import json
from random import randint, random as rnd
from math import e
from PIL import Image
from mnist import MNIST

def parseData(data):
    layers = []
    for k,v in data.items():
        if k.startswith("layer"):
            size = len(v)
            biases = np.array(v)
            layers.append(Layer(size))
            layers[-1].applyBiasesVector(biases)
    network = Network(layers)
    network.makeEdges()
    for k,v in data.items():
        if k.startswith("weights"):
            weights_place = int(k[8:])
            weigth_matrix = np.array(v)
            network.applyEdgesMatrix(weigth_matrix,weights_place)
    return network

def loadNetwork():
    with open(r"python\neuralynetworky\network.json", "r") as f:
        data = json.load(f)
        return parseData(data)




def sigmoid(x):
    return 1/(1+(e**(-x)))
def dsigmoid(x):
    ex = e**(-x)
    return ex/((1+ex)**2)

class Neuron:
    def __init__(self) -> None:
        self.value = 0
        self.bias = 0
        self.To_here_edges = []
        self.From_here_edges = []

class Edge:
    def __init__(self,From_this_neuron, To_this_neuron) -> None:
        # self.weight = rnd() # Change maybe
        self.weight = (rnd()*20)-10 # Change maybe
        # self.weight = 0.0 # Change maybe
        self.From_this_neuron = From_this_neuron
        self.To_this_neuron = To_this_neuron

class Layer:
    def __init__(self,size) -> None:
        self.size = size
        self.isInputLayer = False
        self.neurons = [Neuron() for _ in range(self.size)]
        self.weighted_sum = np.zeros(shape=(self.size,1))
        self.weight_change_matrix = None
        self.bias_change_vector = np.zeros(shape=(self.size,1))
    def getValueVector(self):
        vec_out = np.zeros(shape=(self.size,1))
        for k,v in enumerate(self.neurons):
            vec_out[k,0] = v.value
        return vec_out
    def getBiasVector(self):
        vec_out = np.zeros(shape=(self.size,1))
        for k,v in enumerate(self.neurons):
            vec_out[k,0] = v.bias
        return vec_out
    def getEdgesMatrixWeight(self,next_layer):
        # Outputs the edges from this layer to the next one
        weights = np.zeros(shape=(next_layer.size,self.size))
        self.weight_change_matrix = np.zeros(shape=(next_layer.size,self.size))
        for k,From_neuron in enumerate(self.neurons):
            for edge in From_neuron.From_here_edges:
                To_neuron = edge.To_this_neuron
                kp = next_layer.neurons.index(To_neuron)
                weights[kp,k] = edge.weight
        return weights
    def applyValueVector(self,vec_in):
        for k in range(self.size):
            self.neurons[k].value = vec_in[k,0]
    def applyBiasesVector(self,vec_in):
        for k in range(self.size):
            self.neurons[k].bias = vec_in[k,0]
        
            
class Network:
    def __init__(self,layers) -> None:
        self.layers = layers
        self.edges = []
        self.layers[0].isInputLayer = True
        self.expected_vectors = [np.array([[1],[0],[0],[0],[0],[0],[0],[0],[0],[0]]),
                                np.array([[0],[1],[0],[0],[0],[0],[0],[0],[0],[0]]),
                                np.array([[0],[0],[1],[0],[0],[0],[0],[0],[0],[0]]),
                                np.array([[0],[0],[0],[1],[0],[0],[0],[0],[0],[0]]),
                                np.array([[0],[0],[0],[0],[1],[0],[0],[0],[0],[0]]),
                                np.array([[0],[0],[0],[0],[0],[1],[0],[0],[0],[0]]),
                                np.array([[0],[0],[0],[0],[0],[0],[1],[0],[0],[0]]),
                                np.array([[0],[0],[0],[0],[0],[0],[0],[1],[0],[0]]),
                                np.array([[0],[0],[0],[0],[0],[0],[0],[0],[1],[0]]),
                                np.array([[0],[0],[0],[0],[0],[0],[0],[0],[0],[1]]),]
    def makeEdges(self):
        for k,layer in enumerate(self.layers):
            if not layer.isInputLayer:
                for To_neuron in layer.neurons:
                    for From_neuron in self.layers[k-1].neurons:
                        new_edge = Edge(From_neuron,To_neuron)
                        To_neuron.To_here_edges.append(new_edge)
                        From_neuron.From_here_edges.append(new_edge)
                        self.edges.append(new_edge)
    def getData(self):
        data = {}
        for k,layer in enumerate(self.layers):
            biases = layer.getBiasVector().tolist()
            data["layer " + str(k) + " biases"] = biases
            if k+1 < len(self.layers):
                weights = layer.getEdgesMatrixWeight(self.layers[k+1]).tolist()
                data["weights " + str(k)] = weights
        return data
    def save(self):
        try:
            with open(r"python\neuralynetworky\network.json", "w") as f:
                json.dump(self.getData(), f)
                print("Json Saved")
        except Exception as e:
            print(e)
    def run(self,vec_in):
        self.layers[0].applyValueVector(vec_in)
        for k,layer in enumerate(self.layers):
            if k+1 < len(self.layers):
                next_layer = self.layers[k+1]
                weighted_vec = layer.getEdgesMatrixWeight(next_layer)@layer.getValueVector()+next_layer.getBiasVector()
                # print(f"weight {layer.getEdgesMatrixWeight(next_layer)}")
                # print(f"values {layer.getValueVector()}")
                # print(f"Biases {next_layer.getBiasVector()}")
                next_layer.weighted_sum = weighted_vec
                value_vec = sigmoid(weighted_vec) # This might not work but it looks like it does so its good
                next_layer.applyValueVector(value_vec)
        return self.layers[-1].getValueVector()
    def applyEdgesMatrix(self,edge_matrix,starting_layer_index):
        From_layer = self.layers[starting_layer_index]
        To_layer = self.layers[starting_layer_index+1]
        for i,neuron in enumerate(From_layer.neurons):
            for edge in neuron.From_here_edges:
                j = To_layer.neurons.index(edge.To_this_neuron)
                edge.weight = edge_matrix[j,i]
    def imageToVector(self,file_path):
        input_img = Image.open(file_path)
        image_array = np.zeros(shape=(input_img.size[0]*input_img.size[1],1))
        for x in range(input_img.size[0]):
            for y in range(input_img.size[1]):
                image_array[y+x*28] = input_img.getpixel((y,x))[0]/255
        return image_array
    
    def imageToVec(self,image):
        vec_in = np.zeros(shape=(784,1))
        for i,value in enumerate(image):
            vec_in[i,0] = value/255
        return vec_in
    
    def pngImageToVec(self,image_path):
        img = Image.open(image_path)
        image_list = []
        for y in range(img.size[0]):
            for x in range(img.size[1]):
                image_list.append(255-img.getpixel((x,y))[0])
        return self.imageToVec(image_list)
        
        
    # For every edge this is its impact on the error
    # 2*From_neuron_value*dsigmoid(weight*From_neuron_value+To_neuron_bias)*(To_neuron_value-To_neuron_expected_value)
    
    def getPreviousError(self,current_error,layer,next_layer):
        return np.multiply((np.transpose(layer.getEdgesMatrixWeight(next_layer))@current_error),dsigmoid(layer.weighted_sum))
    
    def test(self):
        mndata = MNIST(r'python\neuralynetworky')
        images, labels = mndata.load_testing()
        amount_right = 0
        for k,image in enumerate(images):
            vec_in = self.imageToVec(image)
            expected_number = labels[k]
            vec_out = self.run(vec_in)
            # get guessed_number
            guessed_number = self.getOutputNumber(vec_out)
            if guessed_number == expected_number : amount_right += 1
            print(f"Accuracy : {amount_right*100/(k+1)}%")
        return amount_right/len(images)
            
    def getOutputNumber(self,vec):
        max_value = [-1,0]
        for kk,v in enumerate(vec):
            if v > max_value[0]:
                max_value[0] = v
                max_value[1] = kk
        return max_value[1]
    
    def AverageApplyWeightBiasChanges(self,sample_count):
        for k,layer in enumerate(self.layers):
            if k+1 < len(self.layers):
                layer.weight_change_matrix = layer.weight_change_matrix/sample_count
                old_weight_matrix = layer.getEdgesMatrixWeight(self.layers[k+1])
                new_weight_matrix = old_weight_matrix - layer.weight_change_matrix
                self.applyEdgesMatrix(new_weight_matrix,k)

                layer.bias_change_vector = layer.bias_change_vector/sample_count
                old_bias_vector = layer.getBiasVector()
                new_bias_vector = old_bias_vector - layer.bias_change_vector
                layer.applyBiasesVector(new_bias_vector)
    
    def train(self):
        mndata = MNIST(r'python\neuralynetworky')
        images, labels = mndata.load_testing()
        # indexes = [randint(0,len(images)) for _ in range(batch_size)]
        for k,image in enumerate(images):
            vec_in = self.imageToVec(image)
            vec_expected = self.expected_vectors[labels[k]]
            vec_out = self.run(vec_in)
            # Get last layer error
            layer_errors = []
            layer_errors.append(np.multiply((vec_out-vec_expected),dsigmoid(self.layers[-1].weighted_sum))) # last error
            # Get all layer errors
            for i in range(len(self.layers)-1):
                layer_errors.insert(0, self.getPreviousError(layer_errors[-(1+i)],self.layers[-(2+i)],self.layers[-(1+i)]))
            # Get every layer neuron vector exept last one
            # transpose the matrix
            # Layer error @ neuron layer 
            for kk in range(len(self.layers)-1):
                transposed_neuron = np.transpose(self.layers[kk].getValueVector())
                self.layers[kk].weight_change_matrix += layer_errors[kk+1]@transposed_neuron
            
            # get bias change
            for kk in range(1,len(self.layers)):
                self.layers[kk].bias_change_vector += layer_errors[kk]
            
            print(f"{round(100*k/len(images),2)}%")
            
        # Average and apply weight and bias changes
        self.AverageApplyWeightBiasChanges(len(images))
                
        # for i in range(10):
        #     for j in range(images_per_number):
        #         vec_in = self.imageToVector(fr"python\neuralynetworky\training_data\{i}\input_image ({j+1}).png")
        #         vec_out = self.run(vec_in)
                # for edge in self.edges:
                #     From_neuron = edge.From_this_neuron
                #     To_neuron = edge.To_this_neuron
                #     To_neuron
                #     impact = 2*From_neuron.value*self.dsigmoid(edge.weight*From_neuron.value+To_neuron.bias)*(To_neuron.value-To_neuron_expected_value)
        
        
if __name__ == "__main__":
    inputLayer = Layer(784)
    hiddenLayer1 = Layer(16)
    hiddenLayer2 = Layer(16)
    outputLayer = Layer(10)
    network = Network([inputLayer,hiddenLayer1,hiddenLayer2,outputLayer])
    network.makeEdges()
    network.train()
    network.save()
    
    # network = loadNetwork()
    # network.test()
    
    # print(network.getOutputNumber(network.run(network.pngImageToVec(r"python\neuralynetworky\training_data\9\input_image (10).png"))))
    
    
    
    
    # or
    # images, labels = mndata.load_testing()

    # vec_in = np.array([[1],[1]])
    # print(network.run(vec_in))
    # print(f"Input Layer : {inputLayer.getValueVector()}")
    # print(f"Output Layer : {outputLayer.getValueVector()}")
    
    
