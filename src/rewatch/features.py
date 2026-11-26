from faster_whisper.audio import decode_audio
import numpy as np

def loudness_per_second(path):
    audio = decode_audio(path, sampling_rate=16000)
    seconds = len(audio) // SAMPLE_RATE
    audio = audio[:seconds * SAMPLE_RATE]
    grid = audio.reshape(seconds, SAMPLE_RATE)
    return np.sqrt(np.mean(grid**2, axis=1))

SAMPLE_RATE = 16000
if __name__ == "__main__":
    loud = loudness_per_second("clip.mp4")
    print(len(loud))
    print(loud.round(3))