import tweepy

from TwitterFollowBot import TwitterBot

my_bot = TwitterBot()
keywords = [line.rstrip('\n') for line in open('brands.txt')]
follow = [line.rstrip('\n') for line in open('Followthese.txt')]
charities = [line.rstrip('\n') for line in open('charities.txt')]
my_bot.auto_fav("charity", count=1)
var = 1
while var == 1:
    keywordcount = 0
    while keywordcount < len(keywords):
        for keyword in keywords:
            my_bot.auto_rt(keyword, count=1)
        keywordcount += 1
    followcount = 0
    while followcount < len(follow):
        for user in follow:
            my_bot.auto_follow_followers_of_user(user, count=1)
        followcount += 1
    charitycount = 0
    while charitycount < len(charities):
        for charity in charities:
            my_bot.send_tweet("Dont forget to help out people at" + charity)
        charitycount += 1
    print("Should start from top")

print("Good bye :(")
