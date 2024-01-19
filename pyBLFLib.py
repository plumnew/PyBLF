from pyBLFLib_Util import *


dll = "D:\\local3rd\\BLFLibs\\Win64\\binlog.dll"


class BLMessageLevel:
    eInfo = 0
    eWarning = 1
    eError = 2


class BLMessageType:
    eDefault = 0
    eSimple = 1
    eAskStop = 2
    eAskStopFurther = 3


class IBLCallback:
    _functions_ = [
        ("OutputMessage", CFUNCTYPE(c_void_p, c_int, c_int, c_char_p)),
    ]


class IBLCallback2(IBLCallback):
    _functions_ = [
        ("SignalEvent", CFUNCTYPE(c_void_p, c_void_p, c_int)),
    ]


class Blf_Handler(Structure):
    pass


class BlfApi:
    _lib_blf = None
    _hdl = POINTER(Blf_Handler)
    _hbase = VBLObjectHeaderBase()
    '''
    _BLCreateFile = WINFUNCTYPE(c_void_p, c_char_p, c_uint32)
    _BLCreateFileW = WINFUNCTYPE(c_void_p, c_wchar_p, c_uint32)
    _BLCreateFileEx = WINFUNCTYPE(c_void_p, c_char_p, c_uint32, c_char_p, c_char_p)
    _BLCreateFileExW = WINFUNCTYPE(c_void_p, c_wchar_p, c_uint32, c_wchar_p, c_wchar_p)
    _BLCreateFileEx2 = WINFUNCTYPE(c_void_p, c_char_p, c_uint32, c_char_p, c_char_p, POINTER(IBLCallback))
    _BLCreateFileEx2W = WINFUNCTYPE(c_void_p, c_wchar_p, c_uint32, c_wchar_p, c_wchar_p, POINTER(IBLCallback))
    _BLCreateFileEx3W = WINFUNCTYPE(c_void_p, c_wchar_p, c_uint32, c_wchar_p, c_void_p, c_wchar_p, POINTER(IBLCallback))
    _BLCloseHandle = WINFUNCTYPE(c_int, c_void_p)
    _BLWriteObject = WINFUNCTYPE(c_int, c_void_p, POINTER(VBLObjectHeaderBase))
    _BLPeekObject = WINFUNCTYPE(c_int, c_void_p, POINTER(VBLObjectHeaderBase))
    _BLSkipObject = WINFUNCTYPE(c_int, c_void_p, POINTER(VBLObjectHeaderBase))
    _BLReadObject = WINFUNCTYPE(c_int, c_void_p, POINTER(VBLObjectHeaderBase))
    _BLReadObjectSecure = WINFUNCTYPE(c_int, c_void_p, POINTER(VBLObjectHeaderBase), c_size_t)
    _BLFreeObject = WINFUNCTYPE(c_int, c_void_p, POINTER(VBLObjectHeaderBase))
    _BLSeekTime = WINFUNCTYPE(c_int, c_void_p, c_uint64, c_void_p, WINFUNCTYPE(c_int, c_void_p, c_float), c_uint16)
    _BLSetApplication = WINFUNCTYPE(c_int, c_void_p, c_uint8, c_uint8, c_uint8, c_uint8)
    _BLSetWriteOptions = WINFUNCTYPE(c_int, c_void_p, c_uint32, c_uint32)
    _BLSetMeasurementStartTime = WINFUNCTYPE(c_int, c_void_p, POINTER(SYSTEMTIME))
    _BLGetFileStatistics = WINFUNCTYPE(c_int, c_void_p, POINTER(VBLFileStatistics))
    _BLGetFileStatisticsEx = WINFUNCTYPE(c_int, c_void_p, POINTER(VBLFileStatisticsEx))
    _BLFlushFileBuffers = WINFUNCTYPE(c_int, c_void_p, c_uint32)
    _BLSetCommentAttributeString = WINFUNCTYPE(c_int, c_void_p, c_wchar_p, c_wchar_p)
    _BLGetNumCommentAttributes = WINFUNCTYPE(c_int, c_void_p, POINTER(c_uint32))
    _BLGetCommentAttributeName = WINFUNCTYPE(c_int, c_void_p, c_uint32, c_wchar_p, POINTER(c_uint32))
    _BLGetCommentAttributeString = WINFUNCTYPE(c_int, c_void_p, c_wchar_p, c_wchar_p, POINTER(c_uint32))
    _BLPeekTimestamp = WINFUNCTYPE(c_int, c_void_p, POINTER(VBLObjectHeaderBase), POINTER(c_uint64))
'''
    def __init__(self):

        self._lib_blf = windll.LoadLibrary(dll)
        print(">> API DLL path used: " + str(self._lib_blf._name))
        self._lib_blf.BLCreateFile.argtypes = [c_char_p, c_uint32]
        self._lib_blf.BLCreateFile.restype = c_void_p

        self._lib_blf.BLCreateFileW.argtypes = [c_wchar_p, c_uint32]
        self._lib_blf.BLCreateFileW.restype = c_void_p

        self._lib_blf.BLCreateFileEx.argtypes = [c_char_p, c_uint32, c_char_p, c_char_p]
        self._lib_blf.BLCreateFileEx.restype = c_void_p

        self._lib_blf.BLCreateFileExW.argtypes = [c_wchar_p, c_uint32, c_wchar_p, c_wchar_p]
        self._lib_blf.BLCreateFileExW.restype = c_void_p
        '''
        _lib_blf.BLCreateFileEx2.argtypes = [c_char_p, c_uint32, c_char_p, c_char_p, POINTER(IBLCallback)]
        _lib_blf.BLCreateFileEx2.restype = c_void_p

        _lib_blf.BLCreateFileEx2W.argtypes = [c_wchar_p, c_uint32, c_wchar_p, c_wchar_p, POINTER(IBLCallback)]
        _lib_blf.BLCreateFileEx2W.restype = c_void_p

        _lib_blf.BLCreateFileEx3W.argtypes = [c_wchar_p, c_uint32, c_wchar_p, c_void_p, c_wchar_p,
                                               POINTER(IBLCallback)]
        _lib_blf.BLCreateFileEx3W.restype = c_void_p
        '''
        self._lib_blf.BLCloseHandle.argtypes = [c_void_p]
        self._lib_blf.BLCloseHandle.restype = c_int

        self._lib_blf.BLWriteObject.argtypes = [c_void_p, POINTER(VBLObjectHeaderBase)]
        self._lib_blf.BLWriteObject.restype = c_int

        self._lib_blf.BLPeekObject.argtypes = [c_void_p, POINTER(VBLObjectHeaderBase)]
        self._lib_blf.BLPeekObject.restype = c_int

        self._lib_blf.BLSkipObject.argtypes = [c_void_p, POINTER(VBLObjectHeaderBase)]
        self._lib_blf.BLSkipObject.restype = c_int

        self._lib_blf.BLReadObject.argtypes = [c_void_p, POINTER(VBLObjectHeaderBase)]
        self._lib_blf.BLReadObject.restype = c_int

        self._lib_blf.BLReadObjectSecure.argtypes = [c_void_p, POINTER(VBLObjectHeaderBase), c_size_t]
        self._lib_blf.BLReadObjectSecure.restype = c_int

        self._lib_blf.BLFreeObject.argtypes = [c_void_p, POINTER(VBLObjectHeaderBase)]
        self._lib_blf.BLFreeObject.restype = c_int

        self._lib_blf.BLSeekTime.argtypes = [c_void_p, c_uint64, c_void_p, WINFUNCTYPE(c_int, c_void_p, c_float), c_uint16]
        self._lib_blf.BLSeekTime.restype = c_int

        self._lib_blf.BLSetApplication.argtypes = [c_void_p, c_uint8, c_uint8, c_uint8, c_uint8]
        self._lib_blf.BLSetApplication.restype = c_int

        self._lib_blf.BLSetWriteOptions.argtypes = [c_void_p, c_uint32, c_uint32]
        self._lib_blf.BLSetWriteOptions.restype = c_int

        self._lib_blf.BLSetMeasurementStartTime.argtypes = [c_void_p, POINTER(SYSTEMTIME)]
        self._lib_blf.BLSetMeasurementStartTime.restype = c_int

        self._lib_blf.BLGetFileStatistics.argtypes = [c_void_p, POINTER(VBLFileStatistics)]
        self._lib_blf.BLGetFileStatistics.restype = c_int

        self._lib_blf.BLGetFileStatisticsEx.argtypes = [c_void_p, POINTER(VBLFileStatisticsEx)]
        self._lib_blf.BLGetFileStatisticsEx.restype = c_int

        self._lib_blf.BLFlushFileBuffers.argtypes = [c_void_p, c_uint32]
        self._lib_blf.BLFlushFileBuffers.restype = c_int

        self._lib_blf.BLSetCommentAttributeString.argtypes = [c_void_p, c_wchar_p, c_wchar_p]
        self._lib_blf.BLSetCommentAttributeString.restype = c_int

        self._lib_blf.BLGetNumCommentAttributes.argtypes = [c_void_p, POINTER(c_uint32)]
        self._lib_blf.BLGetNumCommentAttributes.restype = c_int

        self._lib_blf.BLGetCommentAttributeName.argtypes = [c_void_p, c_uint32, c_wchar_p, POINTER(c_uint32)]
        self._lib_blf.BLGetCommentAttributeName.restype = c_int

        self._lib_blf.BLGetCommentAttributeString.argtypes = [c_void_p, c_wchar_p, c_wchar_p, POINTER(c_uint32)]
        self._lib_blf.BLGetCommentAttributeString.restype = c_int

        self._lib_blf.BLPeekTimestamp.argtypes = [c_void_p, POINTER(VBLObjectHeaderBase), POINTER(c_uint64)]
        self._lib_blf.BLPeekTimestamp.restype = c_int

    def BLCreateFile(self, file_name: str, desired_access: DesiredAccess):
        self._hdl = self._lib_blf.BLCreateFile(file_name.encode('utf-8'), desired_access)
        if BLINVALID_HANDLE_VALUE == self._hdl:
            raise ValueError("handle on specified file on failed")
        return True

    def BLPeekObject(self, base: VBLObjectHeaderBase):
        if self._lib_blf.BLPeekObject(self._hdl, base) == 0:
            return None
        return self._hbase

    def BLSkipObject(self, base: VBLObjectHeaderBase):
        if self._lib_blf.BLSkipObject(self._hdl, base) == 0:
            return None
        return self._hbase

    def BLReadObjectSecure(self, base: VBLObjectHeaderBase, expected_size: int):
        return self._lib_blf.BLReadObjectSecure(self._hdl, base, expected_size) != 0

    def BLFreeObject(self, base: VBLObjectHeaderBase):
        return self._lib_blf.BLFreeObject(self._hdl, base) != 0

    def BLCloseHandle(self):
        if self._lib_blf.BLCloseHandle(self._hdl) == 0:
            raise ValueError("close handle failed")
        return True

    def __del__(self):
        pass


class BlfObjectWrapper:
    _type = None
    _size = None
    obj = None

    def __init__(self, obj_type: BL_OBJ_TYPE, size: int, blf_obj: Structure):
        self._type = obj_type
        self._size = size
        self.obj = blf_obj
        if hasattr(self.obj, 'mHeader') is False:
            raise ValueError("blf_obj define is incorrect")

    def get_type(self):
        return self._type

    def fill_data(self, base: VBLObjectHeaderBase, api: BlfApi):
        self.obj.mHeader.mBase = base
        return api.BLReadObjectSecure(self.obj.mHeader.mBase, self._size)

    def filter(self):
        pass

    def free(self, api: BlfApi):
        if self.obj.mHeader.mBase is not None:
            api.BLFreeObject(self.obj.mHeader.mBase)


class BlfReader:
    BlfApi = None
    _base = VBLObjectHeaderBase()
    _obj_list = {}

    def __init__(self):
        self.BlfApi = BlfApi()

    def open(self, blf_file: str):
        return self.BlfApi.BLCreateFile(blf_file, DesiredAccess.GENERIC_READ)

    def enroll(self, blf_obj: BlfObjectWrapper):
        self._obj_list[blf_obj.get_type()] = blf_obj

    def read_data(self):
        while self.BlfApi.BLPeekObject(self._base):
            if self._base.mObjectType.value in self._obj_list.keys():
                self._obj_list[self._base.mObjectType.value].free(self.BlfApi)
                if self._obj_list[self._base.mObjectType.value].fill_data(self._base, self.BlfApi):
                    if self._obj_list[self._base.mObjectType.value].filter():
                        return self._obj_list[self._base.mObjectType.value]
                    continue
                else:
                    raise ValueError("close handle failed")
            else:
                self.BlfApi.BLSkipObject(self._base)
        return None

    def close(self):
        pass

