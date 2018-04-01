#print("Executing main :{0}".format(__name__))
import sys
import reader

r= reader.Reader(sys.argv[1])
try:
    print(r.read())
finally:
    r.close()