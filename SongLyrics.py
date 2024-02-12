import re

def extract_song_lyrics(text):
    lyrics_pattern = r'\[Verse \d+\] (.+)'
    return re.findall(lyrics_pattern, text)

# Test the Regular Expression
if __name__ == "__main__":
    test_text = "[Verse 1] Hello it me I was [Verse 1] I'm a Barbie girl, in a Barbie world. Another song goes like [Verse 2] Don't stop believing ."
    song_lyrics = extract_song_lyrics(test_text)
     # print found result
    print("Song Lyrics found:", song_lyrics)
