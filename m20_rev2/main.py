from kb import mlego
from kmk.extensions.LED import LED
from kmk.modules.layers import Layers
from kmk.keys import KC
from kmk.modules.tapdance import TapDance
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler


XXX = KC.NO
___ = KC.TRNS

a = KC.A
b = KC.B
c = KC.C
d = KC.D
e = KC.E
f = KC.F
g = KC.G
h = KC.H
i = KC.I
j = KC.J
k = KC.K
l = KC.L
m = KC.M
n = KC.N
o = KC.O
p = KC.P
q = KC.Q
r = KC.R
s = KC.S
t = KC.T
u = KC.U
v = KC.V
w = KC.W
x = KC.X
y = KC.Y
z = KC.Z

m20 = mlego()
m20.debug_enabled = True

td = TapDance()
td.tap_time = 200
m20.modules.append(td)


RSE = KC.TD(KC.MO(2), KC.TO(2))
LWR = KC.TD(KC.MO(1), KC.TO(1))

# enable layers
layers=Layers()
m20.modules.append(layers)

media_keys = MediaKeys()

#enable leds for layer indicators
#leds = LED(led_pin=[mlego_m20.lower_pin,mlego_m20.raise_pin], val=0)
#mlego_m20.extensions.append(leds)
m20.extensions.append(media_keys)

# Rotary encoder, no push
encoder = EncoderHandler()

m20.modules.append(encoder)

encoder.divisor = 4
encoder.pins = ((m20.en_a, m20.en_b, None),)
encoder.map = (((KC.VOLD, KC.VOLU,___),),)


___ = KC.TRNS

# human codes
m20.keymap = [
# "qwerty" layer
        [
            a  , b, d, e  ,
            f  , g, i, j  ,
            k  , l, n, o  ,
            KC.VOLD  , q, s, KC.VOLU  ,
            LWR, u, x, RSE,
  ]            ,
# lower layer
  [
            a  , b, c, e  ,
            f  , g, h, j  ,
            k  , l, m, o  ,
            p  , q, r, t  ,
            LWR, x, y, ___,
  ]            ,
# raise layer
  [
            a  , c, d, e  ,
            f  , h, i, j  ,
            k  , m, n, o  ,
            p  , r, s, t  ,
            LWR, y, z, ___,
  ]            ,
# adjust layer
  [
            a  , b, c, e  ,
            f  , g, h, j  ,
            k  , l, m, o  ,
            p  , q, r, t  ,
            LWR, x, y, ___,
  ]
]


if __name__ == '__main__':
    m20.go()
