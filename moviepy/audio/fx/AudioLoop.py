from moviepy.audio.AudioClip import concatenate_audioclips
from moviepy.decorators import audio_video_effect

from moviepy.Clip import Clip
from moviepy.Effect import Effect
from dataclasses import dataclass


@dataclass
class AudioLoop(Effect):
    """Loops over an audio clip.

    Returns an audio clip that plays the given clip either
    `n_loops` times, or during `duration` seconds.

    Examples
    --------

    >>> from moviepy import *
    >>> videoclip = VideoFileClip('myvideo.mp4')
    >>> music = AudioFileClip('music.ogg')
    >>> audio = music.with_effects([afx.AudioLoop(duration=videoclip.duration)])
    >>> videoclip.with_audio(audio)

    """

    n_loops: int = None
    duration: float = None

    @audio_video_effect
    def apply(self, clip: Clip) -> Clip:
        if self.duration is not None:
            self.n_loops = int(self.duration / clip.duration) + 1
            return concatenate_audioclips(self.n_loops * [clip]).with_duration(
                self.duration
            )

        return concatenate_audioclips(self.n_loops * [clip])
