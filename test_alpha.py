import terrafirma as tf

i1 = tf.img("img1.png")
i2 = tf.img("img2.png")

# First index manually using AchenbachBasic
c1 = tf.achenbach.basic.find(i1)

s = tf.achenbach.alpha.ImageSearcher(c1, 75)
# Updating with other frames using AchenbachAlpha
c2 = s.update(i2)

# tf.show("Output", tf.biran34.basic.mark(i1, c1))
# tf.show("Output", tf.biran34.basic.mark(i2, c2))

diff = tf.biran34.basic.differences(i2, c1, c2)
tf.show("Result", diff)
