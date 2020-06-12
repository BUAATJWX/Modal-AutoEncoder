# !/wlptjwx/anaconda3/envs/tensorflow/bin/python3.7
# -*- coding: utf-8 -*-
# *
# ******************************************************************************
# * @filename: test tensorflow&keras basic application
# * @author  : tjwx
# * @version :
# * @date    : 2020.05.22
# * @brief   : This file provides all the  **** functions.
# * @reference:
# ******************************************************************************
# * TODO
# *
# *
# ******************************************************************************
# *

import tensorflow as tf
import tensorflow.keras as keras
import platform

print("Platform:{}".format(platform.platform()))
print("Tensorflow version:{}".format(tf.__version__))
print("Keras version:{}".format(keras.__version__))
print(tf.test.is_gpu_available())

(x_train, y_train), (x_test,y_test) = keras.datasets.mnist.load_data()
x_train, x_test = x_train.reshape((-1,28*28)) / 255.0, x_test.reshape((-1,28*28))/255.0 # flatten
print(x_train.shape,x_test.shape)

