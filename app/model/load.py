import numpy as np
import keras.models
# from keras.models import model_from_json
# from scipy.misc.pilutil import imread, imshow

import tensorflow as tf
import efficientnet.tfkeras
from tensorflow import keras

global model
def init():
    model = tf.keras.models.load_model('C:/Users/aarti/Desktop/VS Code projects/MeLanie/app/model/model2.h5')
    # graph = tf.compat.v1.get_default_graph()
    return model
