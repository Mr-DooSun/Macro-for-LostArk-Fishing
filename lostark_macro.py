import numpy as np
from PIL import ImageGrab
import cv2
from time import sleep
import pynput
import threading

n_time = 0

def Time():
    while True:
        global n_time
        n_time += 1
        print(n_time)
        sleep(1)

def Thread():
    thread=threading.Thread(target=Time,)
    thread.daemon=True 
    thread.start()

if __name__=="__main__":

    Thread()

    keyboard_button = pynput.keyboard.Controller()
    keyboard_key=pynput.keyboard.Key

    while True:
        printscreen_pil =  ImageGrab.grab(bbox=(630,320,655,370))
        # printscreen_pil =  ImageGrab.grab(bbox=(430,320,655,370))
        printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8').reshape((printscreen_pil.size[1],printscreen_pil.size[0],3)) 

        img=cv2.cvtColor(printscreen_numpy,cv2.COLOR_BGR2RGB)
        
        lower_color=(110, 210, 210)
        upper_color=(170,255, 255)

        img_mask = cv2.inRange(img, lower_color, upper_color)
        
        num = 0

        if n_time > 35 :
            keyboard_button.press('w')
            keyboard_button.release('w')
            n_time = 0

        for y in range(0,50) :
            if num > 50:
                n_time = 0

                print("detecting")

                keyboard_button.press('w')
                keyboard_button.release('w')

                sleep(8)

                keyboard_button.press('w')
                keyboard_button.release('w')

                sleep(2)
                n_time = 0

                break

            for x in range(0,20) :
                if num > 50 :
                    break
                if img_mask[y,x] == 255 :
                    num+=1
        print("pixel : %d"%num)

        cv2.imshow('window',img)
        cv2.imshow("mask",img_mask)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break