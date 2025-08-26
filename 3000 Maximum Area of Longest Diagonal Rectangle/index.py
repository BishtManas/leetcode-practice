def area_of_max_diagonal(dimensions):
    max_diagonal = 0
    max_area = 0

    for length, width in dimensions:
        diagonal = (length ** 2 + width ** 2) ** 0.5
        area = length * width

        if diagonal > max_diagonal:
            max_diagonal = diagonal
            max_area = area
        elif diagonal == max_diagonal and area > max_area:
            max_area = area

    return max_area

dimensions = [[9, 3], [8, 6]]
print(area_of_max_diagonal(dimensions))  

dimensions = [[3, 4], [4, 3]]
print(area_of_max_diagonal(dimensions)) 
