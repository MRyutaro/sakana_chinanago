import argparse
import cv2
import openpifpaf


SIZE_RATE = 0.1

if __name__ == '__main__':
    """settings"""
    openpifpaf.show.Canvas.show = True

    parser = argparse.ArgumentParser()
    parser.add_argument('--source', help='this input video')
    args = parser.parse_args()

    capture = cv2.VideoCapture(args.source)

    while capture.isOpened():
        _, image = capture.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, dsize=None, fx=SIZE_RATE, fy=SIZE_RATE)
        predictor = openpifpaf.Predictor(
            checkpoint='shufflenetv2k16', json_data=False)
        predictions, gt_anns, meta = predictor.numpy_image(image)

        for i in range(len(predictions)):
            print("#" * 4 + str(i) + "人目" + "#" * 4)
            for j in range(len(predictions[i].data)):
                pos_x, pos_y = predictions[i].data[j][:2]
                print(j, "x座標：", pos_x, "y座標：", pos_y)
                cv2.circle(image, (int(pos_x), int(pos_y)),
                           2, (255, 255, 255,), thickness=3)
           
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imshow('image', image)
        cv2.waitKey(1)
    capture.release()
