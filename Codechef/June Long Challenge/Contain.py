class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def subtract(self, p):
    	return Point(self.x - p.x, self.y - p.y)

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

def cross_product(p1, p2):
	return p1.x * p2.y - p2.x * p1.y

def direction(p1, p2, p3):
	return  cross_product(p3.subtract(p1), p2.subtract(p1))

def left(p1, p2, p3):
	return direction(p1, p2, p3) < 0

def right(p1, p2, p3):
	return direction(p1, p2, p3) > 0

def collinear(p1, p2, p3):
	return direction(p1, p2, p3) == 0

def find_min_y(points):
    miny = 999999
    mini = 0
    for i, point in enumerate(points):
        if point.y < miny:
            miny = point.y
            mini = i
        if point.y == miny:
            if point.x < points[mini].x:
                mini = i
    return points[mini], mini

def polar_comparator(p1, p2, p0):
    d = direction(p0, p1, p2)
    if d < 0:
        return -1
    if d > 0:
        return 1
    if d == 0:
        if distance_sq(p1, p0) < distance_sq(p2, p0):
            return -1
        else:
            return 1

def graham_scan(points):
    p0, index = find_min_y(points)

    points[0], points[index] = points[index], points[0]

    sorted_polar = sorted(points[1:], cmp = lambda p1, p2: polar_comparator(p1, p2, p0))
    
    to_remove = []
    for i in range(len(sorted_polar) - 1):
        d = direction(sorted_polar[i], sorted_polar[i + 1], p0)
        if d == 0:
            to_remove.append(i)
    sorted_polar = [i for j, i in enumerate(sorted_polar) if j not in to_remove]

   
    m = len(sorted_polar)
    if m < 2:
        print 'Convex hull is empty'

    else:
        stack = []
        stack_size = 0
        stack.append(points[0])
        stack.append(sorted_polar[0])
        stack.append(sorted_polar[1])
        stack_size = 3

        for i in range(2, m):
            while (True):
                d = direction(stack[stack_size - 2], stack[stack_size - 1], sorted_polar[i])
                if d < 0: 
                    break
                else: 
                    stack.pop()
                    stack_size -= 1
            stack.append(sorted_polar[i])
            stack_size += 1
    return stack