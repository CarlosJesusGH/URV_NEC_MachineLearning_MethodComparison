from NeuralNetwork import *

# --- Initialize NN object ---------------------
NN = NeuralNetwork()
# Network architecture
NN.inputLayerSize = 2
NN.outputLayerSize = 1
NN.numberHiddenLayer = 4
NN.hiddenLayerSizes = [30,40,40,30]  #60 10kEpochs error 9+something
#
NN.epochs = 100000 #200000
NN.trainingFolds = 4
NN.scalar = 0.1
NN.momentum = 0.6
NN.batchSize = 1    # 0 means entire data
# Other settings
# NN.training = False
NN.verbose = 1      # 1 prints cost for every 1000 epochs / 2 prints everything
NN.plot = True
NN.checkWithNumericalGradients = False
NN.randomSeed = 1  # Seed random numbers
# NN.trainDataFile = './input/turbine-input-train'
# NN.validataDataFile = './input/turbine-input-validate'
# NN.trainDataFile = './input/turbine-input-complete'
# NN.trainDataFile = './input/train'
# NN.validataDataFile = './input/validate'
# NN.readDataAndNormalize(NN.trainDataFile, True)
