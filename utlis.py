## SENDING COMMANDS BASED ON FINGERS
if (myCounter==4): sendData([1,1,1,1,1]);FingerCount="Five"
elif (myCounter == 3): sendData([1, 1, 1, 1, 0]);FingerCount="Four"
elif (myCounter == 2):sendData([0, 1, 1, 1, 0]);FingerCount="Three"
elif (myCounter == 1):sendData([0, 0, 1, 1, 0]);FingerCount="Two"
elif (myCounter == 0):
    aspectRatio = w/h
    if aspectRatio < 0.6:
        sendData([0, 0, 0, 1, 0]);FingerCount="One"
    else: sendData([0, 0, 0, 0, 0]);FingerCount="Zero"
        cv2.putText(imgMatch,FingerCount,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
return imgCon,imgMatch

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver