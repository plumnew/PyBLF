from ctypes import *
from typing import Optional

BLINVALID_HANDLE_VALUE = 0xFFFFFFFFFFFFFFFF

BL_FLUSH_STREAM = 0x00000001
BL_FLUSH_FILE = 0x00000002


class DesiredAccess(c_uint32):
    GENERIC_READ = 0x80000000
    GENERIC_WRITE = 0x40000000
    GENERIC_EXECUTE = 0x20000000
    GENERIC_ALL = 0x10000000


class BusType(c_uint32):
    BL_BUS_TYPE_INVALID = 0x00
    BL_BUS_TYPE_CAN = 0x01
    BL_BUS_TYPE_LIN = 0x05
    BL_BUS_TYPE_MOST = 0x06
    BL_BUS_TYPE_FLEXRAY = 0x07
    BL_BUS_TYPE_J1708 = 0x09
    BL_BUS_TYPE_ETHERNET = 0x0B
    BL_BUS_TYPE_WLAN = 0x0D
    BL_BUS_TYPE_AFDX = 0x0E
    BL_BUS_TYPE_KLINE = 0x0F
    BL_BUS_TYPE_A429 = 0x10

    _bus_type_map = {
        0x00: "BL_BUS_TYPE_INVALID",
        0x01: "BL_BUS_TYPE_CAN",
        0x05: "BL_BUS_TYPE_LIN",
        0x06: "BL_BUS_TYPE_MOST",
        0x07: "BL_BUS_TYPE_FLEXRAY",
        0x09: "BL_BUS_TYPE_J1708",
        0x0B: "BL_BUS_TYPE_ETHERNET",
        0x0D: "BL_BUS_TYPE_WLAN",
        0x0E: "BL_BUS_TYPE_AFDX",
        0x0F: "BL_BUS_TYPE_KLINE",
        0x10: "BL_BUS_TYPE_A429",
    }

    def __str__(self):
        return self._bus_type_map[self.value]


class BL_OBJ_TYPE(c_uint32):
    BL_OBJ_SIGNATURE = 0x4A424F4C
    BL_OBJ_TYPE_UNKNOWN = 0
    BL_OBJ_TYPE_CAN_MESSAGE = 1
    BL_OBJ_TYPE_CAN_ERROR = 2
    BL_OBJ_TYPE_CAN_OVERLOAD = 3
    BL_OBJ_TYPE_CAN_STATISTIC = 4
    BL_OBJ_TYPE_APP_TRIGGER = 5
    BL_OBJ_TYPE_ENV_INTEGER = 6
    BL_OBJ_TYPE_ENV_DOUBLE = 7
    BL_OBJ_TYPE_ENV_STRING = 8
    BL_OBJ_TYPE_ENV_DATA = 9
    BL_OBJ_TYPE_LOG_CONTAINER = 10
    BL_OBJ_TYPE_LIN_MESSAGE = 11
    BL_OBJ_TYPE_LIN_CRC_ERROR = 12
    BL_OBJ_TYPE_LIN_DLC_INFO = 13
    BL_OBJ_TYPE_LIN_RCV_ERROR = 14
    BL_OBJ_TYPE_LIN_SND_ERROR = 15
    BL_OBJ_TYPE_LIN_SLV_TIMEOUT = 16
    BL_OBJ_TYPE_LIN_SCHED_MODCH = 17
    BL_OBJ_TYPE_LIN_SYN_ERROR = 18
    BL_OBJ_TYPE_LIN_BAUDRATE = 19
    BL_OBJ_TYPE_LIN_SLEEP = 20
    BL_OBJ_TYPE_LIN_WAKEUP = 21
    BL_OBJ_TYPE_MOST_SPY = 22
    BL_OBJ_TYPE_MOST_CTRL = 23
    BL_OBJ_TYPE_MOST_LIGHTLOCK = 24
    BL_OBJ_TYPE_MOST_STATISTIC = 25
    BL_OBJ_TYPE_reserved_1 = 26
    BL_OBJ_TYPE_reserved_2 = 27
    BL_OBJ_TYPE_reserved_3 = 28
    BL_OBJ_TYPE_FLEXRAY_DATA = 29
    BL_OBJ_TYPE_FLEXRAY_SYNC = 30
    BL_OBJ_TYPE_CAN_DRIVER_ERROR = 31
    BL_OBJ_TYPE_MOST_PKT = 32
    BL_OBJ_TYPE_MOST_PKT2 = 33
    BL_OBJ_TYPE_MOST_HWMODE = 34
    BL_OBJ_TYPE_MOST_REG = 35
    BL_OBJ_TYPE_MOST_GENREG = 36
    BL_OBJ_TYPE_MOST_NETSTATE = 37
    BL_OBJ_TYPE_MOST_DATALOST = 38
    BL_OBJ_TYPE_MOST_TRIGGER = 39
    BL_OBJ_TYPE_FLEXRAY_CYCLE = 40
    BL_OBJ_TYPE_FLEXRAY_MESSAGE = 41
    BL_OBJ_TYPE_LIN_CHECKSUM_INFO = 42
    BL_OBJ_TYPE_LIN_SPIKE_EVENT = 43
    BL_OBJ_TYPE_CAN_DRIVER_SYNC = 44
    BL_OBJ_TYPE_FLEXRAY_STATUS = 45
    BL_OBJ_TYPE_GPS_EVENT = 46
    BL_OBJ_TYPE_FR_ERROR = 47
    BL_OBJ_TYPE_FR_STATUS = 48
    BL_OBJ_TYPE_FR_STARTCYCLE = 49
    BL_OBJ_TYPE_FR_RCVMESSAGE = 50
    BL_OBJ_TYPE_REALTIMECLOCK = 51
    BL_OBJ_TYPE_AVAILABLE2 = 52
    BL_OBJ_TYPE_AVAILABLE3 = 53
    BL_OBJ_TYPE_LIN_STATISTIC = 54
    BL_OBJ_TYPE_J1708_MESSAGE = 55
    BL_OBJ_TYPE_J1708_VIRTUAL_MSG = 56
    BL_OBJ_TYPE_LIN_MESSAGE2 = 57
    BL_OBJ_TYPE_LIN_SND_ERROR2 = 58
    BL_OBJ_TYPE_LIN_SYN_ERROR2 = 59
    BL_OBJ_TYPE_LIN_CRC_ERROR2 = 60
    BL_OBJ_TYPE_LIN_RCV_ERROR2 = 61
    BL_OBJ_TYPE_LIN_WAKEUP2 = 62
    BL_OBJ_TYPE_LIN_SPIKE_EVENT2 = 63
    BL_OBJ_TYPE_LIN_LONG_DOM_SIG = 64
    BL_OBJ_TYPE_APP_TEXT = 65
    BL_OBJ_TYPE_FR_RCVMESSAGE_EX = 66
    BL_OBJ_TYPE_MOST_STATISTICEX = 67
    BL_OBJ_TYPE_MOST_TXLIGHT = 68
    BL_OBJ_TYPE_MOST_ALLOCTAB = 69
    BL_OBJ_TYPE_MOST_STRESS = 70
    BL_OBJ_TYPE_ETHERNET_FRAME = 71
    BL_OBJ_TYPE_SYS_VARIABLE = 72
    BL_OBJ_TYPE_CAN_ERROR_EXT = 73
    BL_OBJ_TYPE_CAN_DRIVER_ERROR_EXT = 74
    BL_OBJ_TYPE_LIN_LONG_DOM_SIG2 = 75
    BL_OBJ_TYPE_MOST_150_MESSAGE = 76
    BL_OBJ_TYPE_MOST_150_PKT = 77
    BL_OBJ_TYPE_MOST_ETHERNET_PKT = 78
    BL_OBJ_TYPE_MOST_150_MESSAGE_FRAGMENT = 79
    BL_OBJ_TYPE_MOST_150_PKT_FRAGMENT = 80
    BL_OBJ_TYPE_MOST_ETHERNET_PKT_FRAGMENT = 81
    BL_OBJ_TYPE_MOST_SYSTEM_EVENT = 82
    BL_OBJ_TYPE_MOST_150_ALLOCTAB = 83
    BL_OBJ_TYPE_MOST_50_MESSAGE = 84
    BL_OBJ_TYPE_MOST_50_PKT = 85
    BL_OBJ_TYPE_CAN_MESSAGE2 = 86
    BL_OBJ_TYPE_LIN_UNEXPECTED_WAKEUP = 87
    BL_OBJ_TYPE_LIN_SHORT_OR_SLOW_RESPONSE = 88
    BL_OBJ_TYPE_LIN_DISTURBANCE_EVENT = 89
    BL_OBJ_TYPE_SERIAL_EVENT = 90
    BL_OBJ_TYPE_OVERRUN_ERROR = 91
    BL_OBJ_TYPE_EVENT_COMMENT = 92
    BL_OBJ_TYPE_WLAN_FRAME = 93
    BL_OBJ_TYPE_WLAN_STATISTIC = 94
    BL_OBJ_TYPE_MOST_ECL = 95
    BL_OBJ_TYPE_GLOBAL_MARKER = 96
    BL_OBJ_TYPE_AFDX_FRAME = 97
    BL_OBJ_TYPE_AFDX_STATISTIC = 98
    BL_OBJ_TYPE_KLINE_STATUSEVENT = 99
    BL_OBJ_TYPE_CAN_FD_MESSAGE = 100
    BL_OBJ_TYPE_CAN_FD_MESSAGE_64 = 101
    BL_OBJ_TYPE_ETHERNET_RX_ERROR = 102
    BL_OBJ_TYPE_ETHERNET_STATUS = 103
    BL_OBJ_TYPE_CAN_FD_ERROR_64 = 104
    BL_OBJ_TYPE_LIN_SHORT_OR_SLOW_RESPONSE2 = 105
    BL_OBJ_TYPE_AFDX_STATUS = 106
    BL_OBJ_TYPE_AFDX_BUS_STATISTIC = 107
    BL_OBJ_TYPE_reserved_4 = 108
    BL_OBJ_TYPE_AFDX_ERROR_EVENT = 109
    BL_OBJ_TYPE_A429_ERROR = 110
    BL_OBJ_TYPE_A429_STATUS = 111
    BL_OBJ_TYPE_A429_BUS_STATISTIC = 112
    BL_OBJ_TYPE_A429_MESSAGE = 113
    BL_OBJ_TYPE_ETHERNET_STATISTIC = 114
    BL_OBJ_TYPE_reserved_5 = 115
    BL_OBJ_TYPE_reserved_6 = 116
    BL_OBJ_TYPE_reserved_7 = 117
    BL_OBJ_TYPE_TEST_STRUCTURE = 118
    BL_OBJ_TYPE_DIAG_REQUEST_INTERPRETATION = 119
    BL_OBJ_TYPE_ETHERNET_FRAME_EX = 120
    BL_OBJ_TYPE_ETHERNET_FRAME_FORWARDED = 121
    BL_OBJ_TYPE_ETHERNET_ERROR_EX = 122
    BL_OBJ_TYPE_ETHERNET_ERROR_FORWARDED = 123
    BL_OBJ_TYPE_FUNCTION_BUS = 124
    BL_OBJ_TYPE_DATA_LOST_BEGIN = 125
    BL_OBJ_TYPE_DATA_LOST_END = 126
    BL_OBJ_TYPE_WATER_MARK_EVENT = 127
    BL_OBJ_TYPE_TRIGGER_CONDITION = 128
    BL_OBJ_TYPE_CAN_SETTING_CHANGED = 129
    BL_OBJ_TYPE_DISTRIBUTED_OBJECT_MEMBER = 130
    BL_OBJ_TYPE_ATTRIBUTE_EVENT = 131
    BL_OBJ_TYPE_DISTRIBUTED_OBJECT_CHANGE = 132
    BL_OBJ_TYPE_ETHERNET_PHY_STATE = 133

    _enum_map = {
        0x4A424F4C: "BL_OBJ_SIGNATURE",
        0: "BL_OBJ_TYPE_UNKNOWN",
        1: "BL_OBJ_TYPE_CAN_MESSAGE",
        2: "BL_OBJ_TYPE_CAN_ERROR",
        3: "BL_OBJ_TYPE_CAN_OVERLOAD",
        4: "BL_OBJ_TYPE_CAN_STATISTIC",
        5: "BL_OBJ_TYPE_APP_TRIGGER",
        6: "BL_OBJ_TYPE_ENV_INTEGER",
        7: "BL_OBJ_TYPE_ENV_DOUBLE",
        8: "BL_OBJ_TYPE_ENV_STRING",
        9: "BL_OBJ_TYPE_ENV_DATA",
        10: "BL_OBJ_TYPE_LOG_CONTAINER",
        11: "BL_OBJ_TYPE_LIN_MESSAGE",
        12: "BL_OBJ_TYPE_LIN_CRC_ERROR",
        13: "BL_OBJ_TYPE_LIN_DLC_INFO",
        14: "BL_OBJ_TYPE_LIN_RCV_ERROR",
        15: "BL_OBJ_TYPE_LIN_SND_ERROR",
        16: "BL_OBJ_TYPE_LIN_SLV_TIMEOUT",
        17: "BL_OBJ_TYPE_LIN_SCHED_MODCH",
        18: "BL_OBJ_TYPE_LIN_SYN_ERROR",
        19: "BL_OBJ_TYPE_LIN_BAUDRATE",
        20: "BL_OBJ_TYPE_LIN_SLEEP",
        21: "BL_OBJ_TYPE_LIN_WAKEUP",
        22: "BL_OBJ_TYPE_MOST_SPY",
        23: "BL_OBJ_TYPE_MOST_CTRL",
        24: "BL_OBJ_TYPE_MOST_LIGHTLOCK",
        25: "BL_OBJ_TYPE_MOST_STATISTIC",
        26: "BL_OBJ_TYPE_reserved_1",
        27: "BL_OBJ_TYPE_reserved_2",
        28: "BL_OBJ_TYPE_reserved_3",
        29: "BL_OBJ_TYPE_FLEXRAY_DATA",
        30: "BL_OBJ_TYPE_FLEXRAY_SYNC",
        31: "BL_OBJ_TYPE_CAN_DRIVER_ERROR",
        32: "BL_OBJ_TYPE_MOST_PKT",
        33: "BL_OBJ_TYPE_MOST_PKT2",
        34: "BL_OBJ_TYPE_MOST_HWMODE",
        35: "BL_OBJ_TYPE_MOST_REG",
        36: "BL_OBJ_TYPE_MOST_GENREG",
        37: "BL_OBJ_TYPE_MOST_NETSTATE",
        38: "BL_OBJ_TYPE_MOST_DATALOST",
        39: "BL_OBJ_TYPE_MOST_TRIGGER",
        40: "BL_OBJ_TYPE_FLEXRAY_CYCLE",
        41: "BL_OBJ_TYPE_FLEXRAY_MESSAGE",
        42: "BL_OBJ_TYPE_LIN_CHECKSUM_INFO",
        43: "BL_OBJ_TYPE_LIN_SPIKE_EVENT",
        44: "BL_OBJ_TYPE_CAN_DRIVER_SYNC",
        45: "BL_OBJ_TYPE_FLEXRAY_STATUS",
        46: "BL_OBJ_TYPE_GPS_EVENT",
        47: "BL_OBJ_TYPE_FR_ERROR",
        48: "BL_OBJ_TYPE_FR_STATUS",
        49: "BL_OBJ_TYPE_FR_STARTCYCLE",
        50: "BL_OBJ_TYPE_FR_RCVMESSAGE",
        51: "BL_OBJ_TYPE_REALTIMECLOCK",
        52: "BL_OBJ_TYPE_AVAILABLE2",
        53: "BL_OBJ_TYPE_AVAILABLE3",
        54: "BL_OBJ_TYPE_LIN_STATISTIC",
        55: "BL_OBJ_TYPE_J1708_MESSAGE",
        56: "BL_OBJ_TYPE_J1708_VIRTUAL_MSG",
        57: "BL_OBJ_TYPE_LIN_MESSAGE2",
        58: "BL_OBJ_TYPE_LIN_SND_ERROR2",
        59: "BL_OBJ_TYPE_LIN_SYN_ERROR2",
        60: "BL_OBJ_TYPE_LIN_CRC_ERROR2",
        61: "BL_OBJ_TYPE_LIN_RCV_ERROR2",
        62: "BL_OBJ_TYPE_LIN_WAKEUP2",
        63: "BL_OBJ_TYPE_LIN_SPIKE_EVENT2",
        64: "BL_OBJ_TYPE_LIN_LONG_DOM_SIG",
        65: "BL_OBJ_TYPE_APP_TEXT",
        66: "BL_OBJ_TYPE_FR_RCVMESSAGE_EX",
        67: "BL_OBJ_TYPE_MOST_STATISTICEX",
        68: "BL_OBJ_TYPE_MOST_TXLIGHT",
        69: "BL_OBJ_TYPE_MOST_ALLOCTAB",
        70: "BL_OBJ_TYPE_MOST_STRESS",
        71: "BL_OBJ_TYPE_ETHERNET_FRAME",
        72: "BL_OBJ_TYPE_SYS_VARIABLE",
        73: "BL_OBJ_TYPE_CAN_ERROR_EXT",
        74: "BL_OBJ_TYPE_CAN_DRIVER_ERROR_EXT",
        75: "BL_OBJ_TYPE_LIN_LONG_DOM_SIG2",
        76: "BL_OBJ_TYPE_MOST_150_MESSAGE",
        77: "BL_OBJ_TYPE_MOST_150_PKT",
        78: "BL_OBJ_TYPE_MOST_ETHERNET_PKT",
        79: "BL_OBJ_TYPE_MOST_150_MESSAGE_FRAGMENT",
        80: "BL_OBJ_TYPE_MOST_150_PKT_FRAGMENT",
        81: "BL_OBJ_TYPE_MOST_ETHERNET_PKT_FRAGMENT",
        82: "BL_OBJ_TYPE_MOST_SYSTEM_EVENT",
        83: "BL_OBJ_TYPE_MOST_150_ALLOCTAB",
        84: "BL_OBJ_TYPE_MOST_50_MESSAGE",
        85: "BL_OBJ_TYPE_MOST_50_PKT",
        86: "BL_OBJ_TYPE_CAN_MESSAGE2",
        87: "BL_OBJ_TYPE_LIN_UNEXPECTED_WAKEUP",
        88: "BL_OBJ_TYPE_LIN_SHORT_OR_SLOW_RESPONSE",
        89: "BL_OBJ_TYPE_LIN_DISTURBANCE_EVENT",
        90: "BL_OBJ_TYPE_SERIAL_EVENT",
        91: "BL_OBJ_TYPE_OVERRUN_ERROR",
        92: "BL_OBJ_TYPE_EVENT_COMMENT",
        93: "BL_OBJ_TYPE_WLAN_FRAME",
        94: "BL_OBJ_TYPE_WLAN_STATISTIC",
        95: "BL_OBJ_TYPE_MOST_ECL",
        96: "BL_OBJ_TYPE_GLOBAL_MARKER",
        97: "BL_OBJ_TYPE_AFDX_FRAME",
        98: "BL_OBJ_TYPE_AFDX_STATISTIC",
        99: "BL_OBJ_TYPE_KLINE_STATUSEVENT",
        100: "BL_OBJ_TYPE_CAN_FD_MESSAGE",
        101: "BL_OBJ_TYPE_CAN_FD_MESSAGE_64",
        102: "BL_OBJ_TYPE_ETHERNET_RX_ERROR",
        103: "BL_OBJ_TYPE_ETHERNET_STATUS",
        104: "BL_OBJ_TYPE_CAN_FD_ERROR_64",
        105: "BL_OBJ_TYPE_LIN_SHORT_OR_SLOW_RESPONSE2",
        106: "BL_OBJ_TYPE_AFDX_STATUS",
        107: "BL_OBJ_TYPE_AFDX_BUS_STATISTIC",
        108: "BL_OBJ_TYPE_reserved_4",
        109: "BL_OBJ_TYPE_AFDX_ERROR_EVENT",
        110: "BL_OBJ_TYPE_A429_ERROR",
        111: "BL_OBJ_TYPE_A429_STATUS",
        112: "BL_OBJ_TYPE_A429_BUS_STATISTIC",
        113: "BL_OBJ_TYPE_A429_MESSAGE",
        114: "BL_OBJ_TYPE_ETHERNET_STATISTIC",
        115: "BL_OBJ_TYPE_reserved_5",
        116: "BL_OBJ_TYPE_reserved_6",
        117: "BL_OBJ_TYPE_reserved_7",
        118: "BL_OBJ_TYPE_TEST_STRUCTURE",
        119: "BL_OBJ_TYPE_DIAG_REQUEST_INTERPRETATION",
        120: "BL_OBJ_TYPE_ETHERNET_FRAME_EX",
        121: "BL_OBJ_TYPE_ETHERNET_FRAME_FORWARDED",
        122: "BL_OBJ_TYPE_ETHERNET_ERROR_EX",
        123: "BL_OBJ_TYPE_ETHERNET_ERROR_FORWARDED",
        124: "BL_OBJ_TYPE_FUNCTION_BUS",
        125: "BL_OBJ_TYPE_DATA_LOST_BEGIN",
        126: "BL_OBJ_TYPE_DATA_LOST_END",
        127: "BL_OBJ_TYPE_WATER_MARK_EVENT",
        128: "BL_OBJ_TYPE_TRIGGER_CONDITION",
        129: "BL_OBJ_TYPE_CAN_SETTING_CHANGED",
        130: "BL_OBJ_TYPE_DISTRIBUTED_OBJECT_MEMBER",
        131: "BL_OBJ_TYPE_ATTRIBUTE_EVENT",
        132: "BL_OBJ_TYPE_DISTRIBUTED_OBJECT_CHANGE",
        133: "BL_OBJ_TYPE_ETHERNET_PHY_STATE",
    }

    def __str__(self):
        return self._enum_map[self.value]


class SYSTEMTIME(Structure):
    _fields_ = [
        ("wYear", c_uint16),
        ("wMonth", c_uint16),
        ("wDayOfWeek", c_uint16),
        ("wDay", c_uint16),
        ("wHour", c_uint16),
        ("wMinute", c_uint16),
        ("wSecond", c_uint16),
        ("wMilliseconds", c_uint16),
    ]
    _pack_ = 8

    @property
    def pYear(self) -> int:
        return self.wYear

    @property
    def pMonth(self) -> int:
        return self.wMonth

    @property
    def pDayOfWeek(self) -> int:
        return self.wDayOfWeek

    @property
    def pDay(self) -> int:
        return self.wDay

    @property
    def pHour(self) -> int:
        return self.wHour

    @property
    def pMinute(self) -> int:
        return self.wMinute

    @property
    def pSecond(self) -> int:
        return self.wSecond

    @property
    def pMilliseconds(self) -> int:
        return self.wMilliseconds


class VBLObjectHeaderBase(Structure):
    _fields_ = [
        ("mSignature", c_uint32),
        ("mHeaderSize", c_uint16),
        ("mHeaderVersion", c_uint16),
        ("mObjectSize", c_uint32),
        ("mObjectType", BL_OBJ_TYPE),
    ]
    _pack_ = 8

    @property
    def pSignature(self) -> int:
        return self.mSignature

    @property
    def pHeaderSize(self) -> int:
        return self.mHeaderSize

    @property
    def pHeaderVersion(self) -> int:
        return self.mHeaderVersion

    @property
    def pObjectSize(self) -> int:
        return self.mObjectSize

    @property
    def pObjectType(self) -> BL_OBJ_TYPE:
        return self.mObjectType


class VBLFileStatistics(Structure):
    _fields_ = [
        ("mStatisticsSize", c_uint32),
        ("mApplicationID", c_uint8),
        ("mApplicationMajor", c_uint8),
        ("mApplicationMinor", c_uint8),
        ("mApplicationBuild", c_uint8),
        ("mFileSize", c_uint64),
        ("mUncompressedFileSize", c_uint64),
        ("mObjectCount", c_uint32),
        ("mObjectsRead", c_uint32),
    ]
    _pack_ = 8

    @property
    def pStatisticsSize(self) -> int:
        return self.mStatisticsSize

    @property
    def pApplicationID(self) -> int:
        return self.mApplicationID

    @property
    def pApplicationMajor(self) -> int:
        return self.mApplicationMajor

    @property
    def pApplicationMinor(self) -> int:
        return self.mApplicationMinor

    @property
    def pApplicationBuild(self) -> int:
        return self.mApplicationBuild

    @property
    def pFileSize(self) -> int:
        return self.mFileSize

    @property
    def pUncompressedFileSize(self) -> int:
        return self.mUncompressedFileSize

    @property
    def pObjectCount(self) -> int:
        return self.mObjectCount

    @property
    def pObjectsRead(self) -> int:
        return self.mObjectsRead


# Base object header type definition
class VBLFileStatisticsEx(Structure):
    _fields_ = [
        ("mStatisticsSize", c_uint32),
        ("mApplicationID", c_uint8),
        ("mApplicationMajor", c_uint8),
        ("mApplicationMinor", c_uint8),
        ("mApplicationBuild", c_uint8),
        ("mFileSize", c_uint64),
        ("mUncompressedFileSize", c_uint64),
        ("mObjectCount", c_uint32),
        ("mObjectsRead", c_uint32),
        ("mMeasurementStartTime", SYSTEMTIME),
        ("mLastObjectTime", SYSTEMTIME),
        ("mReserved", c_uint32 * 18),
    ]
    _pack_ = 8

    @property
    def pStatisticsSize(self) -> int:
        return self.mStatisticsSize

    @property
    def pApplicationID(self) -> int:
        return self.mApplicationID

    @property
    def pApplicationMajor(self) -> int:
        return self.mApplicationMajor

    @property
    def pApplicationMinor(self) -> int:
        return self.mApplicationMinor

    @property
    def pApplicationBuild(self) -> int:
        return self.mApplicationBuild

    @property
    def pFileSize(self) -> int:
        return self.mFileSize

    @property
    def pUncompressedFileSize(self) -> int:
        return self.mUncompressedFileSize

    @property
    def pObjectCount(self) -> int:
        return self.mObjectCount

    @property
    def pObjectsRead(self) -> int:
        return self.mObjectsRead

    @property
    def pMeasurementStartTime(self) -> SYSTEMTIME:
        return self.mMeasurementStartTime

    @property
    def pLastObjectTime(self) -> SYSTEMTIME:
        return self.mLastObjectTime

    @property
    def pReserved(self):
        return list(self.mReserved)


# Extended base object header type definition with dynamic extendible objects
class VBLVarObjectHeader(Structure):
    _fields_ = [
        ("mBase", VBLObjectHeaderBase),
        ("mObjectFlags", c_uint32),
        ("mObjectStaticSize", c_uint16),
        ("mObjectVersion", c_uint16),
        ("mObjectTimeStamp", c_uint64),
    ]
    _pack_ = 8

    @property
    def pBase(self) -> VBLObjectHeaderBase:
        return self.mBase

    @property
    def pObjectFlags(self) -> int:
        return self.mObjectFlags

    @property
    def pObjectStaticSize(self) -> int:
        return self.mObjectStaticSize

    @property
    def pObjectVersion(self) -> int:
        return self.mObjectVersion

    @property
    def pObjectTimeStamp(self) -> int:
        return self.mObjectTimeStamp


# Object header type definitions
class VBLObjectHeader(Structure):
    _fields_ = [
        ("mBase", VBLObjectHeaderBase),
        ("mObjectFlags", c_uint32),
        ("mClientIndex", c_uint16),
        ("mObjectVersion", c_uint16),
        ("mObjectTimeStamp", c_uint64),
    ]
    _pack_ = 8
    
    @property
    def pBase(self) -> VBLObjectHeaderBase:
        return self.mBase

    @property
    def pObjectFlags(self) -> int:
        return self.mObjectFlags

    @property
    def pClientIndex(self) -> int:
        return self.mClientIndex

    @property
    def pObjectVersion(self) -> int:
        return self.mObjectVersion

    @property
    def pObjectTimeStamp(self) -> int:
        return self.mObjectTimeStamp


class VBLObjectHeader2(Structure):
    _fields_ = [
        ("mBase", VBLObjectHeaderBase),
        ("mObjectFlags", c_uint32),
        ("mTimeStampStatus", c_uint8),
        ("mReserved1", c_uint8),
        ("mObjectVersion", c_uint16),
        ("mObjectTimeStamp", c_uint64),
        ("mOriginalTimeStamp", c_uint64),
    ]
    _pack_ = 8


'''
######################################CAN Object Define####################################
'''


# CAN objects
class VBLObjectHeader(Structure):
    _fields_ = [
        ("mBase", VBLObjectHeaderBase),
        ("mObjectFlags", c_uint32),
        ("mClientIndex", c_uint16),
        ("mObjectVersion", c_uint16),
        ("mObjectTimeStamp", c_uint64),
    ]
    _pack_ = 8

    @property
    def pBase(self) -> Optional[VBLObjectHeaderBase]:
        return self.mBase

    @property
    def pObjectFlags(self):
        return self.mObjectFlags

    @property
    def pClientIndex(self):
        return self.mClientIndex

    @property
    def pObjectVersion(self):
        return self.mObjectVersion

    @property
    def pObjectTimeStamp(self):
        return self.mObjectTimeStamp


class VBLCANMessage(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mFlags', c_uint8),
        ('mDLC', c_uint8),
        ('mID', c_uint32),
        ('mData', c_ubyte * 8),
    ]
    _pack_ = 8

    @property
    def pHeader(self) -> Optional[VBLObjectHeader]:
        return self.mHeader

    @property
    def pChannel(self):
        return self.mChannel

    @property
    def pFlags(self):
        return self.mFlags

    @property
    def pDLC(self):
        return self.mDLC

    @property
    def pID(self):
        return self.mID

    @property
    def pData(self):
        return list(self.mData)


class VBLCANErrorFrame(Structure):
    _fields_ = [
        ("mBase", VBLObjectHeaderBase),
        ("mChannel", c_uint16),
        ("mLength", c_uint16),
    ]
    _pack_ = 8


class VBLCANErrorFrameExt(Structure):
    _fields_ = [
        ("mHeader", VBLObjectHeader),
        ("mChannel", c_uint16),
        ("mLength", c_uint16),
        ("mFlags", c_uint32),
        ("mECC", c_uint8),
        ("mPosition", c_uint8),
        ("mDLC", c_uint8),
        ("mReserved1", c_uint8),
        ("mFrameLengthInNS", c_uint32),
        ("mID", c_uint32),
        ("mFlagsExt", c_uint16),
        ("mReserved2", c_uint16),
        ("mData", c_uint8 * 8),
    ]
    _pack_ = 8


class VBLCANOverloadFrame(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mDummy', c_uint16),
    ]
    _pack_ = 8


class VBLCANDriverStatistic(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mBusLoad', c_uint16),
        ('mStandardDataFrames', c_uint32),
        ('mExtendedDataFrames', c_uint32),
        ('mStandardRemoteFrames', c_uint32),
        ('mExtendedRemoteFrames', c_uint32),
        ('mErrorFrames', c_uint32),
        ('mOverloadFrames', c_uint32),
    ]
    _pack_ = 8


class VBLCANDriverError(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mTXErrors', c_uint8),
        ('mRXErrors', c_uint8),
        ('mErrorCode', c_uint32),
    ]
    _pack_ = 8


class VBLCANDriverErrorExt(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mTXErrors', c_uint8),
        ('mRXErrors', c_uint8),
        ('mErrorCode', c_uint32),
        ('mFlags', c_uint32),
        ('mState', c_uint8),
        ('mReserved1', c_uint8),
        ('mReserved2', c_uint16),
        ('mReserved3', c_uint32 * 4),
    ]
    _pack_ = 8


class VBLCANDriverHwSync(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mFlags', c_uint8),
        ('mDummy', c_uint8),
    ]
    _pack_ = 8


# CAN extended objects
class VBLCANMessage2(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mFlags', c_uint8),
        ('mDLC', c_uint8),
        ('mID', c_uint32),
        ('mData', c_uint8 * 8),
        ('mFrameLength', c_uint32),
        ('mBitCount', c_uint8),
        ('mReserved1', c_uint8),
        ('mReserved2', c_uint16),
    ]
    _pack_ = 8


'''
######################################CANFD Object Define####################################
'''


class VBLCANFDMessage(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mFlags', c_uint8),
        ('mDLC', c_uint8),
        ('mID', c_uint32),
        ('mFrameLength', c_uint32),
        ('mArbBitCount', c_uint8),
        ('mCANFDFlags', c_uint8),
        ('mValidDataBytes', c_uint8),
        ('mReserved1', c_uint8),
        ('mReserved2', c_uint32),
        ('mData', c_uint8 * 64),
    ]
    _pack_ = 8


class VBLCANFDMessage(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mFlags', c_uint8),
        ('mDLC', c_uint8),
        ('mID', c_uint32),
        ('mFrameLength', c_uint32),
        ('mArbBitCount', c_uint8),
        ('mCANFDFlags', c_uint8),
        ('mValidDataBytes', c_uint8),
        ('mReserved1', c_uint8),
        ('mReserved2', c_uint32),
        ('mData', c_ubyte * 64),
    ]
    _pack_ = 8


class VBLCANFDExtFrameData(Structure):
    _fields_ = [
        ('mBTRExtArb', c_uint32),
        ('mBTRExtData', c_uint32),
        # 可能在将来的版本中添加其他字段
    ]
    _pack_ = 8


class VBLCANFDMessage64(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),  # 假设 VBLObjectHeader 已在代码中定义
        ('mChannel', c_uint8),
        ('mDLC', c_uint8),
        ('mValidDataBytes', c_uint8),
        ('mTxCount', c_uint8),
        ('mID', c_uint32),
        ('mFrameLength', c_uint32),
        ('mFlags', c_uint32),
        ('mBtrCfgArb', c_uint32),
        ('mBtrCfgData', c_uint32),
        ('mTimeOffsetBrsNs', c_uint32),
        ('mTimeOffsetCrcDelNs', c_uint32),
        ('mBitCount', c_uint16),
        ('mDir', c_uint8),
        ('mExtDataOffset', c_uint8),
        ('mCRC', c_uint32),
        ('mData', c_uint8 * 64),
        ('mExtFrameData', VBLCANFDExtFrameData),
    ]
    _pack_ = 8


class VBLCANSettingsChanged(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),  # 假设 VBLObjectHeader 已在代码中定义
        ('mChannel', c_uint16),
        ('mChangedType', c_uint8),
        ('mBitTimings', VBLCANFDExtFrameData),
    ]
    _pack_ = 8


class VBLCANFDErrorFrame64(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint8),
        ('mDLC', c_uint8),
        ('mValidDataBytes', c_uint8),
        ('mECC', c_uint8),
        ('mFlags', c_uint16),
        ('mErrorCodeExt', c_uint16),
        ('mExtFlags', c_uint16),
        ('mExtDataOffset', c_uint8),
        ('reserved1', c_uint8),
        ('mID', c_uint32),
        ('mFrameLength', c_uint32),
        ('mBtrCfgArb', c_uint32),
        ('mBtrCfgData', c_uint32),
        ('mTimeOffsetBrsNs', c_uint32),
        ('mTimeOffsetCrcDelNs', c_uint32),
        ('mCRC', c_uint32),
        ('mErrorPosition', c_uint16),
        ('mReserved2', c_uint16),
        ('mData', c_uint8 * 64),
        ('mExtFrameData', VBLCANFDExtFrameData),
    ]
    _pack_ = 8


'''
######################################LIN Object Define####################################
'''


class VBLLINMessage(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mID', c_uint8),
        ('mDLC', c_uint8),
        ('mData', c_uint8 * 8),
        ('mFSMId', c_uint8),
        ('mFSMState', c_uint8),
        ('mHeaderTime', c_uint8),
        ('mFullTime', c_uint8),
        ('mCRC', c_uint16),
        ('mDir', c_uint8),
        ('mReserved', c_uint8),
    ]
    _pack_ = 8


class VBLLINCRCError(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mID', c_uint8),
        ('mDLC', c_uint8),
        ('mData', c_uint8 * 8),
        ('mFSMId', c_uint8),
        ('mFSMState', c_uint8),
        ('mHeaderTime', c_uint8),
        ('mFullTime', c_uint8),
        ('mCRC', c_uint16),
        ('mDir', c_uint8),
        ('mReserved', c_uint8),
    ]
    _pack_ = 8


class VBLLINDLCInfo(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mID', c_uint8),
        ('mDLC', c_uint8),
    ]
    _pack_ = 8


class VBLLINChecksumInfo(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),  # 假设 VBLObjectHeader 已在代码中定义
        ('mChannel', c_uint16),
        ('mID', c_uint8),
        ('mChecksumModel', c_uint8),
    ]
    _pack_ = 8


class VBLLINReceiveError(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),  # 假设 VBLObjectHeader 已在代码中定义
        ('mChannel', c_uint16),
        ('mID', c_uint8),
        ('mDLC', c_uint8),
        ('mFSMId', c_uint8),
        ('mFSMState', c_uint8),
        ('mHeaderTime', c_uint8),
        ('mFullTime', c_uint8),
        ('mStateReason', c_uint8),
        ('mOffendingByte', c_uint8),
        ('mShortError', c_uint8),
        ('mTimeoutDuringDlcDetection', c_uint8),
    ]
    _pack_ = 8


class VBLLINSendError(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mID', c_uint8),
        ('mDLC', c_uint8),
        ('mFSMId', c_uint8),
        ('mFSMState', c_uint8),
        ('mHeaderTime', c_uint8),
        ('mFullTime', c_uint8),
    ]
    _pack_ = 8


class VBLLINSlaveTimeout(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mSlaveID', c_uint8),
        ('mStateID', c_uint8),
        ('mFollowStateID', c_uint32),
    ]
    _pack_ = 8


class VBLLINSchedulerModeChange(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mOldMode', c_uint8),
        ('mNewMode', c_uint8),
        ('mOldSlot', c_uint8),
        ('mNewSlot', c_uint8),
        ('mFirstEventAfterWakeUp', c_uint8),
    ]
    _pack_ = 8


class VBLLINSyncError(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mDummy', c_uint16),
        ('mTimeDiff', c_uint32 * 4),
    ]
    _pack_ = 8


class VBLLINBaudrateEvent(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mDummy', c_uint16),
        ('mBaudrate', c_int32),
    ]
    _pack_ = 8


class VBLLINSleepModeEvent(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mReason', c_uint8),
        ('mFlags', c_uint8),
    ]
    _pack_ = 8


class VBLLINWakeupEvent(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mSignal', c_uint8),
        ('mExternal', c_uint8),
    ]
    _pack_ = 8


class VBLLINSpikeEvent(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mWidth', c_uint32),
    ]
    _pack_ = 8


class VBLLINStatisticEvent(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mBusLoad', c_double),
        ('mBurstsTotal', c_uint32),
        ('mBurstsOverrun', c_uint32),
        ('mFramesSent', c_uint32),
        ('mFramesReceived', c_uint32),
        ('mFramesUnanswered', c_uint32),
    ]
    _pack_ = 8


class VBLLINBusEvent(Structure):
    _fields_ = [
        ('mSOF', c_uint64),
        ('mEventBaudrate', c_uint32),
        ('mChannel', c_uint16),
        ('mReserved', c_uint8 * 2),
    ]
    _pack_ = 8


class VBLLINSynchFieldEvent(Structure):
    _fields_ = [
        ('mLinBusEvent', VBLLINBusEvent),
        ('mSynchBreakLength', c_uint64),
        ('mSynchDelLength', c_uint64),
    ]
    _pack_ = 8


class VBLLINMessageDescriptor(Structure):
    _fields_ = [
        ('mLinSynchFieldEvent', VBLLINSynchFieldEvent),
        ('mSupplierID', c_uint16),
        ('mMessageID', c_uint16),
        ('mNAD', c_uint8),
        ('mID', c_uint8),
        ('mDLC', c_uint8),
        ('mChecksumModel', c_uint8),
    ]
    _pack_ = 8


class VBLLINDatabyteTimestampEvent(Structure):
    _fields_ = [
        ('mLinMsgDescrEvent', VBLLINMessageDescriptor),
        ('mDatabyteTimestamps', c_uint64 * 9),
    ]
    _pack_ = 8


class VBLLINMessage2(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mLinTimestampEvent', VBLLINDatabyteTimestampEvent),
        ('mData', c_uint8 * 8),
        ('mCRC', c_uint16),
        ('mDir', c_uint8),
        ('mSimulated', c_uint8),
        ('mIsETF', c_uint8),
        ('mETFAssocIndex', c_uint8),
        ('mETFAssocETFId', c_uint8),
        ('mFSMId', c_uint8),
        ('mFSMState', c_uint8),
        ('mReserved', c_uint8 * 3),
        ('mRespBaudrate', c_uint32),
        ('mExactHeaderBaudrate', c_double),
        ('mEarlyStopbitOffset', c_uint32),
        ('mEarlyStopbitOffsetResponse', c_uint32),
    ]
    _pack_ = 8


class VBLLINSendError2(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mLinMsgDescrEvent', VBLLINMessageDescriptor),
        ('mEOH', c_uint64),
        ('mIsETF', c_uint8),
        ('mFSMId', c_uint8),
        ('mFSMState', c_uint8),
        ('mReserved', c_uint8),
        ('mReserved2', c_uint8 * 4),
        ('mExactHeaderBaudrate', c_double),
        ('mEarlyStopbitOffset', c_uint32),
    ]
    _pack_ = 8


class VBLLINSyncError2(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mLinSynchFieldEvent', VBLLINSynchFieldEvent),
        ('mTimeDiff', c_uint16 * 4),
    ]
    _pack_ = 8


class VBLLINCRCError2(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mLinTimestampEvent', VBLLINDatabyteTimestampEvent),
        ('mData', c_uint8 * 8),
        ('mCRC', c_uint16),
        ('mDir', c_uint8),
        ('mFSMId', c_uint8),
        ('mFSMState', c_uint8),
        ('mSimulated', c_uint8),
        ('mReserved', c_uint8 * 2),
        ('mRespBaudrate', c_uint32),
        ('mReserved2', c_uint8 * 4),
        ('mExactHeaderBaudrate', c_double),
        ('mEarlyStopbitOffset', c_uint32),
        ('mEarlyStopbitOffsetResponse', c_uint32),
    ]
    _pack_ = 8


class VBLLINReceiveError2(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mLinTimestampEvent', VBLLINDatabyteTimestampEvent),
        ('mData', c_uint8 * 8),
        ('mFSMId', c_uint8),
        ('mFSMState', c_uint8),
        ('mStateReason', c_uint8),
        ('mOffendingByte', c_uint8),
        ('mShortError', c_uint8),
        ('mTimeoutDuringDlcDetection', c_uint8),
        ('mIsETF', c_uint8),
        ('mHasDatabytes', c_uint8),
        ('mRespBaudrate', c_uint32),
        ('mReserved', c_uint8 * 4),
        ('mExactHeaderBaudrate', c_double),
        ('mEarlyStopbitOffset', c_uint32),
        ('mEarlyStopbitOffsetResponse', c_uint32),
    ]
    _pack_ = 8


class VBLLINWakeupEvent2(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mLinBusEvent', VBLLINBusEvent),
        ('mLengthInfo', c_uint8),
        ('mSignal', c_uint8),
        ('mExternal', c_uint8),
        ('mReserved', c_uint8),
    ]
    _pack_ = 8


class VBLLINSpikeEvent2(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mLinBusEvent', VBLLINBusEvent),
        ('mWidth', c_uint32),
        ('mInternal', c_uint8),
        ('mReserved', c_uint8 * 3),
    ]
    _pack_ = 8


class VBLLINLongDomSignalEvent(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mLinBusEvent', VBLLINBusEvent),
        ('mType', c_uint8),
        ('mReserved', c_uint8 * 3),
    ]
    _pack_ = 8


class VBLLINLongDomSignalEvent2(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mLinBusEvent', VBLLINBusEvent),
        ('mType', c_uint8),
        ('mReserved', c_uint8 * 7),
        ('mLength', c_uint64),
    ]
    _pack_ = 8


class VBLLINUnexpectedWakeup(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mLinBusEvent', VBLLINBusEvent),
        ('mWidth', c_uint64),
        ('mSignal', c_uint8),
        ('mReserved', c_uint8 * 7),
    ]
    _pack_ = 8


class VBLLINShortOrSlowResponse(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mLinTimestampEvent', VBLLINDatabyteTimestampEvent),
        ('mNumberOfRespBytes', c_uint32),
        ('mRespBytes', c_uint8 * 9),
        ('mSlowResponse', c_uint8),
        ('mInterruptedByBreak', c_uint8),
        ('mReserved', c_uint8),
    ]
    _pack_ = 8


class VBLLINShortOrSlowResponse2(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mLinTimestampEvent', VBLLINDatabyteTimestampEvent),
        ('mNumberOfRespBytes', c_uint32),
        ('mRespBytes', c_uint8 * 9),
        ('mSlowResponse', c_uint8),
        ('mInterruptedByBreak', c_uint8),
        ('mReserved', c_uint8),
        ('mExactHeaderBaudrate', c_double),
        ('mEarlyStopbitOffset', c_uint32),
    ]
    _pack_ = 8


class VBLLINDisturbanceEvent(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mID', c_uint8),
        ('mDisturbingFrameID', c_uint8),
        ('mDisturbanceType', c_uint32),
        ('mByteIndex', c_uint32),
        ('mBitIndex', c_uint32),
        ('mBitOffsetInSixteenthBits', c_uint32),
        ('mDisturbanceLengthInSixteenthBits', c_uint32),
    ]
    _pack_ = 8


'''
######################################FLEXRAY objects Define####################################
'''


class VBLFLEXRAYData(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mMUX', c_uint8),
        ('mLen', c_uint8),
        ('mMessageID', c_uint16),
        ('mCRC', c_uint16),
        ('mDir', c_uint8),
        ('mDummy1', c_uint8),
        ('mDummy2', c_uint16),
        ('mDataBytes', c_uint8 * 12),
    ]
    _pack_ = 8


class VBLFLEXRAYSync(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mMUX', c_uint8),
        ('mLen', c_uint8),
        ('mMessageID', c_uint16),
        ('mCRC', c_uint16),
        ('mDir', c_uint8),
        ('mDummy1', c_uint8),
        ('mDummy2', c_uint16),
        ('mDataBytes', c_uint8 * 11),
        ('mCycle', c_uint8),
    ]
    _pack_ = 8


class VBLFLEXRAYV6StartCycleEvent(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mDir', c_uint8),
        ('mLowTime', c_uint8),
        ('mFPGATick', c_uint32),
        ('mFPGATickOverflow', c_uint32),
        ('mClientIndex', c_uint32),
        ('mClusterTime', c_uint32),
        ('mDataBytes', c_uint8 * 2),
        ('mReserved', c_uint16),
    ]
    _pack_ = 8


class VBLFLEXRAYV6Message(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mDir', c_uint8),
        ('mLowTime', c_uint8),
        ('mFPGATick', c_uint32),
        ('mFPGATickOverflow', c_uint32),
        ('mClientIndex', c_uint32),
        ('mClusterTime', c_uint32),
        ('mFrameId', c_uint16),
        ('mHeaderCRC', c_uint16),
        ('mFrameState', c_uint16),
        ('mLength', c_uint8),
        ('mCycle', c_uint8),
        ('mHeaderBitMask', c_uint8),
        ('mReserved1', c_uint8),
        ('mReserved2', c_uint16),
        ('mDataBytes', c_uint8 * 64),
    ]
    _pack_ = 8


class VBLFLEXRAYStatusEvent(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mVersion', c_uint16),
        ('mStatusType', c_uint16),
        ('mInfoMask1', c_uint16),
        ('mInfoMask2', c_uint16),
        ('mInfoMask3', c_uint16),
        ('mReserved', c_uint16 * 16),
    ]
    _pack_ = 8


class VBLFLEXRAYVFrReceiveMsgEx(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mVersion', c_uint16),
        ('mChannelMask', c_uint16),
        ('mDir', c_uint16),
        ('mClientIndex', c_uint32),
        ('mClusterNo', c_uint32),
        ('mFrameId', c_uint16),
        ('mHeaderCRC1', c_uint16),
        ('mHeaderCRC2', c_uint16),
        ('mByteCount', c_uint16),
        ('mDataCount', c_uint16),
        ('mCycle', c_uint16),
        ('mTag', c_uint32),
        ('mData', c_uint32),
        ('mFrameFlags', c_uint32),
        ('mAppParameter', c_uint32),
        ('mFrameCRC', c_uint32),
        ('mFrameLengthNS', c_uint32),
        ('mFrameId1', c_uint16),
        ('mPDUOffset', c_uint16),
        ('mBlfLogMask', c_uint16),
        ('mReservedW', c_uint16),
        ('mReserved', c_uint32 * 6),
        ('mDataBytes', c_uint8 * 254),
    ]
    _pack_ = 8


class VBLFLEXRAYVFrReceiveMsg(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mVersion', c_uint16),
        ('mChannelMask', c_uint16),
        ('mDir', c_uint8),
        ('mClientIndex', c_uint32),
        ('mClusterNo', c_uint32),
        ('mFrameId', c_uint16),
        ('mHeaderCRC1', c_uint16),
        ('mHeaderCRC2', c_uint16),
        ('mByteCount', c_uint16),
        ('mDataCount', c_uint16),
        ('mCycle', c_uint8),
        ('mTag', c_uint32),
        ('mData', c_uint32),
        ('mFrameFlags', c_uint32),
        ('mAppParameter', c_uint32),
        ('mDataBytes', c_uint8 * 254),
    ]
    _pack_ = 8


class VBLFLEXRAYVFrStartCycle(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mVersion', c_uint16),
        ('mChannelMask', c_uint16),
        ('mDir', c_uint8),
        ('mCycle', c_uint8),
        ('mClientIndex', c_uint32),
        ('mClusterNo', c_uint32),
        ('mNmSize', c_uint16),
        ('mDataBytes', c_uint8 * 12),
        ('mTag', c_uint32),
        ('mData', c_uint32 * 5),
        ('mReserved', c_uint16),
    ]
    _pack_ = 8


class VBLFLEXRAYVFrStatus(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mVersion', c_uint16),
        ('mChannelMask', c_uint16),
        ('mCycle', c_uint8),
        ('mClientIndex', c_uint32),
        ('mClusterNo', c_uint32),
        ('mWus', c_uint32),
        ('mCcSyncState', c_uint32),
        ('mTag', c_uint32),
        ('mData', c_uint32 * 2),
        ('mReserved', c_uint16 * 16),
    ]
    _pack_ = 8


class VBLFLEXRAYVFrError(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mVersion', c_uint16),
        ('mChannelMask', c_uint16),
        ('mCycle', c_uint8),
        ('mClientIndex', c_uint32),
        ('mClusterNo', c_uint32),
        ('mTag', c_uint32),
        ('mData', c_uint32 * 4),
        ('mReserved', c_uint16),
    ]
    _pack_ = 8


'''
######################################Environment variable object Define####################################
'''


class VBLEnvironmentVariable(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mNameLength', c_uint32),
        ('mDataLength', c_uint32),
        ('mName', POINTER(c_uint8)),
        ('mData', POINTER(c_uint8)),
    ]
    _pack_ = 8


'''
######################################System variable object Define####################################
'''


class VBLSystemVariable(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mType', c_uint32),
        ('mRepresentation', c_uint32),
        ('mReserved', c_uint32 * 2),
        ('mNameLength', c_uint32),
        ('mDataLength', c_uint32),
        ('mName', POINTER(c_uint8)),
        ('mData', POINTER(c_uint8)),
    ]
    _pack_ = 8


'''
######################################GPS event object Define####################################
'''


class VBLGPSEvent(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mFlags', c_uint32),
        ('mChannel', c_uint16),
        ('mReserved', c_uint16),
        ('mLatitude', c_double),
        ('mLongitude', c_double),
        ('mAltitude', c_double),
        ('mSpeed', c_double),
        ('mCourse', c_double),
    ]
    _pack_ = 8


'''
######################################Ethernet frame object Define####################################
'''


class VBLEthernetFrame(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mSourceAddress', c_uint8 * 6),
        ('mChannel', c_uint16),
        ('mDestinationAddress', c_uint8 * 6),
        ('mDir', c_uint16),
        ('mType', c_uint16),
        ('mTPID', c_uint16),
        ('mTCI', c_uint16),
        ('mPayLoadLength', c_uint16),
        ('mPayLoad', POINTER(c_uint8)),
    ]
    _pack_ = 8


class VBLEthernetFrameEx(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mStructLength', c_uint16),
        ('mFlags', c_uint16),
        ('mChannel', c_uint16),
        ('mHardwareChannel', c_uint16),
        ('mFrameDuration', c_uint64),
        ('mFrameChecksum', c_uint32),
        ('mDir', c_uint16),
        ('mFrameLength', c_uint16),
        ('mFrameHandle', c_uint32),
        ('mReserved', c_uint32),
        ('mFrameData', POINTER(c_uint8)),  # 使用 POINTER 来表示指向数据的指针
    ]
    _pack_ = 8


class VBLEthernetRxError(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mStructLength', c_uint16),
        ('mChannel', c_uint16),
        ('mDir', c_uint16),
        ('mHardwareChannel', c_uint16),
        ('mFcs', c_uint32),
        ('mFrameDataLength', c_uint16),
        ('mReserved2', c_uint16),
        ('mError', c_uint32),
        ('mFrameData', POINTER(c_uint8)),  # 使用 POINTER 来表示指向数据的指针
    ]
    _pack_ = 8


class VBLEthernetErrorEx(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mStructLength', c_uint16),
        ('mFlags', c_uint16),
        ('mChannel', c_uint16),
        ('mHardwareChannel', c_uint16),
        ('mFrameDuration', c_uint64),
        ('mFrameChecksum', c_uint32),
        ('mDir', c_uint16),
        ('mFrameLength', c_uint16),
        ('mFrameHandle', c_uint32),
        ('mError', c_uint32),
        ('mFrameData', POINTER(c_uint8)),
    ]
    _pack_ = 8


class VBLEthernetStatus(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mFlags', c_uint16),
        ('mLinkStatus', c_uint8),
        ('mEthernetPhy', c_uint8),
        ('mDuplex', c_uint8),
        ('mMdi', c_uint8),
        ('mConnector', c_uint8),
        ('mClockMode', c_uint8),
        ('mPairs', c_uint8),
        ('mHardwareChannel', c_uint8),
        ('mBitrate', c_uint32),
        ('mLinkUpDuration', c_uint64),
    ]
    _pack_ = 8


class VBLEthernetPhyState(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mFlags', c_uint16),
        ('mPhyState', c_uint8),
        ('mPhyEvent', c_uint8),
        ('mHardwareChannel', c_uint8),
    ]
    _pack_ = 8


class VBLEthernetStatistic(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mRcvOk_HW', c_uint64),
        ('mXmitOk_HW', c_uint64),
        ('mRcvError_HW', c_uint64),
        ('mXmitError_HW', c_uint64),
        ('mRcvBytes_HW', c_uint64),
        ('mXmitBytes_HW', c_uint64),
        ('mRcvNoBuffer_HW', c_uint64),
        ('mSQI', c_int16),
        ('mHardwareChannel', c_uint16),
    ]
    _pack_ = 8


'''
######################################WLAN frame object Define####################################
'''


class VBLWlanFrame(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mFlags', c_uint16),
        ('mDir', c_uint8),
        ('mRadioChannel', c_uint8),
        ('mSignalStrength', c_int16),
        ('mSignalQuality', c_uint16),
        ('mFrameLength', c_uint16),
        ('mFrameData', POINTER(c_uint8)),
    ]
    _pack_ = 8


class VBLWlanStatistic(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mChannel', c_uint16),
        ('mFlags', c_uint16),
        ('mRxPacketCount', c_uint32),
        ('mRxByteCount', c_uint32),
        ('mTxPacketCount', c_uint32),
        ('mTxByteCount', c_uint32),
        ('mCollisionCount', c_uint32),
        ('mErrorCount', c_uint32),
    ]
    _pack_ = 8


'''
######################################Application trigger object Define####################################
'''


class VBLAppTrigger(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mPreTriggerTime', c_uint64),
        ('mPostTriggerTime', c_uint64),
        ('mChannel', c_uint16),
        ('mFlags', c_uint16),
        ('mAppSecific2', c_uint32),
    ]
    _pack_ = 8


'''
######################################Application text object Define####################################
'''


class VBLAppText(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mSource', c_uint32),
        ('mReserved', c_uint32),
        ('mTextLength', c_uint32),
        ('mText', c_char_p),
    ]
    _pack_ = 8


'''
######################################Realtime clock object Define####################################
'''


class VBLRealtimeClock(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mTime', c_uint64),
        ('mLoggingOffset', c_uint64),
    ]
    _pack_ = 8


'''
######################################File statistics####################################
'''


class VBLFileStatistics(Structure):
    _fields_ = [
        ('mStatisticsSize', c_uint32),
        ('mApplicationID', c_uint8),
        ('mApplicationMajor', c_uint8),
        ('mApplicationMinor', c_uint8),
        ('mApplicationBuild', c_uint8),
        ('mFileSize', c_uint64),
        ('mUncompressedFileSize', c_uint64),
        ('mObjectCount', c_uint32),
        ('mObjectsRead', c_uint32),
    ]
    _pack_ = 8


class VBLFileStatisticsEx(Structure):
    _fields_ = [
        ('mStatisticsSize', c_uint32),
        ('mApplicationID', c_uint8),
        ('mApplicationMajor', c_uint8),
        ('mApplicationMinor', c_uint8),
        ('mApplicationBuild', c_uint8),
        ('mFileSize', c_uint64),
        ('mUncompressedFileSize', c_uint64),
        ('mObjectCount', c_uint32),
        ('mObjectsRead', c_uint32),
        ('mMeasurementStartTime', SYSTEMTIME),
        ('mLastObjectTime', SYSTEMTIME),
        ('mReserved', c_uint32 * 18),
    ]
    _pack_ = 8


'''
######################################Bus system independent####################################
'''


class VBLDriverOverrun(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mBusType', c_uint32),
        ('mChannel', c_uint16),
        ('mDummy', c_uint16),
    ]
    _pack_ = 8


'''
######################################Event Comment####################################
'''


class VBLEventComment(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mCommentedEventType', c_uint32),
        ('mTextLength', c_uint32),
        ('mText', c_char_p),
    ]
    _pack_ = 8


'''
######################################Event Global Marker####################################
'''


class VBLGlobalMarker(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mCommentedEventType', c_uint32),
        ('mForegroundColor', c_uint32),
        ('mBackgroundColor', c_uint32),
        ('mIsRelocatable', c_uint8),
        ('mGroupNameLength', c_uint32),
        ('mMarkerNameLength', c_uint32),
        ('mDescriptionLength', c_uint32),
        ('mGroupName', c_char_p),
        ('mMarkerName', c_char_p),
        ('mDescription', c_char_p),
    ]
    _pack_ = 8


'''
######################################Test Structure Event####################################
'''


class VBLTestStructure(Structure):
    _fields_ = [
        ('mHeader', VBLObjectHeader),
        ('mExecutingObjectIdentity', c_uint32),
        ('mType', c_uint16),
        ('mUniqueNo', c_uint32),
        ('mAction', c_uint16),
        ('mResult', c_uint16),
        ('mExecutingObjectNameLength', c_uint32),
        ('mNameLength', c_uint32),
        ('mTextLength', c_uint32),
        ('mExecutingObjectName', c_wchar_p),
        ('mName', c_wchar_p),
        ('mText', c_wchar_p),
    ]
    _pack_ = 8



