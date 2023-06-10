from kb import mlego
from kmk.extensions.LED import LED
from kmk.extensions.lock_status import LockStatus
from kmk.modules.layers import Layers as _Layers
from kmk.keys import KC
from kmk.modules.tapdance import TapDance
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.oled import Oled,TextEntry,ImageEntry
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

class LEDLockStatus(LockStatus):                                                                                                    
    def __init__(self, leds):                                                                                                       
        super().__init__()                                                                                                          
        self._leds = leds                                                                                                           
                                                                                                                                    
    def set_lock_leds(self):                                                                                                        
        if self.get_caps_lock():                                                                                                     
            self._leds.set_brightness(100, leds=[0])                                                                                
        else:                                                                                                                       
            self._leds.set_brightness(0, leds=[0])                                                                                  
                                                                                                                                    
    def after_hid_send(self, sandbox):                                                                                              
        super().after_hid_send(sandbox)  # Critically important. Removing this will break lock status.                              
                                                                                                                                    
        if self.report_updated:                                                                                                     
            self.set_lock_leds()

m65 = mlego()
m65.debug_enabled = True

class Layers(_Layers):
    def __init__(self, leds):
      super().__init__()
      self._leds = leds  

    last_layer_active = 0
    
    def after_hid_send(self, keyboard):
      layer_active =  keyboard.active_layers[0]
      if layer_active != self.last_layer_active:
        self.last_layer_active = layer_active 
        led_active = []
        led_inactive = [1,2]
        if layer_active == 1:
            led_active = [1]
            led_inactive = [2]
        elif layer_active == 2:
            led_active = [2]
            led_inactive = [1]
        elif layer_active == 3: 
            led_active = [1,2]
            led_inactive = []
        for led in led_active:
          self._leds.set_brightness(100, leds=[led]) 
        for led in led_inactive: 
          self._leds.set_brightness(0, leds=[led])
          

            

# enable tapdande
td = TapDance()
m65.modules.append(td)
td.tap_time = 250

# enable leds for layer indicators
leds = LED(led_pin=[m65.caps_led, m65.lower_led, m65.raise_led], val=1,brightness=0)
m65.extensions.append(leds)

m65.extensions.append(LEDLockStatus(leds))

# enable layers
layers = Layers(leds)
m65.modules.append(layers)

RSE = KC.TD(KC.MO(2), KC.TT(2))
LWR = KC.TD(KC.MO(1), KC.TT(1))
ADJ = KC.MO(3)

# enable mediakeys
media_keys = MediaKeys()
m65.extensions.append(media_keys)

# Rotary encoder, no push
encoder = EncoderHandler()
m65.modules.append(encoder)

encoder.divisor = 4
encoder.pins = ((m65.en_a, m65.en_b, None),)
encoder.map = (((KC.VOLD, KC.VOLU, ___),),)

f = open("kmk_logo.bmp","rb")
oled = Oled(sda=m65.sda, scl=m65.scl,
            entries=[ TextEntry(text=f"Layer: {x}",layer=i) for x,i in zip(["lower","raise","adjust"],[1,2,3]) ]+
            [ImageEntry(x=22,y=0,image=f,layer=0)])
m65.extensions.append(oled)

combos = Combos()
m65.modules.append(combos)
combos.combos = [
  Sequence((LWR, RSE), ADJ),
]

# fmt: off
# human codes
m65.keymap = [
# "qwerty"
   [
       KC.ESC, KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0, KC.MINS	,KC.BSPC,
       KC.TAB, q, w, e , r ,t , y, u , i , o, p, KC.LBRC,KC.RBRC,
       KC.NUHS	,a,s,d,f,g,h,j,k,l,KC.SCLN,KC.QUOT,KC.ENT,
       KC.LSFT, KC.NUBS	, z,x,c,v,b,n,m,KC.COMM,KC.DOT,KC.UP,KC.SLSH,
       KC.LCTL,KC.APP,LWR, KC.LALT,RSE,KC.SPC,KC.SPC,KC.SPC,KC.RALT, KC.RSFT,KC.LEFT,KC.DOWN	,KC.RGHT,
  ],
# lower layer
  [
            ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,
            ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,
            ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,
            ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,
            ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,
  ],
# raise layer
  [
            ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, KC.EQL,
            ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,
            ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,
            ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,
            ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,
  ],
# adjust layer
  [
           KC.RESET,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___,  KC.RELOAD    ,
            ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,
            ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,
            ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,
            ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, ___,  ___, KC.DEBUG,
  ]
]
# fmt: on

if __name__ == '__main__':
  m65.go()
