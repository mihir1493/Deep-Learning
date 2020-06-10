# -*- coding: utf-8 -*-
"""
Created on Fri May 29 11:12:38 2020
Creating a checkpoint of the best model weight in a HDF5 type 
Checkpoint Best Neural Network Model Only
@author: LENOVO
"""

# Checkpoint the weights for best model on validation accuracy
import h5py
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt
import numpy
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]
# create model
model = Sequential()

model.add(Dense(12, input_dim=8, init= uniform , activation= "relu" ))
model.add(Dense(8, init= "uniform" , activation= "relu" ))
model.add(Dense(1, init= "uniform" , activation= "sigmoid" ))
# Compile model
model.compile(loss= "binary_crossentropy" , optimizer= "adam" , metrics=[ "accuracy" ])


###########################################################################################

# checkpoint
filepath="weights.best.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor= "val_acc" , verbose=1, save_best_only=True,
mode= "max" )
callbacks_list = [checkpoint]
# Fit the model
model.fit(X, Y, validation_split=0.33, nb_epoch=150, batch_size=10,
callbacks=callbacks_list, verbose=0)

##########################################################################################
# Using the model
# How to load and use weights from a checkpoint
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt
import numpy
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# create model
model = Sequential()
model.add(Dense(12, input_dim=8, init= uniform , activation= relu ))
model.add(Dense(8, init= uniform , activation= relu ))
model.add(Dense(1, init= uniform , activation= sigmoid ))

# load weights
model.load_weights("weights.best.hdf5")


# Compile model (required to make predictions)
model.compile(loss= binary_crossentropy , optimizer= adam , metrics=[ accuracy ])
print("Created model and loaded weights from file")
# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]
# estimate accuracy on whole dataset using loaded weights
scores = model.evaluate(X, Y, verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))




