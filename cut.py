import subprocess
def cut(input_path, start, end, output_path):
    command = [
        "ffmpeg",
        "-y",
        "-ss",
        str(start),
        "-to",
        str(end),
        "-i",
        input_path,
        "-c:v",
        "libx264",
        "-crf",
        "18",
        "-c:a",
        "aac",
        "-pix_fmt",
        "yuv420p",
        "-movflags",
        "-faststart",
        output_path
    ]
    subprocess.run(command,check=True)



cut("episode.mp4", "90", "120", "output.mp4")