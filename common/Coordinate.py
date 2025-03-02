class CoordinateTool(object):
    def __init__(self, coordinate_list):
        self.coordinate_list = coordinate_list
        self.reslut = []
        self.left_coordinate = (0, 0)
        self.right_coordinate = (0, 0)

    def computation(self, coordinatelistone, coordinatelisttwo):
        x1, y1 = coordinatelistone
        x2, y2 = coordinatelisttwo
        x3 = int((x1 + x2) / 2)
        y3 = int((y1 + y2) / 2)
        return x3, y3

    def get_coordinate(self):
        return self.computation(self.left_coordinate, self.right_coordinate)
