import re

def extractMovieTitles(text):
    movieTitlePattern = r'(.+)\s\(\d{4}\)'
    return re.findall(movieTitlePattern, text)

# Test the Regular Expression
if __name__ == "__main__":
    testText = "SnowFall (2017) is a crime movie. Pay it Forward"
    movieTitles = extractMovieTitles(testText)
     # print found result
    print("Movie Titles found:", movieTitles)
