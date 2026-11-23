from faster_whisper import WhisperModel

from dataclasses import dataclass


@dataclass
class Word:
    text: str
    start: float
    end: float


def transcribe(path):
    model = WhisperModel("tiny", device="cpu", compute_type="int8")
    segments, info = model.transcribe("clip.mp4", word_timestamps=True)

    words = []

    for segment in segments:
        for word in segment.words:
            words.append(Word(word.word.strip(), float(round(word.start, 2)), float(round(word.end, 2))))
    
    return words

if __name__ == "__main__":
    words = transcribe("clip.mp4")
    for w in words:
        print(w)