import json
import terrafirma as tf

i1 = tf.img("img/hard/1.png")
i2 = tf.img("img/hard/2.png")
i3 = tf.img("img/hard/3.png")

s, c1 = tf.achenbach.alpha.Search.from_image(i1, 75)

m1t2, c2 = s.moves(c1, s.use(s.update(i2)))
m2t3, c3 = s.moves(c2, s.use(s.update(i3)))

tf.show("Output", tf.biran34.basic.mark(i1, c1))
tf.show("Output", tf.biran34.basic.mark(i2, c2))
tf.show("Output", tf.biran34.basic.mark(i3, c3))

diff1 = tf.biran34.alpha.visualize(i1.shape, m1t2)
tf.show("Result", diff1)

diff2 = tf.biran34.alpha.visualize(i1.shape, m2t3)
tf.show("Result", diff2)

tf.save("result1.png", diff1)
tf.save("result2.png", diff2)

json.dump({"moves": m1t2}, open("move1to2.json", "w"))
json.dump({"moves": m2t3}, open("move2to3.json", "w"))
