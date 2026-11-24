import subprocess


def burn(input_path, srt_path, output_path):
    command = [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-i", input_path,
        "-vf", f"subtitles={srt_path}",
        "-c:v", "libx264", "-crf", "18",
        "-c:a", "copy",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        output_path,
    ]
    subprocess.run(command, check=True)


if __name__ == "__main__":
    burn("clip.mp4", "clip.srt", "clip_captioned.mp4")
