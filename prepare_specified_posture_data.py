# 特定のポーズだけをした動画を用意する
# mkdir posture_data
import argparse
import cv2
from recognize_specified_posture import RecognizePosture as RP


def extracting_required_data(posture_data: list):
    if posture_data is not None:
        return posture_data[:, 0:2]  # type: ignore
    else:
        return None


def add_data(all_data: list, posture_data: list) -> list:
    joint_position = extracting_required_data(posture_data)
    print(joint_position)
    if joint_position is not None:
        all_data.append(joint_position)
    return all_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--video', help='this input video',
                        default="sakana.mp4")
    args = parser.parse_args()

    capture = cv2.VideoCapture(args.video)

    recognize_posture = RP()
    all_data = list()

    while capture.isOpened():
        ret, image = capture.read()
        if not ret:
            break
        posture_data = recognize_posture.get_posture_data(image)
        all_data = add_data(all_data, posture_data)

    print(all_data)
    print("jsonファイルに出力するデータ作成")
    print("jsonファイルに骨格情報を出力")
