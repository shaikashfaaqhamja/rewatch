from faster_whisper import WhisperModel

def transcribe(path):
    model = WhisperModel("tiny", device="cpu", compute_type="int8")
    segments, info = model.transcribe("clip.mp4", word_timestamps=True)

    for segment in segments:
        for word in segment.words:
            print(f"{word.word}, {word.start}, {word.end}")

if __name__ == "__main__":
    transcribe("clip.mp4")