wallSize = 1
pathSize = 25
elmSz = wallSize + pathSize

winRes = [720, 720]
size = [ int(winRes[0] / elmSz) * elmSz+wallSize, int(winRes[1] / elmSz) * elmSz+wallSize] # window size

# 0 = wall colour
# 1 = path colour
colours = [ [128, 0, 0], [0, 0, 0] ]
screen = None

lock = False