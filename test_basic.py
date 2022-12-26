import terrafirma as tf

i1 = tf.img("img1.png")
i2 = tf.img("img2.png")

c1 = tf.achenbach.basic.find(i1)
c2 = tf.achenbach.basic.find(i2)

# tf.show("Output", tf.biran34.basic.mark(i1, c1))
# tf.show("Output", tf.biran34.basic.mark(i2, c2))

diff = tf.biran34.basic.differences(i2, c1, c2)
tf.show("Output", diff)
