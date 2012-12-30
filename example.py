'''
	Simple example to demonstrate usage of LyricsParser
'''
from LyricsParser import Parser

song = Parser("eminem", "when i'm gone")
lyrics = song.parse()
print lyrics
