import argparse
import cv2
from recognize_specified_posture import RecognizePosture as RP

# python skeleton_coordinate_acquisition.py --source posture.mp4


# 予め認識させたいポーズがどんなものかを指定する方式
class CheckPoseMatch():
    def __init__(self, posture_name: str):
        print("初期化")
        self.posture_name = posture_name
        print("posture_nameのjsonファイルの読みこみ")

    def check_pose_match(self, raw_image) -> bool:
        print("ポーズが一致するかを検証")
        print("RPを使う")
        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--video', help='this input video', default="sakana.mp4")
    args = parser.parse_args()

    capture = cv2.VideoCapture(args.video)

    check_pose_match = CheckPoseMatch("sakana")

    while capture.isOpened():
        _, image = capture.read()
        check_pose_match.check_pose_match(image)

        if cv2.waitKey(1) == 27:
            exit()
