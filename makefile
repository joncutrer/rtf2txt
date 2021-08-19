build:
	poetry run pyinstaller --onefile --specpath ./build --distpath ./dist .\src\rtf2txt\main.py --name rtf2txt

clean:

	rmdir /Q /S build\rtf2txt
	del /Q dist\rtf2txt.exe 

all:
	clean build


.PHONY: all build clean