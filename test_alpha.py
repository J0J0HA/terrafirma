import terrafirma as tf

i1 = tf.img("img/hard/1.png")
i2 = tf.img("img/hard/2.png")
i3 = tf.img("img/hard/3.png")

# First index manually using AchenbachBasic
c1 = tf.achenbach.basic.find(i1)

# Updating with second frames using AchenbachAlpha
s = tf.achenbach.alpha.ImageSearcher(c1, 75)
c2 = s.update(i2)
c3 = s.update(i3)

tf.show("Output", tf.biran34.basic.mark(i1, c1))
tf.show("Output", tf.biran34.basic.mark(i2, c2))

diff1 = tf.biran34.basic.movement(i2, c1, c2)
tf.show("Result", diff1)

diff2 = tf.biran34.basic.movement(i2, c2, c3)
tf.show("Result", diff2)

tf.save("result1.png", diff1)
tf.save("result2.png", diff2)
