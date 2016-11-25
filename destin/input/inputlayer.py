# -*- coding: utf-8 -*-

import abc
import numpy as np
import random
import sys
import logging as log

import tensorflow as tf

class InputLayer(object):
    __metaclass__ = abc.ABCMeta
    """
    TODO doc
    """
    
    def assertions(self):
        #TODO make sure params are sane
        assert(42==42)
    
    def __init__(self, batch_size=1, output_size=(28,28)):
        self.name = 'inputlayer-%08x' % random.getrandbits(32)
        self.output_size = output_size
        self.batch_size = batch_size
        self.batch = []

        with tf.name_scope(self.name) as n_scope:
            self.name_scope = n_scope
            self.input_placeholder = tf.placeholder(dtype=tf.float32, shape=(self.batch_size, output_size[0], output_size[1], 1), name='input')

        self.assertions()
        log.debug("📸 Input Layer initalized")

    def get_tensor_for_region(self, region):
        with tf.name_scope(self.name_scope):
            # crop params are vertical top left, horizontal top left, height, width
            cropped = tf.map_fn(lambda img: tf.image.crop_to_bounding_box(img, region[1], region[0], region[3], region[2]), self.input_placeholder)
            flattened = tf.reshape(cropped, [self.batch_size,-1])

        return flattened








    ## TODO: is this needed anymore?
    def dims_for_receiver(self, receiver):
        for region, callback in self.callbacks:
            if (callback.im_self == receiver):
                return region[2]*region[3] #return width*height

        return -1 #callback not found
