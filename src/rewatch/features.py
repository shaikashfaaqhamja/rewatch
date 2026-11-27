from faster_whisper.audio import decode_audio
import numpy as np
from rewatch.transcribe import transcribe

SAMPLE_RATE = 16000

def loudness_per_second(path):
    audio = decode_audio(path, sampling_rate=SAMPLE_RATE)
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

def scale(values):
    values = np.array(values, dtype=float)
    min_val = np.min(values)
    max_val = np.max(values)
    if max_val - min_val == 0:
        return np.zeros_like(values)
    return (values - min_val) / (max_val - min_val)

def window_scores(scores, size):
    total = sum(scores[:size])
    result = [total]
    for i in range(size, len(scores)):
        total += scores[i]
        total -= scores[i - size]
        result.append(total)
    return result


if __name__ == "__main__":
    loud = loudness_per_second("clip.mp4")
    words = transcribe("clip.mp4")
    speed = words_per_second(words, len(loud))
    score = scale(loud) + scale(speed)
    windows = window_scores(score, 5)
    print(len(windows))
    print(np.round(windows, 2))