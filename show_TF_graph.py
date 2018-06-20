# This scipt is used to show the construction of the Tensorflow Graph.
# Created by Junbin Huang on 06/02/2018

import tensorflow as tf

output = open('output.txt','w')

with tf.Session() as sess:
    with open('./model.pb', 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read()) 
        output.write(str(graph_def))

output.close()
