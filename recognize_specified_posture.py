import argparse
import cv2
import openpifpaf


class RecognizePosture():
    def __init__(self):
        print("初期化")
        openpifpaf.show.Canvas.show = True
        self.SIZE_RATE = 0.1

    def recognize_posture(self, raw_image) -> list:
        rgb_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)
        resized_image = cv2.resize(
            rgb_image, dsize=None, fx=self.SIZE_RATE, fy=self.SIZE_RATE)
        predictor = openpifpaf.Predictor(
            checkpoint='shufflenetv2k16', json_data=False)
        predictions, gt_anns, meta = predictor.numpy_image(resized_image)
        return predictions

    def get_posture_data(self, raw_image):
        predictions = self.recognize_posture(raw_image)
        if len(predictions) == 1:
            return predictions[0].data
        else:
            if len(predictions) == 0:
                print("誰も映っていません")
            else:
                print("動画に複数人映っています。一人で撮影してください。")
            return None
