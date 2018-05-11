
def median(items):
    if not items:
        raise ValueError("median() arg is an empty sequence")
    items  = sorted(items)
    median_index = (len(items)-1) // 2
    if (len(items) %2 )!= 0 :
        return items(median_index)
    
    return  (items[median_index] + items[median_index+2])/2.0

if __name__ == '__main__':
    try:
        print(median([1,2,3,4,5,6,7,8,9,10]))
        print(median([]))
    except ValueError as ve:
        print("payload :{0}".format(ve.args))
    