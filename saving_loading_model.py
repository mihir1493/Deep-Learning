# -*- coding: utf-8 -*-
"""
Created on Fri May 29 00:19:53 2020

@author: LENOVO

How to save model weights to HDF5 formatted files and load them again later.
How to save Keras model definitions to JSON files and load them again.
How to save Keras model definitions to YAML files and load them again.

"""
from keras.models import model_from_json

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
# later...
# load json and create model

json_file = open( "model.json" , "r" )
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")


#------------------------------------------------------------->

# MLP for Pima Indians Dataset serialize to YAML and HDF5

from keras.models import model_from_yaml
# serialize model to YAML
model_yaml = model.to_yaml()
with open("model.yaml", "w") as yaml_file:
yaml_file.write(model_yaml)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")

# later...
# load YAML and create model

yaml_file = open( "model.yaml" , "r" )
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")



