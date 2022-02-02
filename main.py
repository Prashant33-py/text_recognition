import pytesseract
from PIL import Image
import cv2
import pyttsx3
 
engine = pyttsx3.init()
img = cv2.imread('C:\\Users\\Prashant\\OneDrive\\Desktop\\sbi.jfif',cv2.IMREAD_COLOR) #Open the image from which charectors has to be recognized
# img = cv2.resize(img, (620,480) ) #resize the image if required 
 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey to reduce detials 
gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
 
original = pytesseract.image_to_string(gray, config='', lang="hin")
test = (pytesseract.image_to_data(gray, lang=None, config='', nice=0) ) #get confidence level if required
print(pytesseract.image_to_boxes(gray))
 
print (original)
engine.say(original)
engine.runAndWait()
 
required = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
Final = ''
 
for c in original:
    for ch in required:
        if c==ch:
            Final = Final + c 
            break
 
print (test)
 
for a in test:
    if a == "\n":
        print("found")
 