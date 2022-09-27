1:カギにしたいポーズだけをしている動画を撮影する(.mp4)

2:再生したい音声データを用意する(.mp3)

3:1と2で入手したデータをsakana_chinanago下に移動させる。（↓ディレクトリ構成）
  ```bash
  sakana_chinanago
    |-*.mp3
    |-*.mp4
    |-main.py
  ...
  ```

4:カギとなるポーズを用意する
```bash
python prepare_specified_posture_data.py --source <VIDEO_PATH>
```

5:カギにしたポーズと一致するか確認する
```bash
python main.py --source <AUDIO_PATH>
```
