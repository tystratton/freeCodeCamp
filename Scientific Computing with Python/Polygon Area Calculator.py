class Shape:
    pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return ((self.width * 2)) + ((self.height * 2))
    
    def get_diagonal(self):
        return ((self.width**2 + self.height**2) ** 0.5)


    def get_picture(self):
        height = self.height
        width = self.width
        heightCounter = 0
        widthCounter = 0
        picture = ""
        if height and width < 50:
            while height > heightCounter:
                while width > widthCounter:
                    picture+="*"
                    widthCounter+=1
                picture+="\n"
                widthCounter=0
                heightCounter+=1
            return picture
        else:
            picture = "Too big for picture."
            return picture

    def get_amount_inside(self, Shape):
        height = Shape.height
        width = Shape.width
        selfHeight = self.height
        selfWidth = self.width
        countHeight = 0
        countWidth = 0
        while height <= selfHeight:
            countHeight += 1
            selfHeight-=height
        while width <= selfWidth:
            countWidth += 1
            selfWidth-=width
        return (countHeight * countWidth)

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return f'Square(side={self.width})'
    
    def set_width(self, side):
        self.height = side
        self.width = side

    def set_height(self, side):
        self.height = side
        self.width = side

    def set_side(self, side):
        self.width = side
        self.height = side
    
    

def main():
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
main()