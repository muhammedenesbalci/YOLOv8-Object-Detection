# import libraries
from ultralytics import YOLO
import cv2

# It downloads the model automatically. If not already downloaded
# I choose the medium model you can choose others. Such as, yolov8n, yolov8s etc.
model = YOLO("yolov8m.pt")


# Automatic annotations
def automatic_annotations_img(img_pth):
    # Open the img
    img = cv2.imread(img_pth)

    # Give img to the model
    result = model(img)

    # Take annotated results
    annotated_img = result[0].plot()

    # Save annotated image
    cv2.imwrite("../datas/test_img_result_automatic.jpg", annotated_img)


# Customized annotations
def customized_annotations_img(img_pth):
    # Open the img
    img = cv2.imread(img_pth)

    # Give img to the model
    result = model(img)

    # Get boxes
    boxes = result[0].boxes.xyxy.cpu().numpy().astype(int)

    # Get indexes of object names
    clss = result[0].boxes.cls

    for box, cls in zip(boxes, clss):
        # Get name of object
        name = result[0].names[int(cls)]

        # Draw Rectangle
        cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), 2)

        # Find center of object
        center_of_object = (int((box[2] - box[0]) / 2) + box[0], int((box[3] - box[1]) / 2) + box[1])

        # Put a dot to center of object
        cv2.circle(img, (center_of_object), 5, (0, 255, 0), cv2.FILLED)

        # Write names and center points
        cv2.putText(img, f"{name}-{center_of_object}", (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Save Result
    cv2.imwrite("../datas/test_img_result_customized.jpg", img)


def customized_annotations_video(video_pth):
    # Set Video
    cap = cv2.VideoCapture(video_pth)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Set video writer
    writer = cv2.VideoWriter('../datas/test_video_result_customized.mp4',
                             cv2.VideoWriter_fourcc(*'DIVX'), 25, (1280, 720))

    # Start
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error starting camera")
            break
        try:
            # Give img to the model
            result = model(frame)

            # Get boxes
            boxes = result[0].boxes.xyxy.cpu().numpy().astype(int)

            # Get indexes of object names
            clss = result[0].boxes.cls

            for box, cls in zip(boxes, clss):
                # Get name of object
                name = result[0].names[int(cls)]

                # Draw Rectangle
                cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), 2)

                # Find center of object
                center_of_object = (int((box[2] - box[0]) / 2) + box[0], int((box[3] - box[1]) / 2) + box[1])

                # Put a dot to center of object
                cv2.circle(frame, (center_of_object), 5, (0, 255, 0), cv2.FILLED)

                # Write names and center points
                cv2.putText(frame, f"{name}-{center_of_object}", (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 0, 0), 2)

        except Exception as e:
            print(e)
        # Show video
        cv2.imshow("frame", frame)

        # Write frames for a video
        writer.write(frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Close video writer and video
    cap.release()
    writer.release()
    cv2.destroyAllWindows()

img_pth = "../datas/test_img.jpg"

automatic_annotations_img(img_pth)
customized_annotations_img(img_pth)

video_pth = "../datas/test_video.mp4"
customized_annotations_video(video_pth)