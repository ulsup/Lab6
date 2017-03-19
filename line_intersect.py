def line_intersection(coordinates_1, coordinates_2):
    '''
    Checks if lines intersect. If no, returns none, if match - coordinates of the first line.
    '''
    A = coordinates_1[0]
    B = coordinates_1[1]
    C = coordinates_2[0]
    D = coordinates_2[1]
    koef_1 = (B[1] - A[1]) / (B[0] - A[0])
    koef_2 = (D[1] - C[1]) / (D[0] - C[0])
    b_1 = A[1] - (A[0] * koef_1)
    b_2 = C[1] - (C[0] * koef_2)
    if koef_1 == koef_2 and b_1 == b_2:
        return coordinates_1
    c_x = (A[0] - B[0], C[0] - D[0])
    c_y = (A[1] - B[1], C[1] - D[1])
    div = c_x[0] * c_y[1] - c_x[1] * c_y[0]
    if div == 0:
        return None
    d = (A[0] * B[1] - A[1] * B[0], C[0] * D[1] - C[1] * D[0])
    x = (d[0] * c_x[1] - d[1] * c_x[0]) / div
    y = (d[0] * c_y[1] - d[1] * c_y[0]) / div
    return x // 1, y // 1


'''if __name__ == '__main__':
    print(line_intersection([(4, 2), (2, 0)], [(0, 4), (4, 0)]))'''
