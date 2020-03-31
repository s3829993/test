from sense_hat import SenseHat
import smileys #when on trinket.io
#from test.smiley import Smiley
sense = SenseHat()
sense.clear()

B = [0, 0, 0]
Y = [255, 255, 0]

smile_face = [
B, B, Y, Y, Y, Y, B, B,
B, Y, Y, Y, Y, Y, Y, B, 
Y, Y, B, Y, Y, B, Y, Y, 
Y, Y, B, Y, Y, B, Y, Y, 
Y, Y, Y, Y, Y, Y, Y, Y, 
Y, Y, B, Y, Y, B, Y, Y, #40-47
B, Y, Y, B, B, Y, Y, B, #48-55
B, B, Y, Y, Y, Y, B, B,
]

sad_smile = [
Y, Y, Y, B, B, Y, Y, Y, 
B, Y, B, Y, Y, B, Y, B, 
]

sad_face = smile_face[:]
sad_face[40:56] = sad_smile

happy_smile = [
Y, Y, B, B, B, B, Y, Y, 
B, Y, Y, B, B, Y, Y, B,
]

happy_face = smile_face[:]
happy_face[40:56] = happy_smile

s1 = smileys.Smiley(smile_face)
s1.setPattern(sad_face)
sense.set_pixels(s1.pattern)
