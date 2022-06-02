class Config:
    class __ClassESP:
        class __ClassESPAllies:
            Enable: bool
            Box: bool
            Name: bool
            Bone: bool
            HealthBar: bool
            State: classmethod

        class __ClassESPEnemies:
            Enable: bool
            Box: bool
            Name: bool
            Bone: bool
            HealthBar: bool
            State: classmethod

        class __ClassESPState:
            Enable: bool
            Defuser: bool
            Helmet: bool
            Scoped: bool

        Enable: bool
        Allies = __ClassESPAllies()
        Enemies = __ClassESPEnemies()
        Allies.State = __ClassESPState()
        Enemies.State = __ClassESPState()

    ESP = __ClassESP()
    Debug: bool

def Setup():
    config = Config()

    config.Debug = True

    # ESP
    config.ESP.Enable = True
    # Allies
    config.ESP.Allies.Enable = False
    config.ESP.Allies.Box = False
    config.ESP.Allies.Name = True
    config.ESP.Allies.Bone = False
    config.ESP.Allies.HealthBar = True
    config.ESP.Allies.State.Enable = True
    config.ESP.Allies.State.Defuser = False
    config.ESP.Allies.State.Helmet = False
    config.ESP.Allies.State.Scoped = False
    # Enemies
    config.ESP.Enemies.Enable = True
    config.ESP.Enemies.Box = False
    config.ESP.Enemies.Name = True
    config.ESP.Enemies.Bone = False
    config.ESP.Enemies.HealthBar = True
    config.ESP.Enemies.State.Enable = True
    config.ESP.Enemies.State.Defuser = False
    config.ESP.Enemies.State.Helmet = False
    config.ESP.Enemies.State.Scoped = False

    return config

