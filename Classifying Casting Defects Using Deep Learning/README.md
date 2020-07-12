# Analyzing Casting Defects using Image Classification Techniques

## Description
Using deep learning based image classification techniques to identify Manufacturing defects during Casting. <br>
Casting is a manufacturing process in which a liquid material is usually poured into a mold, which contains a hollow cavity of the desired shape, and then allowed to solidify.

**Aim**: Classifying Defective Castings using Deep Learning based Image Classifier

## Types of Defects
* Blow hole
* Pin hole
* Burr
* Shrinkage defects
* Mold material defects 
* Pouring metal defects
* Metallurgical defects

## Dataset
Kaggle: Casting Product Image Data for Quality Inspection
Link: [Dataset Here](https://www.kaggle.com/ravirajsinh45/real-life-industrial-dataset-of-casting-product)

## Demo
![](video.gif)

## Procedure
* Download the Dataset from the Kaggle Url given above
* Extract the test and train images in `Data` folder 
* Open the `Image Classification on Casting Defects.ipynb` notebook
* Use **Transfer Learning** or created **Sequential Deep Learning Model** to create a Model
* Export the Model to `models/model.h5` folder
* Run the `app.py` file and connect to the server 
* Upload the Image, Click Predict and Volla 
   
This is a simple image classification Flask app trained on the top of Keras API. <br>
The trained model (`models/model.h5`) takes an casting image as an input and predict if the casting is defective or Ok.

## Technical Aspect
* This method essentially qualifies as the most basic quality control technique called as Non Destructive Testing.
* This technology coupled with traditional quality control processes serves as an additional set of eyes to catch manufacturing defects that are rather invisible to naked eye.
* Another benefit is the speed at which it detects manufacturing defects without wearing out the human operator.
* Company can divert these essential individuals to core areas or spend time fixing these defects 

## Findings
* The model made using a Sequential Deep Learning Technique obtained a Validation Accuracy of 0.91 on 6633 images used for training.
* The model accuracy can be pushed further using transfer learning techniques such as VGG16 or VGG19 or Mobilenet
* Moreover having images in the order of 30,000+ would have helped in fine tuning the model, but would have been computationally intensive 

## Requirements
The Code is written in Python 3.7. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://keras.io/img/logo.png" width=200>](https://keras.io/) [<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://symbols.getvecta.com/stencil_97/61_tensorflow.7037ae5acc.png" width=200>](https://github.com/tensorflow/tensorflow) 

## Credits
This project wouldnt been possible without the dataset gathered by PILOT TECHNOCAST, Shapar, Rajkot. 
