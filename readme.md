# YT-DLP to MP3 music downloader
This small python script uses yt-dlp with a GUI to download videos from Youtube and convert it as an mp3 file for music backup.
## About the program
The program has a minimal user interface that just asks for a Youtube link (Regular link or a playlist) and gets it all placed in your music folder (Not sure about Mac and Linux as I have not tested it yet)
## Tested website that work with the program
* Youtube (Obviously)
* Soundcloud
* Twitter/X (Why would you do that?)
### Requirements to get the program running.
1. Python (to run it from .py code instead of built executable)
2. [FFmpeg](https://ffmpeg.org/download.html)
3. [yt-dlp](https://github.com/yt-dlp/yt-dlp) 
>Python 3.10 was used for the program, but it is a requirement to have FFmpeg installed 
# How to use
There are two options to run the file, by downloading the executable in the releases tab. (For Windows users)
Or run this command in terminal where you placed the executable.
```
python main.py
```
Changing the python file name from `main.py` to something else can also work for ease of use when you want to use the program from time to time in command line.

* If you don't want to run the executable in windows simply place the `main.py` file in `C:\Users\<USER>` and just write the same command to run it in python.
# Things used to write the code
1. Customtikinter for GUI.
2. yt-dlp for the ability to download from links.
3. PyInstaller to be able to create an executable of the python file.

## Issues with the program I wish that could be fixed
As for now the program when it downloads a single youtube video it can hang for a bit until it finishes, but you can see a command line in the background to see the progress of your download.