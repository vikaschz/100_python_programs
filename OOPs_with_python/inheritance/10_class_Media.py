"""
Create a base class Media with play(). Derive Audio and Video classes.
"""


class Media:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def play(self):

        print(f"Now playing: {self.title}")


class Audio(Media):
    def __init__(self, title, duration, bitrate):
        super().__init__(title, duration)
        self.bitrate = bitrate

    def play(self):
        super().play()
        print(f"Outputting audio at {self.bitrate} kbps... 🔊")


class Video(Media):
    def __init__(self, title, duration, resolution):
        super().__init__(title, duration)
        self.resolution = resolution

    def play(self):
        super().play()
        print(f"Rendering video at {self.resolution} resolution... 🎬")


song = Audio("Blinding Lights", 200, 320)
movie = Video("Inception", 8800, "4K")

print("--- Media Player ---")
song.play()
movie.play()
