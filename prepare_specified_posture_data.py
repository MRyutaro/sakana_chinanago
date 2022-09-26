# 特定のポーズだけをした動画を用意する
# mkdir posture_data
import argparse
import cv2
from recognize_specified_posture import RecognizePosture as RP


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', help='this input video')
    args = parser.parse_args()

    capture = cv2.VideoCapture(args.source)

    recognize_posture = RP()

    while capture.isOpened():
        _, image = capture.read()
        posture_data = recognize_posture.get_posture_data(image)
        print(posture_data)
        print("必要なデータだけ取得する")

        if cv2.waitKey(1) == 27:
            exit()

    print("jsonファイルに出力するデータ作成")
    print("jsonファイルに骨格情報を出力")
