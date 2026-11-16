from Graphics.RectFunction import*
from Graphics.CirFunction import*
from Graphics.DGraphics.SphereFunction import*
from Graphics.DGraphics.CuboidFunction import*

l=int(input("enter length:"))
b=int(input("enter breadth:"))
print("rectangle area=",RectArea(l,b))
print("rectangle perimeter=",RectPerimeter(l,b))

r=int(input("enter radius:"))
print("Circle area=",CirArea(r))
print("Circle perimeter=",CirPerimeter(r))

r=int(input("enter radius of sphere:"))
print("sphere area=",SpArea(r))
print("sphere volume=",SpPerimeter(r))

l=int(input("enter cuboid length:"))
b=int(input("enter cuboid breadth:"))
h=int(input("enter cuboid height:"))
print("cuboid area=",CubArea(l,b,h))
print("cuboid perimeter=",CubPerimeter(l,b,h))

