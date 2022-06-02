from pymeow import *
from Entity import Entity

def ESP(Offset, overlay, entity, font, config, Debug):
    LocalPlayer = read_int(Offset.process, Offset.module + Offset.dwLocalPlayer)
    LocalPlayerData = Entity(Offset, LocalPlayer)

    if entity != LocalPlayer and config.Enable:
        try:
            viewMatrix = read_floats(Offset.process, Offset.module + Offset.dwViewMatrix, 16)

            EntityData = Entity(Offset, entity)
            EntityPos = wts_dx(overlay, viewMatrix, EntityData.Pos())
            EntityHeadPos = wts_dx(overlay, viewMatrix, EntityData.BonePos(8))
            if EntityData.Health() <= 0:
                del viewMatrix, EntityData, EntityPos, EntityHeadPos, LocalPlayer, LocalPlayerData
                return
            if EntityData.Team() == LocalPlayerData.Team():
                if config.Allies.Enable:
                    config = config.Allies
                else:
                    del viewMatrix, EntityData, EntityPos, EntityHeadPos, LocalPlayer, LocalPlayerData
                    return
            else:
                if config.Enemies.Enable:
                    config = config.Enemies
                else:
                    del viewMatrix, EntityData, EntityPos, EntityHeadPos, LocalPlayer, LocalPlayerData
                    return

            width = (EntityHeadPos["y"] - EntityPos["y"]) / 2
            center = width / -2

            BoxColor = "green"
            FontColor = "white"
            if EntityData.Dormant():
                BoxColor = "black"
                FontColor = "black"
            if EntityData.Team() == LocalPlayerData.Team():
                BoxColor = "white"
                FontColor = "white"

            #Box
            if config.Box:
                box(EntityPos["x"] + center, EntityPos["y"], width, width * 2 + 5 + width / 3, 2, rgb("black"))
                box(EntityPos["x"] + center, EntityPos["y"], width, width * 2 + 5 + width / 3, 0.15, rgb(BoxColor))

            #HealthBar
            if config.HealthBar:
                value_bar(
                    EntityPos["x"] + center - 5,
                    EntityPos["y"],
                    EntityPos["x"] + center - 5,
                    EntityHeadPos["y"] + width / 3,
                    2,
                    100,
                    EntityData.Health()
                )

            #Name
            if config.Name:
                font_print(
                    font,
                    EntityPos["x"] + center - 5,
                    EntityHeadPos["y"] + width / 3 + 8,
                    EntityData.Name(),
                    rgb(FontColor)
                )

            #State
            ConfigState = config.State
            if ConfigState.Enable:
                EntityState = []
                if EntityData.HasDefuser() and ConfigState.Defuser:
                    EntityState.append("DF")
                if EntityData.HasHelmet and ConfigState.Helmet:
                    EntityState.append("HM")
                if EntityData.IsScoped and ConfigState.Scoped:
                    EntityState.append("Zoom")

                EntityPos3 = EntityData.Pos()
                EntityAng = EntityData.ViewAngles()
                EntityState.append("x: " + str(int(EntityPos3["x"])) + ", y: " + str(int(EntityPos3["y"])) + ", z: " + str(int(EntityPos3["z"])))
                EntityState.append("x: " + str(int(EntityAng["x"])) + ", y: " + str(int(EntityAng["y"])))
                del EntityPos3, EntityAng

                font_print_lines(
                    font,
                    EntityPos["x"] + center + width + 5,
                    EntityHeadPos["y"] + width / 3 - 2,
                    EntityState,
                    rgb(FontColor),
                    0
                )
            del ConfigState

            #Bone
            if config.Bone:
                if Debug:
                    for i in range(89):
                        try:
                            BonePos = wts_dx(overlay, viewMatrix, EntityData.BonePos(i))

                            font_print(font, BonePos["x"], BonePos["y"] - 6, str(i), rgb("white"))
                            circle(BonePos["x"], BonePos["y"], 2, rgb("white"), True)
                        except:
                            pass

                BoneLine = (
                    (0, 5), (5, 7), #身体
                    (7, 10), (7, 38),
                    (7, 8), #头
                    (10, 11), (11, 12), (12, 14), #手臂
                    (38, 39), (39, 40), (40, 42), #手臂
                    (0, 66), (66, 67), (67, 69),
                    (0, 73), (73, 74), (74, 76)
                )
                for i in range(len(BoneLine)):
                    BoneLinePos1 = wts_dx(overlay, viewMatrix, EntityData.BonePos(BoneLine[i][0]))
                    BoneLinePos2 = wts_dx(overlay, viewMatrix, EntityData.BonePos(BoneLine[i][1]))

                    line(BoneLinePos1["x"], BoneLinePos1["y"], BoneLinePos2["x"], BoneLinePos2["y"], 1, rgb("white"))
                    del BoneLinePos1, BoneLinePos2
                circle(EntityHeadPos["x"], EntityHeadPos["y"], width / 4.8, rgb("white"), False)


            del viewMatrix, EntityData, EntityPos, EntityHeadPos, width, center, font, LocalPlayer, LocalPlayerData
        except:
            pass


