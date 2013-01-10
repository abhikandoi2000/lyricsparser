'''
	Simple example to demonstrate usage of LyricsParser
'''
from LyricsParser import Parser
import sys

if len(sys.argv) == 3:
	artist = sys.argv[1]
	songname = sys.argv[2]
	song = Parser(artist, songname)
	lyrics = song.parse()
	print lyrics
else :
	print "Usage python example.py <artist-name> <song-title>"
	print "Example: python example.py eminem \"space bound\""
