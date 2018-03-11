
import tensorflow as tf
import os
alpha = tf.Variable(3.0, name='alpha')
x = tf.Variable(tf.ones([3, 3], tf.float32), name='x')
y = tf.Variable(tf.ones([3, 3], tf.float32), name='y')
result = (alpha * x) + y
with tf.Session('grpc://{TPU_IP}:8470'.format(**os.environ)) as sess:
  print( "Initializing global variables...")
  tf.global_variables_initializer().run()
  print ("Initialized!")
  output = sess.run(result)
  print ("Output:")
  print (output)
  print ("Done!")

