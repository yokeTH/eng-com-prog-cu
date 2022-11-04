# 2565_1_Quiz_2_3

colorFilename = input()
lyricsFilename = input()

colorFile = open(colorFilename)
lyricsFile = open(lyricsFilename)

color = []
for ln in colorFile:
    for e in ln.strip().split():
        color.append(e.lower())

lyrics = lyricsFile.read()     
for e in color:
    i = lyrics.lower().find(e)
    while i != -1:
        lyrics = lyrics[:i] + '<'+e+'>' + lyrics[i:i+len(e)] + '</>' + lyrics[i+len(e):]
        i = lyrics.lower().find(e,i+len(e)*2+5)
        
print(lyrics)