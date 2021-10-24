import numpy,matplotlib.pyplot

class neuralNetwork:

    def __init__(self,inputNodes,hiddenNodes,outputNodes,learningRate):
        # nodes
        self.inodes = inputNodes
        self.hnodes = hiddenNodes
        self.onodes = outputNodes
        # learningrate
        self.lr = learningRate
        #link weight


        # activation function -> sigmoid function
        
    def train(self):
        pass

    def query(self,inputList):
        return outputList

input_nodes = 3
hidden_nodes = 3
output_nodes = 3
learnig_rate = 0.3

nn = neuralNetwork(input_nodes,hidden_nodes,output_nodes,learnig_rate)
