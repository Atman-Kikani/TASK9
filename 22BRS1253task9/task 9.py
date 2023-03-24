import cv2
yo = cv2.VideoCapture("notarickroll.mp4")
count_dracula=1
fpsnew=int((yo.get(cv2.CAP_PROP_FPS)/4))
while True:
    grabbed, frame = yo.read()
    if count_dracula%5==0:
        cv2.imshow('Frame',frame)
        cv2.waitKey(int(1000/fpsnew))#preserves original fps
    count_dracula+=1   
yo.release()