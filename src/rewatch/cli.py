import typer
from rewatch.cut import cut as cut_video
app = typer.Typer()

@app.callback()
def main():
    """rewatch turn long videos into short clips"""

@app.command()
def cut(input_path: str, start: float, end: float, output_path: str):
    cut_video(input_path, start, end, output_path)
    typer.echo(f"Saved clip to {output_path}")

