
# all the distance 1 offsets around a hexagon
# in clockwise order starting from the top
offsets = ((0,-1), (1,-1), (1,0), (0,1), (-1,1), (-1,0))

def add(hex1,hex2):
    return (hex1[0]+hex2[0], hex1[1]+hex2[1])

def sub(hex1,hex2):
    return (hex1[0]-hex2[0], hex1[1]-hex2[1])

# rotate left is anti-clockwise, right is clockwise

left_rotations  = {offsets[i]:offsets[(i-1)%6] for i in xrange(6)}
right_rotations = {offsets[i]:offsets[(i+1)%6] for i in xrange(6)}
opposites       = {offsets[i]:offsets[(i+3)%6] for i in xrange(6)}

def rotate(offset,dir):
    if dir == 'left':
        return left_rotations[offset]
    elif dir == 'right':
        return right_rotations[offset]
    else:
        raise ValueError

def opposite(offset):
    return opposites[offset]    

def neighbours(hex):
    return set((hex[0]+offset[0], hex[1]+offset[1]) for offset in offsets)