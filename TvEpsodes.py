import re

def get_tv_episode_titles(text):
    episode_title_pattern = r'(.+) S\d{2}E\d{2}: (.+)'
    return re.findall(episode_title_pattern, text)

# Test the Regular Expression
if __name__ == "__main__":
    test_text = "The fourth episode is All The Way Down Bad S04E04: SnowFall(2017).   The first episode is Breaking Bad S01E01: Pilot. Another one is Friends S03E10: The One with the Monkey."
    episode_titles = get_tv_episode_titles(test_text)
     # print found result
    print("TV Episode Titles found:", episode_titles)
