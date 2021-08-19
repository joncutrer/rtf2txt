# rtf2txt

A simple command line tool to convert rtf files to plain txt.

## Usage 
```
Usage: rtx2txt.exe INFILE [OUTFILE]

Arguments:
  INFILE    [required]
  OUTFILE   [optional]

```

### Example 1

```
rtx2txt.exe doc.rtf doc.txt
```

### Example 2

```
rtx2txt.exe doc.rft > doc.txt
```

This application was written in Python.  The actual conversion work of the tool is done by the `striprtf` python module while the rest is handled by the excellent `Typer` cli framework.  `PyInstaller` is used to compile the final binary exectuable.

## License

MIT License