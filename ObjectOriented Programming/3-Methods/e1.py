class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.position = None
        self.area = None
     
    def change_position (self, x, y):
        self.x = x
        self.y = y

    def get_position (self):
        return self.x, self.y
     
    
    def get_area (self):
        self.area = self.width * self.height
        return self.area
