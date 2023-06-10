import board

from kmk.bootcfg import bootcfg
import supervisor

supervisor.runtime.autoreload = True

bootcfg(
    sense=board.GP1,   # column
    source=board.GP22,  # row
    midi=False,
    mouse=True,
    storage=True,
    nkro=True,
    usb_id=('mlego m65 rev6', '5x13 ortho'),
)
