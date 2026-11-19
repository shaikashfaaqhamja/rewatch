import subprocess
import sys
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
        "+faststart",
        output_path
    ]
    subprocess.run(command,check=True)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python cut.py <input_path> <start_time> <end_time> <output_path>")
        sys.exit(1)


    cut(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])