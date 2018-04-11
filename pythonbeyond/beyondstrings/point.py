'''
Point2D class 
To demonstrate overriding __str__ and __repr__
'''

class Point2D:
    def __init__(self,x,y):
        self.x =x
        self.y =y
    
    def __str__(self):
        return  '({0},{1})'.format(self.x,self.y)
    
    def __repr__(self):
        return "Point2D(x={0},y={1})".format(self.x,self.y)
    
    def __format__(self,f):
        if f == 'r':
            return repr(self)
        else:
            return str(self)

if __name__ == '__main__':
    p = Point2D(10,20)
    print("{0:r}".format(p))
    print("{0}".format(p))
    print("{!r}".format(p)) 