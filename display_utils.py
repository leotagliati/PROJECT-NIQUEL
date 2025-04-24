def printIcon(display, icon, x0, y0):
    for y, row in enumerate(icon):
        for x, c in enumerate(row):
            if c == "0":
                display.pixel(x0 + x, y0 + y, 1)
                
def buildIcon(icon, orientation="horizontal"):
    rows = len(icon)
    columns = len(icon[0])
    icon_rotated = []

    for x in range(columns):
        newRow = ""
        for y in range(rows - 1, -1, -1):
            if orientation == "horizontal":
                newRow += icon[y][x]
            elif orientation == "vertical":
                newRow += icon[x][y] 
        icon_rotated.append(newRow)

    return icon_rotated