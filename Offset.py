import sys
import json
from pymeow import *
from requests import get
from win32api import MessageBox
from win32con import MB_YESNO

def OffsetSetup():
    class DataClass:
        pass
    try:
        OffsetData = get("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json").json()
    except:
        if MessageBox(0, "Get CS:GO OffsetData Failed.\nSwitch To Offline Mode? (Offset MayBe Will Inaccurate!)", "Error!",MB_YESNO) == 6:
            OffsetDataFile = open("OffsetOffline.json")
            OffsetData = json.loads(OffsetDataFile.read())
            OffsetDataFile.close()
        else:
            exit(1)
        #exit("Get CS:GO OffsetData Failed." + "\nOffset: " + "https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json")
    [setattr(DataClass, Name, Value) for Name, Value in OffsetData["signatures"].items()]
    [setattr(DataClass, Name, Value) for Name, Value in OffsetData["netvars"].items()]
    DataClass.process = process_by_name("csgo.exe")
    DataClass.module = DataClass.process["modules"]["client.dll"]["baseaddr"]
    DataClass.engine = DataClass.process["modules"]["engine.dll"]["baseaddr"]
    print("csgo.exe - PID:", DataClass.process["pid"], ", Handle:", DataClass.process["handle"])
    del OffsetData
    return DataClass
