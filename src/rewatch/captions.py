from dataclasses import dataclass
from rewatch.transcribe import Word

@dataclass
class Caption:
    text: str
    start: float
    end: float

def group_words(words, max_words = 5):
    captions = []
    current = []
    for word in words:
        current.append(word)
        if len(current) >= max_words or word.text.endswith(('.', '?', '!')):
            text = " ".join([w.text for w in current])
            start = current[0].start
            end = current[-1].end
            captions.append(Caption(text, start, end))
            current = []
    if current:
        text = " ".join([w.text for w in current])
        start = current[0].start
        end = current[-1].end
        captions.append(Caption(text, start, end))
    return captions

def srt_time(seconds):
    ms = round(seconds * 1000)
    hours = ms // 3600000
    minutes = (ms % 3600000) // 60000
    secs = (ms % 60000) // 1000
    millis = ms % 1000
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

def write_srt(captions, path):
    with open(path, 'w', encoding='utf-8') as f:
        for i, c in enumerate(captions, start=1):
            f.write(f"{i}\n")
            f.write(f"{srt_time(c.start)} --> {srt_time(c.end)}\n")
            f.write(f"{c.text}\n\n")


if __name__ == "__main__":
    print(srt_time(1.14), srt_time(75.5))
    from rewatch.transcribe import transcribe

    captions = group_words(transcribe("clip.mp4"))
    write_srt(captions, "clip.srt")

