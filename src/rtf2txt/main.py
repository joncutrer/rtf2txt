from typing import Optional
import typer
import striprtf
from striprtf.striprtf import rtf_to_text

app = typer.Typer()

@app.command("main", )
def cmd_main(infile: str, outfile: Optional[str] = typer.Argument(None) ):
    """Convert RTF file to plain text"""
    

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




if __name__ == "__main__":
    # execute only if run as a script
    app()