# rewatch

rewatch takes a long video and turns it into short clips with captions. It all runs on your own laptop. No API keys, no uploading your videos anywhere, no paying per clip.

I'm building this from scratch to learn, so it's early. This is version 0.1.0.

## What works right now

You can cut any part of a video into a clip that plays everywhere (phones, Macs, Windows, Instagram, WhatsApp). You can also give it a clip and it will listen to the speech, write captions and put them on the video. The listening part uses Whisper, running locally.

## What I'm working on next

The big one: finding the best moments in a long video by itself. A lot of clipping tools just ask an AI chatbot "what's interesting here?". I want to train a model on what people actually rewatch on YouTube and use that instead.

After that, a vertical crop that follows whoever is talking, and captions in Hindi and Telugu.

## Before you install

You need Python 3.11 or newer, and FFmpeg.

One thing that took me a while to figure out: on a Mac, the normal `brew install ffmpeg` can't draw captions, because it's built without a library called libass. You need `ffmpeg-full`:

```
brew install ffmpeg-full
brew unlink ffmpeg
brew link --force ffmpeg-full
```

To check, run `ffmpeg -hide_banner -filters | grep subtitles`. If it prints nothing, captions won't work.

## Install

```
git clone https://github.com/shaikashfaaqhamja/rewatch.git
cd rewatch
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## How to use it

Cut 30 seconds, starting at 1:30:

```
rewatch cut episode.mp4 90 120 clip.mp4
```

Put captions on a clip:

```
rewatch captions clip.mp4 clip_captioned.mp4
```

The first time you run captions it downloads the Whisper model, so give it a minute.

## What happens inside

FFmpeg cuts the clip and converts it to H.264 video and AAC audio, which is what plays everywhere. Then faster-whisper listens to it and gives back every word with the time it was said. I group those words into short lines of up to five words, and a line also ends wherever a sentence ends. The lines go into an SRT file, and FFmpeg draws them onto every frame.

## License

MIT, so you can use it however you want. See [LICENSE](LICENSE).