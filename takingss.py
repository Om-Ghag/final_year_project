import cv2
from imutils.video import VideoStream
#camera = cv2.VideoCapture(0)
#for i in range(10):
#   return_value, image = camera.read()
 #   cv2.imwrite('opencv'+str(i)+'.png', image)
#del(camera)
camera = VideoStream(src=0).start()

for i in range(10):
    image = camera.read()
    cv2.imwrite('opencv'+str(i)+'.png', image)
del(camera)

#count = 0
	#	if mask > withoutMask:
		#	label= "Mask"
#		else: 
	#		label = "No Mask"
	#		camera = cv2.VideoCapture(0)
	#		return_value, image = camera.read()
	#		cv2.imwrite('opencv'+str(count)+'.png', image)
			#count = count + 1