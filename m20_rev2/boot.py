import board

from kmk.bootcfg import bootcfg
import supervisor

supervisor.runtime.autoreload = True

bootcfg(
    sense=board.GP1,   # column
    source=board.GP9,  # row
    midi=False,
    mouse=True,
    storage=True,
    nkro=True,
    usb_id=('mlego m20', '5x4 numpad'),
)
