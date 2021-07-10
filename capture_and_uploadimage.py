import cv2
import dropbox
import time
import random



def take_snapshot():
    number= random.randint(0,100)
    videoCaptureObject= cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame= videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        #print("start time inside snapshot",start_time)
        result=False
    return img_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token='6weROgX68DcAAAAAAAAAAUYDuxovohQ7tAQkVczoPxbfavbW5zHTkP05SMl1Vp6H'
    file_from= img_name
    file_to= "/PicFolder/"+img_name
    dbx=dropbox.Dropbox(access_token)

    f= open(file_from,'rb')
    dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
    print("File uploaded")

def main():
    start_time=time.time()
    print("Initial start time",start_time)
    while(True):
        if((time.time()-start_time)>=500):
            #print(" start time before calling snapshot",start_time)
            #print((time.time()-start_time))
            name=take_snapshot()
            start_time=time.time()
            #print(" start time after calling snapshot",start_time)
            upload_file(name)

main()
