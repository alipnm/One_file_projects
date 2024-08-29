from math import sqrt
scndrt = lambda number : sqrt(number)
area = lambda length, width : length * width
perimeter = lambda length, width : (length * 2) + (width * 2)
volume = lambda length, width, height : length * width * height
surface_area = lambda length, width, height : (length * width * 2) + (length * height * 2) + (width * height * 2)