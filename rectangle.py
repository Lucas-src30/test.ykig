class Rectangle():
    def __init__(self,length,width,color):
        self.__color=color
        self.__length = length
        self.__width = width
    def color(self):
        return (self.__color)
    def perimeter(self):
        result=(self.__length*2)+(self.__width*2)
        return result
    def area(self):
        result=(self.__length*self.__width)
        return result
rectangle1=Rectangle(6,7,"blue")
print(rectangle1.color())