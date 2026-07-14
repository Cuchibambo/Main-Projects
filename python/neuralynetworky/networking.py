import numpy as np
import json
from PIL import Image
from mnist import MNIST

def parseData(data):
    layers = []
    for k,v in data.items():
        if k.startswith("layer"):
            size = len(v)
            biases = np.array(v)
            layers.append(Layer(size))
            layers[-1].neuron_biases = biases
    network = Network(layers)
    network.makeEdges()
    for k,v in data.items():
        if k.startswith("weights"):
            weights_position = int(k[8:])
            weigth_matrix = np.array(v)
            network.layers[weights_position].edges = weigth_matrix
    return network

def loadNetwork():
    with open(r"python\neuralynetworky\network.json", "r") as f:
        data = json.load(f)
        return parseData(data)
    
def sigmoid(x):
    return 1/(1+(np.exp(-x)))
def sigmoid_prime(x):
    ex = np.exp(-x)
    return ex/((1+ex)**2)

class Layer:
    def __init__(self,size) -> None:
        self.size = size
        self.neuron_values = np.zeros(shape=(self.size,1))
        self.neuron_biases = np.zeros(shape=(self.size,1))
        self.weighted_sum = np.zeros(shape=(self.size,1))
        self.edges = None
        self.layer_error = None
        self.weights_change = None
        self.biases_change = np.zeros(shape=(self.size,1))
        
class Network:
    def __init__(self,layers) -> None:
        self.layers = layers
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
            if k != 0:
                # from top # from bottom
                # [[[],[]], # to top
                #  [[],[]]] # to bottom
                # edges_matrix = np.zeros(shape=(layer.size,self.layers[k-1].size))
                # for i in range(layer.size):
                #     for j in range(self.layers[k-1].size):
                #         edges_matrix[i,j] = (rnd()*10)-5
                # layer.edges = edges_matrix
                layer.weights_change = np.zeros(shape=(layer.size,self.layers[k-1].size))
                layer.edges = np.random.randn(layer.size, self.layers[k-1].size) * np.sqrt(1/self.layers[k-1].size)
    def use(self,vec_in):
        self.layers[0].neuron_values = vec_in
        for k,layer in enumerate(self.layers):
            if layer != self.layers[-1]:
                next_layer = self.layers[k+1]
                next_layer.weighted_sum = (next_layer.edges@layer.neuron_values) + next_layer.neuron_biases
                next_layer.neuron_values = sigmoid(next_layer.weighted_sum)
    def getData(self):
        data = {}
        for k,layer in enumerate(self.layers):
            if layer != self.layers[0]:
                weights = layer.edges.tolist()
                data["weights " + str(k)] = weights
            biases = layer.neuron_biases.tolist()
            data["layer " + str(k) + " biases"] = biases
        return data
    def save(self):
        try:
            with open(r"python\neuralynetworky\network.json", "w") as f:
                json.dump(self.getData(), f)
                print("Json Saved")
        except Exception as e:
            print(e)
    def getOutputIndex(self):
        output_vec = self.layers[-1].neuron_values
        maximum_value = [-1,0.5]
        for k,v in enumerate(output_vec):
            if v > maximum_value[0]:
                maximum_value[0] = v
                maximum_value[1] = k
        return maximum_value[1]
    def imageToVec(self,image):
        vec = np.zeros(shape=(len(image),1))
        for k,v in enumerate(image):
            vec[k,0] = v/255
        return vec
    def pngImageToVec(self,image_path):
        img = Image.open(image_path)
        img = img.convert("L")
        img = img.resize((28,28),0)
        # img.show()
        # image_list = np.array(img)/255
        # return image_list
        image_list = []
        for y in range(img.size[0]):
            for x in range(img.size[1]):
                image_list.append(img.getpixel((x,y)))
        return self.imageToVec(image_list)
    def test(self):
        mndata = MNIST(r'python\neuralynetworky')
        images, labels = mndata.load_testing()
        amount_right = 0
        for k,image in enumerate(images):
            vec_in = self.imageToVec(image)
            expected_number = labels[k]
            self.use(vec_in)
            # get guessed_number
            guessed_number = self.getOutputIndex()
            if guessed_number == expected_number : amount_right += 1
            # print(f"Accuracy : {amount_right*100/(k+1)} %")
        return amount_right/len(images)
    def getLastLayerError(self,expected_number):
        # expected_vector = self.expected_vectors[expected_number]
        # gotten_vector = self.layers[-1].neuron_values
        # weighted_sum = self.layers[-1].weighted_sum
        # return np.multiply((gotten_vector-expected_vector),sigmoid_prime(weighted_sum))
        expected_vector = self.expected_vectors[expected_number]
        gotten_vector = self.layers[-1].neuron_values
        return gotten_vector - expected_vector
    def train(self,a):
        mndata = MNIST(r'python\neuralynetworky')
        images, labels = mndata.load_training() # Load images
        for image_k,image in enumerate(images): # Go through every image
            # Evaluate image
            vec_in = self.imageToVec(image)
            self.use(vec_in)
            # print(self.layers[-1].neuron_values.flatten())
            # print("label:", labels[image_k])
            # Last layer error
            self.layers[-1].layer_error = self.getLastLayerError(labels[image_k])
            # get other layer errors
            for layer_k in range(len(self.layers)-1):
                reversed_layer_k = len(self.layers)-1-layer_k # reverse order
                current_layer = self.layers[reversed_layer_k]
                previous_layer = self.layers[reversed_layer_k-1]
                previous_layer.layer_error = np.multiply((np.transpose(current_layer.edges))@current_layer.layer_error,sigmoid_prime(previous_layer.weighted_sum))
            # get weights change and biases change
            for layer_k1,layer in enumerate(self.layers):
                if layer != self.layers[0]:
                    previous_layer1 = self.layers[layer_k1-1]
                    layer.weights_change += (layer.layer_error)@(np.transpose(previous_layer1.neuron_values))
                    layer.biases_change += layer.layer_error
            # Average and apply at the end of batches
            if (image_k+1)%100 == 0:
                print(f"{round(100*image_k/len(images),2)}%")
                for layer1 in self.layers:
                    if layer1 != self.layers[0]:
                        layer1.weights_change *= a/256
                        layer1.biases_change *= a/256
                        layer1.edges -= layer1.weights_change
                        layer1.neuron_biases -= layer1.biases_change
                        layer1.weights_change = np.zeros(shape=layer1.weights_change.shape)
                        layer1.biases_change = np.zeros(shape=layer1.biases_change.shape)
            
            
                
            
            
                        
                




a = 0.001


# input_layer = Layer(784)
# hidden_layer_1 = Layer(64)
# hidden_layer_2 = Layer(64)
# output_layer = Layer(10)

# network = Network([input_layer,hidden_layer_1,hidden_layer_2,output_layer])
# network.makeEdges()
# network.train(a)
# print(network.test()*100,"%")
# network.save()

# network = loadNetwork()
# network.train(a)
# network.train(a)
# network.train(a)
# network.train(a)
# network.train(a)
# network.train(a)
# network.train(a)
# network.train(a)
# network.train(a)
# network.train(a)
# print(network.test()*100,"%")
# network.save()

# network = loadNetwork()
# running_count = 0
# for i in range(10):
#     for j in range(1,13):
#         network.use(network.pngImageToVec(fr"python\neuralynetworky\training_data\{i}\input_image ({j}).png"))
#         print(network.getOutputIndex())
#         if network.getOutputIndex() == i:
#             print(i,j)
#             running_count += 1
# print(100*running_count/120,"%")

network = loadNetwork()
# network.use(network.pngImageToVec(fr"python\neuralynetworky\training_data\0\input_image (3).png"))
network.use(network.pngImageToVec(r"python\neuralynetworky\image.png"))
print(network.getOutputIndex())