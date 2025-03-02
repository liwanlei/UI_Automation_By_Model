from paddleocr import PaddleOCR

from common.Coordinate import CoordinateTool
from common.Data import Stack, Item


class PaddleOCR_Result(object):
    def __init__(self, imgpath):
        self.imgpath = imgpath
        self.reslutnode = Stack()
    def get_result(self):
        ocr = PaddleOCR(use_angle_cls=True, lang='ch')
        result = ocr.ocr(self.imgpath, cls=True)
        return result
    def reslut(self):
        result = self.get_result()
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                item = Item(CoordinateTool(line[0]).get_coordinate(), line[1][0])
                self.reslutnode.push(item)
        return self.reslutnode

if __name__=="__main__":
    print(PaddleOCR_Result("/Users/lileilei/Desktop/AimodelAutoTest/11.png").get_result())