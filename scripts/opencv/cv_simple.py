import cv2

def main():
    vid = cv2.VideoCapture(2)
    #vid.set(3, 1280)  # set the resolution
    #vid.set(4, 720)
    vid.set(cv2.CAP_PROP_AUTOFOCUS, 1)  # turn the autofocus on
    while (True):
        ret, frame = vid.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
        main()