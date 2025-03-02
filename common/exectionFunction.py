from common.ImagePase import PaddleOCR_Result
from common.center import centercontrol
import os

import uuid

from config import openswapnum


class Exection(object):
    def __init__(self,device):
        self.device=device
        self.base=os.path.join(os.path.join(os.getcwd(),'images'),self.device)
        if os.path.exists(self.base) is False:
            os.makedirs(self.base)

    def open(self,appname):
        '''
        启动应用
        :param appname: 应用的名称
        :return:
        '''

        for _ in range(openswapnum):
            imagesname = uuid.uuid4()
            path = os.path.join(self.base, str(imagesname) + '.png')
            centercontrol(self.device, "screen_pull", path=path)
            postion = PaddleOCR_Result(path).reslut()
            reslut = postion.contains(appname)
            if reslut:
                centercontrol(self.device, "tap", postion=reslut.box)
                break
    def tap(self,text):
        imagesname = uuid.uuid4()
        path = os.path.join(self.base, str(imagesname) + '.png')
        centercontrol(self.device, "screen_pull", path=path)
        postion = PaddleOCR_Result(path).reslut()
        reslut = postion.contains(text)
        if reslut:
            centercontrol(self.device, "tap", postion=reslut.box)
            return True
        else:
            return False

    def input(self,content):
        centercontrol(self.device, "input", text=content)
        return True

    def asserttext(self,text):
        imagesname = uuid.uuid4()
        path = os.path.join(self.base, str(imagesname) + '.png')
        centercontrol(self.device, "screen_pull", path=path)
        postion = PaddleOCR_Result(path).reslut()
        reslut = postion.contains(text)
        if reslut:
            return  True
        return False