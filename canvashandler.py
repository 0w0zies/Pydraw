canvases = []
def createcanvas(sizex,sizey,color):
    import numpy as np
    img = np.zeros([sizey,sizex,3],dtype=np.uint8)
    img.fill(255)
    img = np.ndarray.tolist(img)
    print(img)
    canvases.append([sizex,sizey,img,False,0,0,"",[],-1])
    return len(canvases)