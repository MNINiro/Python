class Circle(object):

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

##    def draw(self, canvas):
##        rad = self.radius
##        x1 = self.center[0]-rad
##        y1 = self.center[1]-rad
##        x2 = self.center[0]+rad
##        y2 = self.center[1]+rad
##        canvas.create_oval(x1, y1, x2, y2, fill='green')
##
##    def move(self, x, y):
##        self.center = [x, y]


myCircle = Circle([10,30], 20) # Never pass “self”, it’s automatic

myOtherCircle = Circle([4,60], 10)

#myCircle.draw(canvas)
#myCircle.move(x,y)

print("CENTER :"+str(myCircle.center))
print("Radius :"+str(myCircle.radius))
      
