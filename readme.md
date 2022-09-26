1:さかな～のときのポーズだけをしている動画を撮影し、posture.mp4という名前に変更する

2:ちんあなご～の音声データを入手し、chinanago.mp3という名前に変更する

3:1と2で入手したデータをsakana_chinanago下に移動させる。（↓ディレクトリ構成）
  ```bash
  sakana_chinanago
    |-chinanago.mp3
    |-posture.mp4
    |-main.py
  ...
  ```

4:
```bash
python specified_posture_data_preparation.py --source posture.mp4
```

5:
```bash
python main.py
```
