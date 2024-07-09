def calculate_area(width, height):
    return width * height

def process_data(data):
    result = []
    for item in data:
        if item % 2 == 0:
            result.append(item)
    return result

class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def sum_coordinates(self):
        return self.x_coordinate + self.y_coordinate
