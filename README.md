# PyBLF
PyBLF is a python wrapper for read and write BLF file

# configuration PyBLF
In PyBLFLib, you could set the dll path, that the only thing you need to do about the wrapper configuration 
dll = "D:\\local3rd\\BLFLibs\\Win64\\binlog.dll"

# Struture
low level wrapper is only API convert from C API, there is not different.
PyBLF also offer a high level API, which using "enroll" method, so only user need data will be readback, that will save lots of efforts and make code look simple.

# demo for a reader

In the following demo, user need to decliar the BLFObject and even could set addtional filter.

'''
from pyBLFLib import *


class CanMessage(BlfObjectWrapper):
    obj: Optional[VBLCANMessage] = None
    
    def __init__(self):
        super().__init__(BL_OBJ_TYPE.BL_OBJ_TYPE_CAN_MESSAGE, sizeof(VBLCANMessage), VBLCANMessage())

    def filter(self):
        return self.obj.channel == 1


can_msg = CanMessage()
reader = BlfReader()
if reader.open("C:\\Users\\Public\\Documents\\Vector\\CANoe\\Sample Configurations 17.0.201\\IO_HIL\\FDX\\Logging\\Easy.blf") is False:
    print("Open Error!")
reader.enroll(can_msg)
while (obj := reader.read_data()) is not None:
    if obj is can_msg:
        print(can_msg.obj.header.object_time_stamp, can_msg.obj.identifier, can_msg.obj.channel, can_msg.obj.data)
reader.close()
'''
