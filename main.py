from pymeow import *
from Offset import OffsetSetup
from Entity import Entity
import Config
import Rander

if __name__ == '__main__':
    Offset = OffsetSetup()
    overlay = overlay_init()  # Windowed Fullscreen

    font = font_init(12, "Tahoma")
    set_foreground("Counter-Strike: Global Offensive - Direct3D 9")
    cfg = Config.Setup()

    LocalPlayer = read_int(Offset.process, Offset.module + Offset.dwLocalPlayer)
    LocalPlayerData = Entity(Offset, LocalPlayer)

    while overlay_loop(overlay):
        if True:
            for i in range(32):
                Entitys = read_int(Offset.process, Offset.module + Offset.dwEntityList + 0x04 * i)
                if not Entitys == 0:
                    Rander.ESP(Offset, overlay, Entitys, font, cfg.ESP, cfg.Debug)

    overlay_deinit(overlay)
