# Twitter_Cleanup
A simple python script to clean up old tweets and favorites.


Special thanks from @imathew. I got this from his blog. https://www.mathewinkson.com/2015/03/delete-old-tweets-selectively-using-python-and-tweepy

I basically updated the print lines to be compatible with python3.

## Requirements:
*Python 3.X
*Tweepy (pip install tweepy)
*A twitter developer account and you need to create a standalone app to get the credentials. Make sure you give the app read/write permissions.

## Usage
Its pretty straightforward. If you want to delete tweets, set delete_tweets to true. If you want to delete favorites, set delete_favs to true. days_to_keep specifies how many of the past days of twitter activity that you want to perserve. If there are any tweets/favorites outside of specified range that you want to keep, go to the tweet, grab the number at the end of the URL and add it to the tweets_to_save/favs_to_save section. Don't forget your indents and commas.