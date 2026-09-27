class VideoFunctions:
    def __init__(self, title:str, duration_minutes : int):
        self.title = title
        self.duration = duration_minutes
        self.current_playback = 0
        self.is_playing = False
    def play(self):
        self.is_playing = True
        return self.title + " is playing"
    def advance(self, seconds:int):
        if not self.is_playing :
            raise ValueError("Video is not playing")
        elif seconds <= 0 :
            raise ValueError("The second must be greater than 0")
        elif seconds > self.duration:
            raise ValueError("The second must be below video duration")
        elif (self.current_playback + seconds) <= self.duration :
            self.current_playback += seconds
        else :
            raise ValueError("You cant forward above the video duration")
    def is_finished(self):
        return self.duration == self.current_playback
    def restart(self):
        if self.is_playing :
            self.current_playback = 0
        else :
            raise ValueError("Video has not started yet")
    def time_remaining(self):
        return self.duration - self.current_playback