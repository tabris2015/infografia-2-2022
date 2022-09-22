def get_line_small(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    xk = x0
    yk = y0
    y_inc = 1
    if dy < 1:
        y_inc = -1
        dy = -1 * dy
    Pk = 2 * dy - dx
    while xk <= x1:
        points.append((xk, yk))
        xk += 1
        if Pk < 0:
            Pk = Pk + 2 * dy
        else:
            Pk = Pk + 2 * dy - 2 * dx
            yk += y_inc
    return points

def get_line_big(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    xk = x0
    yk = y0
    x_inc = 1
    if dx < 1:
        x_inc = -1
        dx = -1 * dx
    Pk = 2 * dx - dy
    while yk <= y1:
        points.append((xk, yk))
        yk += 1
        if Pk < 0:
            Pk = Pk + 2 * dx
        else:
            Pk = Pk + 2 * dx - 2 * dy
            xk += x_inc
    return points

def get_line(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dy) > abs(dx):
        # pendiente > 1
        return get_line_big(x0, y0, x1, y1)
    else:
        return get_line_small(x0, y0, x1, y1)
        
if __name__ == "__main__":
    print(get_line(0, 0, 7, 2))