import argparse
import cv2
from check_pose_match import CheckPoseMatch as CPM
from controller.sound_play import SoundPlay

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', help='this input video')
    args = parser.parse_args()
    print("識別したいポーズ名をコマンドラインで取得")
    print("再生したい音声のデータのパスをコマンドラインで取得")

    capture = cv2.VideoCapture(1)
    is_prepared_pose = CPM("POSTURE_NAME")
    sound_play = SoundPlay("chinanago.mp3")

    while capture.isOpened():
        _, image = capture.read()
        print("識別したいポーズかどうかを検証")
        if is_prepared_pose.check_pose_match(image):
            print("識別したいポーズなら音を鳴らす")
            sound_play.sound_play()
            print("音を再生している間はフレームをとっていない。とれるように並列処理を行う")

        cv2.imshow("image", image)
        if cv2.waitKey(1) == 27:
            exit()
