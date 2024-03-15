import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Controller, Key

video = cv2.VideoCapture(0)

cv2.namedWindow("Tekken Player 2", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Tekken Player 2", cv2.WND_PROP_TOPMOST, 1)

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
                    keyboard.press('w')
                    keyboard.release("s")
                    keyboard.release("d")
                    keyboard.release("a")
                    keyboard.release('f')
                    keyboard.release('g')

                if finger == [0,0,0,0,1]:
                    print("Right")
                    cv2.putText(img, "Right", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press("d")
                    keyboard.release("s")
                    keyboard.release("w")
                    keyboard.release("a")
                    keyboard.release('f')
                    keyboard.release('g')

                if finger == [1, 0, 0, 0, 0]:
                    print("left")
                    cv2.putText(img, "Left", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press("a")
                    keyboard.release("s")
                    keyboard.release("d")
                    keyboard.release("w")
                    keyboard.release('f')
                    keyboard.release('g')

                if finger == [0,0,0,0,0]:
                    print("Down")
                    cv2.putText(img, "Down", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press("s")
                    keyboard.release("w")
                    keyboard.release("d")
                    keyboard.release("a")
                    keyboard.release('f')
                    keyboard.release('g')

                # if finger == [0, 1, 1, 1, 1]:
                #     print("Swap 1")
                #     cv2.putText(img, "Swap 1", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                #     keyboard.press('H')
                #     keyboard.release("w")
                #     keyboard.release("d")
                #     keyboard.release("a")
                #     keyboard.release("s")
                #     keyboard.release('G')

                # if finger == [1, 1, 1, 1, 1]:
                #     print("Swap 1")
                #     cv2.putText(img, "Swap 1", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                #     keyboard.press('Q')
                #     keyboard.release('F')
                #     keyboard.release("w")
                #     keyboard.release("d")
                #     keyboard.release("a")
                #     keyboard.release("s")
                    
                # if finger == [0,0,0,0,0]:
                #     print("Swap 3")
                #     cv2.putText(img, "Swap 3", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                #     keyboard.press('F')
                #     keyboard.release('Q')
                #     keyboard.release("w")
                #     keyboard.release("d")
                #     keyboard.release("a")
                #     keyboard.release("s")
            
                
                

            if hand["type"] == "Left":
                if finger == [0, 1, 0, 0, 0]:
                    print("Punch")
                    cv2.putText(img, "Punch", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press('f')
                    keyboard.release('g')
                    keyboard.release("q")
                    keyboard.release("w")
                    keyboard.release("d")
                    keyboard.release("a")
                    keyboard.release("s")


                if finger == [0, 1, 1, 0, 0]:
                    print("Punch")
                    cv2.putText(img, "Punch", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press('i')
                    keyboard.release('f')
                    keyboard.release("q")
                    keyboard.release("w")
                    keyboard.release("d")
                    keyboard.release("a")
                    keyboard.release('s')
                    # keyboard.release('a')
                    # keyboard.release('d')
                    # keyboard.release('s')
                    # keyboard.release('z')
                    # keyboard.release('x')
                    # keyboard.release('c')
                    # keyboard.release('v')

                if finger == [1, 0, 0, 0, 0]:
                    print("kick")
                    cv2.putText(img, "kick", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press('h')
                    keyboard.release('g')
                    keyboard.release("f")
                    keyboard.release('q')
                    keyboard.release("w")
                    keyboard.release("d")
                    keyboard.release("a")
                    keyboard.release('s')

                    # keyboard.release('w')
                    # keyboard.release('a')
                    # keyboard.release('s')
                    # keyboard.release('z')
                    # keyboard.release('x')
                    # keyboard.release('c')
                    # keyboard.release('v')

                if finger == [1,1,0,0,0]:
                    print("kick")
                    cv2.putText(img, "Skill 4", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
                    keyboard.press('q')
                    keyboard.release('g')
                    keyboard.release('f')
                    keyboard.release("w")
                    keyboard.release("d")
                    keyboard.release("a")
                    keyboard.release("s")

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
                keyboard.release('f')
                keyboard.release('g')
                keyboard.release("w")
                keyboard.release("d")
                keyboard.release("a")
                keyboard.release("s")
                keyboard.release('h')
                keyboard.release('q')


    cv2.imshow("Tekken Player 2", img)
    if cv2.waitKey(1) == ord("q") or cv2.waitKey(1) == 27:
        break