import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Controller, Key

video = cv2.VideoCapture(2)

cv2.namedWindow("Tekken Player 1", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Tekken Player 1", cv2.WND_PROP_TOPMOST, 1)

detector = HandDetector(detectionCon=0.7, maxHands=2)
keyboard = Controller()

while True:
    _, img = video.read()
    # img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands:
        for hand in hands:
            finger = detector.fingersUp(hand)
            if hand["type"] == "Right":
                if finger == [1,1,1,1,1]:
                    print("Dodge")
                    cv2.putText(img, "Dodge", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press(Key.up)
                    keyboard.release(Key.down)
                    keyboard.release(Key.right)
                    keyboard.release(Key.left)
                    keyboard.release('u')
                    keyboard.release('i')

                if finger == [0,0,0,0,1]:
                    print("Right")
                    cv2.putText(img, "Right", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press(Key.right)
                    keyboard.release(Key.down)
                    keyboard.release(Key.up)
                    keyboard.release(Key.left)
                    keyboard.release('u')
                    keyboard.release('i')

                if finger == [1, 0, 0, 0, 0]:
                    print("left")
                    cv2.putText(img, "Left", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press(Key.left)
                    keyboard.release(Key.down)
                    keyboard.release(Key.right)
                    keyboard.release(Key.up)
                    keyboard.release('u')
                    keyboard.release('i')

                if finger == [0,0,0,0,0]:
                    print("Down")
                    cv2.putText(img, "Down", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press(Key.down)
                    keyboard.release(Key.up)
                    keyboard.release(Key.right)
                    keyboard.release(Key.left)
                    keyboard.release('u')
                    keyboard.release('i')
                    
                # if finger == [0, 1, 1, 1, 1]:
                #     print("left puch")
                #     cv2.putText(img, "left punch", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                #     keyboard.press('u')
                #     keyboard.release(Key.up)
                #     keyboard.release(Key.right)
                #     keyboard.release(Key.left)
                #     keyboard.release(Key.down)
                #     keyboard.release('i')

                # if finger == [1, 1, 1, 1, 1]:
                #     print("Swap 1")
                #     cv2.putText(img, "Swap 1", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                #     keyboard.press('k')
                #     keyboard.release('b')
                #     keyboard.release(Key.up)
                #     keyboard.release(Key.right)
                #     keyboard.release(Key.left)
                #     keyboard.release(Key.down)
                    
                # if finger == [0,0,0,0,0]:
                #     print("Swap 3")
                #     cv2.putText(img, "Swap 3", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                #     keyboard.press('u')
                    # keyboard.release('k')
                    # keyboard.release(Key.up)
                    # keyboard.release(Key.right)
                    # keyboard.release(Key.left)
                    # keyboard.release(Key.down)
            
                
                

            if hand["type"] == "Left":
                if finger == [0, 1, 0, 0, 0]:
                    print("Punch")
                    cv2.putText(img, "Punch", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press('u')
                    keyboard.release('i')
                    keyboard.release('k')
                    keyboard.release(Key.up)
                    keyboard.release(Key.right)
                    keyboard.release(Key.left)
                    keyboard.release(Key.down)

                if finger == [0, 1, 1, 0, 0]:
                    print("Punch")
                    cv2.putText(img, "Punch", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press('i')
                    keyboard.release('u')
                    keyboard.release('k')
                    keyboard.release(Key.up)
                    keyboard.release(Key.right)
                    keyboard.release(Key.left)
                    keyboard.release(Key.down)

                    # keyboard.release('a')
                    # keyboard.release('d')
                    # keyboard.release('s')
                    # keyboard.release('z')
                    # keyboard.release('x')
                    # keyboard.release('c')
                    # keyboard.release('v')

                if finger == [1,0,0,0,0]:
                    print("Kick")
                    cv2.putText(img, "Kick", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press('j')
                    keyboard.release('i')
                    keyboard.release('u')
                    keyboard.release('k')
                    keyboard.release(Key.up)
                    keyboard.release(Key.right)
                    keyboard.release(Key.left)
                    keyboard.release(Key.down)
                    # keyboard.release('w')
                    # keyboard.release('a')
                    # keyboard.release('s')
                    # keyboard.release('z')
                    # keyboard.release('x')
                    # keyboard.release('c')
                    # keyboard.release('v')

                if finger == [1,1,0,0,0]:
                    print("kick")
                    cv2.putText(img, "kick", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press('k')
                    keyboard.release('i')
                    keyboard.release('u')
                    keyboard.release(Key.up)
                    keyboard.release(Key.right)
                    keyboard.release(Key.left)
                    keyboard.release(Key.down)
                    # keyboard.release('w')
                    # keyboard.release('d')
                    # keyboard.release('a')
                    # keyboard.release('z')
                    # keyboard.release('x')
                    # keyboard.release('c')
                    # keyboard.release('v')

                # if finger == [1, 1, 1, 1, 1]:
                #     print("Special Attack")
                #     cv2.putText(img, "Special Attack", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                #     keyboard.press('z')
                #     keyboard.release('w')
                #     keyboard.release('d')
                #     keyboard.release('s')
                #     keyboard.release('a')
                #     keyboard.release('x')
                #     keyboard.release('c')
                #     keyboard.release('v')

                # if finger == [1, 1, 0, 0, 0]:
                #     print("Dragon Rush")
                #     cv2.putText(img, "Dragon Rush", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                #     keyboard.press('x')
                #     keyboard.release('w')
                #     keyboard.release('d')
                #     keyboard.release('s')
                #     keyboard.release('z')
                #     keyboard.release('a')
                #     keyboard.release('c')
                #     keyboard.release('v')

                # if finger == [1, 1, 1, 0, 0]:
                #     print("Super Dash")
                #     cv2.putText(img, "Super Dash", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                #     keyboard.press('c')
                #     keyboard.release('w')
                #     keyboard.release('d')
                #     keyboard.release('s')
                #     keyboard.release('z')
                #     keyboard.release('a')
                #     keyboard.release('x')
                #     keyboard.release('v')

                # if finger == [1, 1, 1, 1, 0]:
                #     print("Vanish")
                #     cv2.putText(img, "Vanish", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                #     keyboard.press('v')
                #     keyboard.release('w')
                #     keyboard.release('d')
                #     keyboard.release('s')
                #     keyboard.release('z')
                #     keyboard.release('a')
                #     keyboard.release('c')
                #     keyboard.release('x')
            else:
                keyboard.release('u')
                keyboard.release('i')
                keyboard.release(Key.up)
                keyboard.release(Key.right)
                keyboard.release(Key.left)
                keyboard.release(Key.down)
                keyboard.release('j')
                keyboard.release('k')
                # keyboard.release('d')
                # keyboard.release('s')
                # keyboard.release('z')
                # keyboard.release('a')
                # keyboard.release('c')
                # keyboard.release('x')

    cv2.imshow("Tekken Player 1", img)
    if cv2.waitKey(1) == ord("q") or cv2.waitKey(1) == 27:
        break