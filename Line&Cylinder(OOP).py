import math

class Line():
    
    def __init__(self,coor1,coor2):
        
        self.coor1 = coor1
        self.coor2 = coor2
        
    def slope(self):
        
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        return (y2-y1)/(x2-x1)
    
    def distance(self):
        return math.sqrt((self.coor1[0]-self.coor2[0])**2 + (self.coor1[1] - self.coor2[1])**2)
    
class Cylinder():
    
    def __init__(self, height =1, radius = 1):
        
        self.height = height
        self.radius = radius
        
    def volume(self):
        
        print(3.14 * self.radius**2 *self.height)
    
    def surface_area(self):
        
        print(self.radius*2*3.14*self.height + 2*3.14*(self.radius)**2)
    
c = Cylinder(8,12)
c.surface_area()
c.volume()
    
c1 = (3,2)
c2 = (8,10)
myline = Line(c1,c2)
print(myline.distance())
print('\n')
print(myline.slope())