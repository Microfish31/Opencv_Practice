import cv2
import numpy as np
import pyautogui
import time
import threading

def screenShot():
    img = pyautogui.screenshot(region=[100,200, 1600, 1000])
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    return img

class Car:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        self.slope = -1
        self.control = False

    def press(self,key):
        pyautogui.keyDown(key)
        time.sleep(0.005)        
        pyautogui.keyUp(key)

    def press2(self,key1,key2):
        pyautogui.keyDown(key1)
        pyautogui.keyDown(key2)
        time.sleep(0.005)        
        pyautogui.keyUp(key1)
        pyautogui.keyUp(key2)

    def drive_up(self):
        return threading.Thread(target=self.press, name="up", args='w')
    def drive_down(self):
        self.press('s')
    def drive_left(self):
        return threading.Thread(target=self.press, name="left", args='a') 
    def drive_right(self):
        return threading.Thread(target=self.press, name="right", args='d') 
    def drive(self,key1,key2):
        return threading.Thread(target=self.press2, name="drive", args=[key1,key2])
    def drive_brake(self):
        self.press('space')
    def drive_accerate(self):
        self.press('n')

def drawCntMax(img,cntMax):
    rect = cv2.minAreaRect(cntMax)
    box = np.int64(cv2.boxPoints(rect))
    return int(rect[0][0]),int(rect[0][1]),box,rect[2]

def findMaxgrayContour(gray) :
    blur = cv2.GaussianBlur(gray,(5,5),0)
    thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnt_max = max(contours,key=cv2.contourArea)
    return cnt_max

def findColor(img,L,U):
    return cv2.inRange(img,np.array(L),np.array(U))

def findObjPos(img,L,U):
    mask = findColor(img,np.array(L),np.array(U))
    max_cnt = findMaxgrayContour(mask)
    x,y,box,theta = drawCntMax(img,max_cnt)
    return x,y,box,theta

def cleanObs(img):
    eroded = cv2.erode(img,np.ones((3,3),np.uint8),iterations=1)
    dilated = cv2.dilate(eroded,np.ones((9,9),np.uint8),iterations=2)
    return dilated

def findSlope(p1,p2):
    return (p2[1]-p1[1])/(p2[0]-p1[0])

def makeMask(w,h):
    stencil = np.zeros((w, h, 3), np.uint8)
    polygon = np.array([[450,1080], [450,300], [1000,300], [1000,1080]])
    cv2.fillConvexPoly(stencil, polygon, (255,255,255))
    return stencil

def DisP2C(xp,yp,x1,y1,x2,y2):
    if x1==x2:   # Vertical Line
        D=abs(xp-x1)
    elif y1==y2: # Horizontal Line
        D=abs(yp-y1)
    else:
        m=(y1-y2)/(x1-x2)
        D=(float)(abs(m*(xp-x1)+(y1-yp)))/(float)(np.sqrt(m**2+1))
        return D

def disP2P(p1,p2):
    return int(np.sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 ))

def putext(img,text,x,y):
    cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)

def drawMidLine(frame,mll,mrl):
    cv2.line(frame,(mll[0][0],mll[0][1]),(mll[0][2],mll[0][3]),(0,0,0,),5)
    cv2.line(frame,(mrl[0][0],mrl[0][1]),(mrl[0][2],mrl[0][3]),(255,0,0,),5)
    cv2.circle(frame,(mll[0][0],mll[0][1]),5,(0,0,0),-1)
    cv2.circle(frame,(mll[0][2],mll[0][3]),5,(0,0,0),-1)
    cv2.circle(frame,(mrl[0][0],mrl[0][1]),5,(255,0,0),-1)
    cv2.circle(frame,(mrl[0][2],mrl[0][3]),5,(255,0,0),-1)

def Karamaformula(m1,P1,m2,P2):
    #m2=-1/m1
    a1=m1;b1=-1;c1=m1*P1[0]-P1[1]
    a2=m2;b2=-1;c2=m2*P2[0]-P2[1]
    delta=a1*b2-b1*a2
    deltax=c1*b2-b1*c2
    deltay=a1*c2-c1*a2
    x=deltax/delta
    y=deltay/delta
    return x,y

# Screenshot
frame = screenShot()
#.........................................

w,h,c = frame.shape
car = Car(-1,-1)
road_r = 550

# stencil =  makeMask(w,h)

# Screenshot
time.sleep(3)
#.........................................

# Screenshot
while 1:
#.........................................

    # ScreenShot
    frame = screenShot()
    #...................................

    # Find Car Position (problem)
        # testing
        # mask0 = cv2.bitwise_and(frame,stencil)
        # car.X,car.Y,rect_ps,theta = findObjPos(mask0,[47,44,39],[120,114,107])
        # car.X,car.Y,rect_ps,theta = findObjPos(mask0,[0,100,90],[10,200,230])

    car.X,car.Y,rect_ps,theta = findObjPos(frame,[0,100,90],[10,200,230])

    # Write horizontal Line
    if theta < 45 :
       rr_x,rr_y = car.X + road_r , int(car.Y + road_r * findSlope((rect_ps[1][0],rect_ps[1][1]),(rect_ps[2][0],rect_ps[2][1])))
       ll_x,ll_y = car.X - road_r , int(car.Y - road_r * findSlope((rect_ps[1][0],rect_ps[1][1]),(rect_ps[2][0],rect_ps[2][1])))
       xtc,ytc = int((rect_ps[1][0]+rect_ps[2][0])/2),int( (rect_ps[1][1]+rect_ps[2][1])/2)
    else:
       rr_x,rr_y = car.X + road_r , int(car.Y + road_r * findSlope((rect_ps[0][0],rect_ps[0][1]),(rect_ps[1][0],rect_ps[1][1])))
       ll_x,ll_y = car.X - road_r , int(car.Y - road_r * findSlope((rect_ps[0][0],rect_ps[0][1]),(rect_ps[1][0],rect_ps[1][1])))
       xtc,ytc = int((rect_ps[0][0]+rect_ps[1][0])/2),int( (rect_ps[0][1]+rect_ps[1][1])/2)                                    

    # Find the road lines beside the car.
    mask1 = findColor(frame,[140,150,160],[215,200,215])
    mask1 = cleanObs(mask1)

    lines = cv2.HoughLinesP(mask1,1,np.pi/180,100,minLineLength=300,maxLineGap=15)

    RL=[]
    LL=[]

    if lines is not None:
        for line in lines :
            x1,y1,x2,y2 = line[0]
            if x2!=x1:
                m = (y2-y1)/(x2-x1)
                if m > 0.3:
                    RL.append((line[0],m))
                elif m < -0.3:
                    LL.append((line[0],m))

        ll_len = len(LL)
        rl_len = len(RL)
        L='left line='+str(ll_len)
        R='Right line='+str(rl_len)
        dll = -1
        drl = -1

        if ll_len and rl_len :
           car.slope = (ll_y-rr_y)/(ll_x-rr_x)
           points,slope = LL[0]
           xl,yl = Karamaformula(slope,(points[0],points[1]),car.slope,(car.X,car.Y))
           # dll = DisP2C(car.X,car.Y,points[0],points[1],points[2],points[3])
           dll = disP2P((car.X,car.Y),(xl,yl))
           cv2.line(frame,(points[0],points[1]),(points[2],points[3]),(0,0,0),5)

           points,slope = RL[0]
           xr,yr = Karamaformula(slope,(points[0],points[1]),car.slope,(car.X,car.Y))
           # drl = DisP2C(car.X,car.Y,points[0],points[1],points[2],points[3])
           drl = disP2P((car.X,car.Y),(xr,yr))
           cv2.line(frame,(points[0],points[1]),(points[2],points[3]),(255,0,0),5)

           xc,yc = int((xl + xr)/2),int((yl + yr)/2)
           DL = 'DL =' + str(dll)
           DR = 'DR =' + str(drl)           
           RTP=Karamaformula(car.slope,(rect_ps[1][0],rect_ps[1][1]),RL[0][1],(RL[0][0][0],RL[0][0][1]))
           LTP=Karamaformula(car.slope,(rect_ps[1][0],rect_ps[1][1]),LL[0][1],(LL[0][0][0],LL[0][0][1]))
           MTP=(int((RTP[0]+LTP[0])/2),int((RTP[1]+LTP[1])/2))           
           d = disP2P((car.X,car.Y),(xc,yc))
           dl2l = disP2P((xl,yl),(xr,yr))
           td = disP2P((MTP[0],MTP[1]),(xtc,ytc))
           
           if td >20:
               if xtc>MTP[0]:
                   t = car.drive_left()
                   t.start()
                   car.control = True
                   putext(frame,'td>20LL',100,300)
               else:
                   t = car.drive_right()
                   t.start()
                   car.control = True
                   putext(frame,'td>20RR',100,300)
           else:
               if d > 110 :
                   if (MTP[0]-xtc)>0 and (xc-car.X)<0: # car head | car center
                       t = car.drive('w','d')
                       t.start()
                       car.control = True
                       putext(frame,'d>110Case1',100,300)
                   elif (MTP[0]-xtc)<0 and (xc-car.X)>0: # car center | car head 
                       t = car.drive('w','a')
                       t.start()
                       car.control = True
                       putext(frame,'d>110Case2',100,300)
                   else :                                # No cross
                       t = car.drive_up()
                       t.start()
                       car.control = True
                       putext(frame,'d>110Case3',100,300)
               else :
                   if (xc-car.X)>0 and (MTP[0]-xtc)>0 and (MTP[0]-xtc)-(xc-car.X)>-5: # car head | car center
                       t = car.drive('w','d')
                       t.start()
                       car.control = True
                       putext(frame,'d<110caseL',100,300)
                   elif (car.X-xc )>0 and (xtc-MTP[0])>0 and (xtc-MTP[0])- (car.X-xc)>-5: # car center | car head 
                       t = car.drive('w','a')
                       t.start()
                       car.control = True
                       putext(frame,'d<110caseR',100,300)
                   else :
                        t = car.drive_up()
                        t.start()
                        car.control = True
                        putext(frame,'WW',100,300)
               
               
           putext(frame,'td='+str(td),500,300)
           putext(frame,DL,100,200)
           putext(frame,DR,500,200)
           putext(frame,"d=" + str(d),100,400)
           putext(frame,"dl2l=" + str(dl2l),100,500)
           cv2.circle(frame,(xc,yc),10,(255,0,0),-1)
           cv2.circle(frame,(MTP[0],MTP[1]),10,(0,0,0),-1) 
           cv2.line(frame,(MTP[0],MTP[1]),(xc,yc),(0,0,0),5)
           cv2.line(frame,(xtc,ytc),(car.X,car.Y),(0,0,255),5)

        putext(frame,L,100,100)
        putext(frame,R,500,100)

    putext(frame,'degree = ' + str(round(theta,2)),100,50)
    cv2.circle(frame,(xtc,ytc),10,(0,255,0),-1)
    cv2.circle(frame,(car.X,car.Y),10,(0,0,255),-1)
    cv2.line(frame,(ll_x,ll_y),(rr_x,rr_y),(0,255,0),2);
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xff == ord("q"):
       break

    if car.control:
       t.join()
       car.control = False

cv2.destroyAllWindows()
