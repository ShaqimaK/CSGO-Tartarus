from pymeow import *

class Entity:
    def __init__(self, Offset, Entity):
        self.__offset = Offset
        self.__entity = Entity

    def Pos(self):
        return read_vec3(self.__offset.process, self.__entity + self.__offset.m_vecOrigin)

    def BonePos(self, id):
        boneMatrix = read_int(self.__offset.process, self.__entity + self.__offset.m_dwBoneMatrix)
        return vec3(
            read_float(self.__offset.process, boneMatrix + 0x30 * id + 0x0C),
            read_float(self.__offset.process, boneMatrix + 0x30 * id + 0x1C),
            read_float(self.__offset.process, boneMatrix + 0x30 * id + 0x2C)
        )

    def ViewAngles(self):
        return vec2(
            read_float(self.__offset.process, self.__entity + 300 + 0x04),
            read_float(self.__offset.process, self.__entity + 300)
        )

    def Name(self):
        return read_string(self.__offset.process, read_int(self.__offset.process, read_int(self.__offset.process, self.__offset.module + self.__offset.dwRadarBase) + 0x78) + 0x300 + (0x174 * (read_int(self.__offset.process, self.__entity + 0x64) - 1)))

    def Team(self):
        return read_int(self.__offset.process, self.__entity + self.__offset.m_iTeamNum)

    def Health(self):
        return read_int(self.__offset.process, self.__entity + self.__offset.m_iHealth)

    def ArmorValue(self):
        return read_int(self.__offset.process, self.__entity + self.__offset.m_ArmorValue)

    def ActiveWeapon(self):
        return read_uint(self.__offset.process, self.__entity + self.__offset.m_hActiveWeapon)

    def HasHelmet(self):
        return read_uint(self.__offset.process, self.__entity + self.__offset.m_bHasHelmet)

    def HasDefuser(self):
        return read_uint(self.__offset.process, self.__entity + self.__offset.m_bHasDefuser)

    def IsScoped(self):
        return read_uint(self.__offset.process, self.__entity + self.__offset.m_bIsScoped)

    def Defusing(self):
        return read_bool(self.__offset.process, self.__entity + self.__offset.m_bIsDefusing)

    def FlashDuration(self):
        return read_float(self.__offset.process, self.__entity + self.__offset.m_flFlashDuration)

    def Dormant(self):
        return read_bool(self.__offset.process, self.__entity + self.__offset.m_bDormant)

    def Spotted(self):
        return read_bool(self.__offset.process, self.__entity + self.__offset.m_bSpotted)

    def SpottedByMask(self):
        return read_bool(self.__offset.process, self.__entity + self.__offset.m_bSpottedByMask)