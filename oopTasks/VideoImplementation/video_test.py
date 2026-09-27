import unittest

from video import VideoFunctions

class MyTestCase(unittest.TestCase):
    def test_the_video_is_playing(self):
        video = VideoFunctions("Game of throne", 10)
        self.assertEqual(video.play(), "Game of throne is playing")
        self.assertTrue(video.is_playing)
    def test_the_video_is_playing_and_got_forwarded(self):
        video = VideoFunctions("Game of throne", 10)
        video.play()
        video.advance(8)
        self.assertEqual(video.current_playback, 8)
    def test_the_video_is_not_playing_and_advance(self):
        video = VideoFunctions("Game of throne", 10)
        self.assertRaises(ValueError, video.advance, 3)
    def test_the_video_got_advance_by_negative_second(self):
        video = VideoFunctions("Game of throne", 10)
        video.play()
        self.assertRaises(ValueError, video.advance, -1)
        self.assertEqual(video.current_playback, 0)
    def test_the_video_got_advance_by_zero_second(self):
        video = VideoFunctions("Game of throne", 10)
        video.play()
        self.assertRaises(ValueError, video.advance, 0)
    def test_the_video_is_playing_and_advance_below_above_duration(self):
        video = VideoFunctions("Game of throne", 10)
        video.play()
        video.advance(5)
        self.assertEqual(video.current_playback, 5)
        self.assertRaises(ValueError, video.advance, 7)
        self.assertEqual(video.current_playback, 5)
    def test_the_video_is_not_playing_and_advance_below_or_above_duration(self):
        video = VideoFunctions("Game of throne", 10)
        self.assertRaises(ValueError, video.advance, 5)
        self.assertRaises(ValueError, video.advance, 15)
    def test_the_video_is_playing_and_advance_above_duration(self):
        video = VideoFunctions("Game of throne", 10)
        video.play()
        self.assertRaises(ValueError, video.advance, 17)
        self.assertEqual(video.current_playback, 0)
    def test_that_video_has_reached_the_end(self):
        video = VideoFunctions("Game of throne", 10)
        video.play()
        video.advance(5)
        self.assertEqual(video.current_playback, 5)
        self.assertFalse(video.is_finished())
        video.advance(5)
        self.assertEqual(video.current_playback, 10)
        self.assertTrue(video.is_finished())
    def test_that_video_advance_more_than_duration_and_is_not_finish(self):
        video = VideoFunctions("Game of throne", 10)
        video.play()
        self.assertRaises(ValueError, video.advance, 17)
        self.assertEqual(video.current_playback, 0)
        self.assertFalse(video.is_finished())
    def test_that_video_reset_back_to_the_beginning(self):
        video = VideoFunctions("Game of throne", 10)
        video.play()
        video.advance(5)
        self.assertEqual(video.current_playback, 5)
        video.restart()
        self.assertEqual(video.current_playback, 0)
    def test_that_video_is_not_playing_and_reset(self):
        video = VideoFunctions("Game of throne", 10)
        self.assertRaises(ValueError, video.restart)
    def test_that_video_is_playing_and_reset(self):
        video = VideoFunctions("Game of throne", 10)
        video.play()
        self.assertEqual(video.current_playback, 0)
        video.restart()
        self.assertEqual(video.current_playback, 0)
    def test_to_check_time_remaining(self):
        video = VideoFunctions("Game of throne", 10)
        video.play()
        video.advance(4)
        self.assertEqual(video.current_playback, 4)
        self.assertEqual(video.time_remaining(), 6)
    def test_to_check_time_remaining_2(self):
        video = VideoFunctions("Game of throne", 10)
        video.play()
        self.assertEqual(video.current_playback, 0)
        self.assertEqual(video.time_remaining(), 10)
    def test_to_check_time_remaining_video_not_playing(self):
        video = VideoFunctions("Game of throne", 10)
        self.assertEqual(video.time_remaining(), 10)

if __name__ == '__main__':
    unittest.main()