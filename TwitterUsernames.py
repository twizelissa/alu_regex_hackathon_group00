import re

TWITTER_USERNAME_PATTERN = r'@([a-zA-Z0-9_]+)'

def extract_twitter_usernames(text):
    return re.findall(TWITTER_USERNAME_PATTERN, text)

if __name__ == "__main__":
    test_text = "Hello , my name is jase ! follow to get best of stories on x @twizelissa @user12 and follow @realman_user!"
    twitter_usernames = extract_twitter_usernames(test_text)
     # print found result
    print("Twitter Usernames found:", twitter_usernames)
