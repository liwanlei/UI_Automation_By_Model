from common.System.Android import AndroidTool
from config import testphonetype

'''
1.调用中枢，通过这里调用不同的控制方法
'''
def centercontrol(devices, command, *args, **kwargs):
    system = {
        "Android": AndroidTool
    }
    method = getattr(system[testphonetype](devices), command)
    if callable(method):
        return method(*args, **kwargs)
