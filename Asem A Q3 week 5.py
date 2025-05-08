class shap :
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int (height)

class regtangle (shap) :
    def calculate_area (self):
        return self.width * self.height 
    
class square (shap):
    def area_calculate (self):
        return self.width * self.height

regtangle = regtangle (7,5)
print(f'Rectangle width = {regtangle.width}\nRectangle heigh = {regtangle.height}\nRectangle area = {regtangle.calculate_area()} ')

square = square (5,5)
print(f'Square width = {regtangle.width}, Square height = {regtangle.height} , Regtangle area = {square.area_calculate()}')

