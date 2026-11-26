from faster_whisper.audio import decode_audio
import numpy as np
from rewatch.transcribe import transcribe

def loudness_per_second(path):
    audio = decode_audio(path, sampling_rate=16000)
    seconds = len(audio) // SAMPLE_RATE
    audio = audio[:seconds * SAMPLE_RATE]
    grid = audio.reshape(seconds, SAMPLE_RATE)
    return np.sqrt(np.mean(grid**2, axis=1))

def words_per_second(words, seconds):
    counts = [0] * seconds
    for word in words:
        second = int(word.start)
        if second < seconds:
            counts[second] += 1
    return counts

SAMPLE_RATE = 16000
if __name__ == "__main__":
    loud = loudness_per_second("clip.mp4")
    words = transcribe("clip.mp4")
    speed = words_per_second(words, len(loud))
    print(speed)