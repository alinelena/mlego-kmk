from kb import mlego
from kmk.extensions.LED import LED
from kmk.modules.layers import Layers
from kmk.keys import KC
from kmk.modules.tapdance import TapDance
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.oled import Oled
from kmk.modules.combos import Combos, Sequence


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

# enable tapdande
td = TapDance()
m20.modules.append(td)
td.tap_time = 250

# enable layers
layers = Layers()
m20.modules.append(layers)

RSE = KC.TD(KC.MO(2), KC.TT(2))
LWR = KC.TD(KC.MO(1), KC.TT(1))
ADJ = KC.MO(3)

# enable mediakeys
media_keys = MediaKeys()
m20.extensions.append(media_keys)

# enable leds for layer indicators
leds = LED(led_pin=[m20.lower_led, m20.raise_led], val=0)
m20.extensions.append(leds)

# Rotary encoder, no push
encoder = EncoderHandler()
m20.modules.append(encoder)

encoder.divisor = 4
encoder.pins = ((m20.en_a, m20.en_b, None),)
encoder.map = (((KC.VOLD, KC.VOLU, ___),),)

oled = Oled(sda=m20.sda, scl=m20.scl)
m20.extensions.append(oled)
oled.enable

combos = Combos()
m20.modules.append(combos)
combos.combos = [
  Sequence((LWR, RSE), ADJ),
]

# fmt: off
# human codes
m20.keymap = [
# "qwerty"
   [
            a  , b, d, e  ,
            f  , g, i, j  ,
            k  , l, n, o  ,
            p, q,s, t,
            LWR, u, v, RSE,
  ],
# lower layer
  [
            a  , b, c, e  ,
            f  , g, h, j  ,
            k  , l, m, o  ,
            p  , q, r, t  ,
            ___, x, z, ___,
  ],
# raise layer
  [
            a  , c, d, e  ,
            f  , h, i, j  ,
            k  , m, n, o  ,
            p  , r, s, t  ,
            ___, y, y, ___,
  ],
# adjust layer
  [
            KC.RESET, b, c, KC.RELOAD,
            f  , g, h, j  ,
            k  , l, m, o  ,
            p  , q, r, KC.DEBUG   ,
            ___, z, x, ___,
  ]
]
# fmt: on

if __name__ == '__main__':
  m20.go()
