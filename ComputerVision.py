import cv2
import os

# ***CHANGE THE BELOW LINE OF CODE TO YOUR FOLDER PATH***
save_folder=r"C:\Users\YOUR_NAME\Pictures\CapturedImages"

#Create folder if it doesnt exist
os.makedirs(save_folder, exist_ok=True)

#Open webcam
cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Couldn't open camera.")
    exit()

print("======================================")
print("Controls:")
print("SPACE -> Capture and save image")
print("Q -> Quit")
print("======================================")

image_count=1

while True:
    ret,frame=cap.read()

    if not ret:
        print("Failed to grab frame.")
        break

    #To show live camera feed
    cv2.imshow("Camera",frame)
    key=cv2.waitKey(1) & 0xFF

    #SPACEBAR -> Save Image
    if key==ord(' '):
        filename=os.path.join(save_folder, f"image_{image_count:03d}.jpg")
        cv2.imwrite(filename,frame)
        print(f"Saved:{filename}")
        image_count+=1

    #Q - Quit
    elif key == ord('q'):
        print("Closing camera...")
        break

#Release resources
cap.release()
cv2.destroyAllWindows()

        
