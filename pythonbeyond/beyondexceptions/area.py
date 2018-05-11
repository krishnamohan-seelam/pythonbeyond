import math
import sys
import io
'''
    TriangleError inherits Exception class to demonstrate how to create new exce
    ptions and implicit chaining of exceptions(__context__)
'''
class TriangleError(Exception):
    def __init__(self,text,sides):
        super().__init__(text)
        self._sides =tuple(sides)
    
    @property
    def sides(self):
        return self._sides
    
    def __str__(self):
        return "'{}' for sides {}".format(self.args[0],self._sides)

    def __repr(self):
        #return "TriangleError({!r},{!r})".format(self.args[0],self._sides)
        return "TriangleError({!r}, {!r}".format(self.args[0], self._sides)

def triangle_area(a,b,c):
    sides =sorted([a,b,c])
    if sides[2] > (sides[0] + sides[1]):
        raise TriangleError("Illegal triangle",sides)
    p= (a+b+c)/2
    a=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return a

if __name__ == '__main__':
    try:
        print(triangle_area(3,4,5))
        print(triangle_area(4,10,5))
    except TriangleError as te:
        print(te)
        try:
            print("{!r}".format(te), file=sys.stdin) 
        except io.UnsupportedOperation as iou:
            print(te)
            print(iou)
            print(iou.__context__ is te )
