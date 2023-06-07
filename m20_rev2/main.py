from kb import KMKKeyboard
from kmk.extensions.LED import LED
from kmk.modules.layers import Layers
from kmk.keys import KC
from kmk.modules.tapdance import TapDance

XXX = KC.NO

LWR = KC.TT(1)
RSE = KC.TT(2)

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

mlego_m20 = KMKKeyboard()
mlego_m20.debug_enabled = True

td = TapDance()
td.tap_time = 200

mlego_m20.modules.append(td)

RSE= KC.TD(KC.MO(2), KC.TO(2))
LWR= KC.TD(KC.MO(1), KC.TO(1))

# enable layers
mlego_m20.modules.append(Layers())

#enable leds for layer indicators
#leds = LED(led_pin=[mlego_m20.lower_pin,mlego_m20.raise_pin], val=0)
#mlego_m20.extensions.append(leds)

___ = KC.TRNS

# human codes

mlego_m20.keymap = [
# "qwerty" layer
        [
            a  , b, d, e  ,
            f  , g, i, j  ,
            k  , l, n, o  ,
            p  , q, s, t  ,
            LWR, u, x, RSE,
  ]            ,
# lower layer
  [
            a  , b, c, e  ,
            f  , g, h, j  ,
            k  , l, m, o  ,
            p  , q, r, t  ,
            ___, x, y, ___,
  ]            ,
# raise layer
  [
            a  , c, d, e  ,
            f  , h, i, j  ,
            k  , m, n, o  ,
            p  , r, s, t  ,
            ___, y, z, ___,
  ]            ,
# adjust layer
  [
            a  , b, c, e  ,
            f  , g, h, j  ,
            k  , l, m, o  ,
            p  , q, r, t  ,
            ___, x, y, ___,
  ]
]

if __name__ == '__main__':
    mlego_m20.go()
