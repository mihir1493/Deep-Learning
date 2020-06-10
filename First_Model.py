# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import numpy
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]

# Manually creation of test and training data 
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=seed)


# create model
model = Sequential()
model.add(Dense(12, input_dim=8, init= uniform , activation= relu ))
model.add(Dense(8, init= uniform , activation= relu ))
model.add(Dense(1, init= uniform , activation= sigmoid ))
# Compile model
model.compile(loss=' binary_crossentropy' , optimizer= 'adam' , metrics=['accuracy'])


# Fit the model
model.fit(X, Y, validation_split=0.33, nb_epoch=150, batch_size=10)

# Fit
#model.fit(X_train, y_train, validation_data=(X_test,y_test), nb_epoch=150, batch_size=10)
# evaluate the model
scores = model.evaluate(X, Y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
