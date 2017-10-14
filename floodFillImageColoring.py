from PIL import Image, ImageFilter

def getNeighbours(i, j, n, m) :
    arr = []
    if i-1 >= 0 and j-1 >= 0 :
        arr.append((i-1, j-1))
    if i-1 >= 0 :
        arr.append((i-1, j))
    if i-1 >= 0 and j+1 < m :
        arr.append((i-1, j+1))
    if j+1 < m :
        arr.append((i, j+1))
    if i+1 < n and j+1 < m :
        arr.append((i+1, j+1))
    if i+1 < n :
        arr.append((i+1, j))
    if i+1 < n and j-1 >= 0 :
        arr.append((i+1, j-1))
    if j-1 >= 0 :
        arr.append((i, j-1))
    return arr


img = Image.open('elephant.jpg')
bitmap = img.load()


n = img.size[0]
m = img.size[1]

#fill state map
stateMap = []
for i in range(n):
    stateMap.append([False for j in range(m)])       

queue = [(0, 0)]

while queue:
    e = queue.pop(0)
    i = e[0]
    j = e[1]
    if not stateMap[i][j]:
        stateMap[i][j] = True
        color = int((bitmap[i, j][0] + bitmap[i, j][1] + bitmap[i, j][2])/3)
        if color > 100: # check the color of the pixel against athreshold
            bitmap[i, j] = (135, 206, 250) # fill light blue color
            neigh = getNeighbours(i, j, n, m)
            for ne in neigh:
                queue.append(ne) # add neighbour pixels to the queue

img.show()







    
