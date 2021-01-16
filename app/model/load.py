import numpy as np
import keras.models
from keras.models import model_from_json
from scipy.misc import imread, imresize,imshow

import tensorflow as tf
import efficientnet.tfkeras
from tensorflow import keras


def init():
    model = tf.keras.models.load_model('/content/model2.h5')
    graph = tf.get_default_graph()
	return graph