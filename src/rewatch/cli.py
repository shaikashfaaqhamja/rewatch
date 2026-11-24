import typer
from rewatch.transcribe import transcribe
from rewatch.captions import group_words, write_srt
from rewatch.burn import burn


from rewatch.cut import cut as cut_video
app = typer.Typer()

@app.callback()
def main():
    """rewatch turn long videos into short clips"""

@app.command()
def cut(input_path: str, start: float, end: float, output_path: str):
    cut_video(input_path, start, end, output_path)
    typer.echo(f"Saved clip to {output_path}")

@app.command()
def captions(input_path: str, output_path: str):
    words = transcribe(input_path)
    lines = group_words(words)
    write_srt(lines, "captions.srt")
    burn(input_path, "captions.srt", output_path)
    typer.echo(f"Saved captions to {output_path}")




