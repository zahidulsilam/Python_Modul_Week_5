

class Rectangle:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
    def area (self) :
        return f' {self.width * self.height}'
    def perimeter (self) : 
        return f' {(self.width + self.height)*2}'
    
my_rectangle = Rectangle(5, 7)

# Print the area and perimeter
print("area =",my_rectangle.area())
print('Perimeter =',my_rectangle.perimeter())
