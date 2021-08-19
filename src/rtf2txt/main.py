from pathlib import Path
from typing import Optional

import striprtf
import typer
from striprtf.striprtf import rtf_to_text

from . import __version__

app = typer.Typer()

def version_callback(value: bool):
    if value:
        typer.echo(f"rtf2txt {__version__}")
        raise typer.Exit()

@app.command()
def main(
        infile: Path,
        outfile: Optional[Path] = typer.Argument(None),
        version: Optional[bool] = typer.Option(
            None, "--version", "-V", callback=version_callback
        ),
    ):
    """Convert RTF file to plain text"""
    
    if infile is None:
        typer.echo(f"[Errno 2] No such file or directory: '{infile}'")
        raise typer.Abort()

    if infile.is_dir():
        typer.echo(f"[Errno 3] directory provided instead of file: '{infile}'")
        raise typer.Abort()

    if (outfile != None) and outfile.is_dir():
        typer.echo(f"[Errno 3] directory provided instead of file: '{outfile}'")
        raise typer.Abort()


    try:
        with open(infile, mode="r") as f:
            file_contents = f.read()

    except FileNotFoundError as e:
        typer.echo(str(e))
        exit(-1)

    text = rtf_to_text(file_contents)
    if outfile is None:
        typer.echo(text)
        return
    
    try:    
        with open(outfile, mode="w+", encoding="utf-8") as f:
            f.write(text)
        typer.echo(f"{len(text)} bytes written")

    except FileNotFoundError as e:
        typer.echo(str(e))
        exit(-1)

    except PermissionError as e:
        typer.echo(str(e))
        exit(-1)


if __name__ == "__main__":
    # execute only if run as a script
    app()
