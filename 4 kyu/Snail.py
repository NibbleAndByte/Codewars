import math
def snail(array):
    if array == [[]]:
        return []
    
    retArr = []
    side = len(array)
    total = side * side
    currX = 0
    currY = 0
    print('{} is total. {} is side. {}, {} is currX, currY'.format(total, side, currX, currY))
    
    
    while (len(retArr) < total):
        # TODO: Fix currx/y
        #heading Right
        for i in range(currX, side):
            print ("hit")
            currX += 1
            retArr.append(1)
        
        print('RIGHT: {}, {} is currX, currY'.format(currX, currY))
        
        side -= .5
        #heading Down
        for i in range(currY, math.floor(side)):
            print ("hit")
            currY += 1
            retArr.append(array[currX][currY])
        
        print('Down: {}, {} is currX, currY'.format(currX, currY))
        
        side -= .5
        #heading Left
        for i in range(math.floor(currX - side), currX):
            print ("hit")
            currX -= 1
            retArr.append(1)
        print('LEFT: {}, {} is currX, currY'.format(currX, currY))
        
        side -= .5
        #heading Up
        for i in range(math.floor(currY - side), currY):
            print ("hit")
            currY -= 1
            retArr.append(1)
            
        print('UP: {}, {} is currX, currY'.format(currX, currY))
    
    return retArr;
    