import os
from playsound import playsound

class SoundPlay():
  def __init__(self):
    self.audio_path = "chinanago.mp3"

  def is_existing_voice_file(self):
    return os.path.isfile(self.audio_path)

  def sound_play(self):
    if self.is_existing_voice_file:
      print("音声を再生します")
      playsound(self.audio_path)
  

if __name__ == "__main__":
    sound_play = SoundPlay()
    sound_play.sound_play()