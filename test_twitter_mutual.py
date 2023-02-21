import pytest
from twitter_mutual import *
import tweepy

@pytest.fixture
def api():
   #keys and secrets
   consumer_key = "DfX0h6Q77YLZP8a5NTaBOqZze"
   consumer_secret = "IpECn4KomuBfItdrHrollLLTp2hbRV6y225krt0gGo7PY6CM91"
   access_token = "2834678624-yVB4Vfy2dG9MwaTqMH7o7FtWGv67WvqT35BKojC"
   access_token_secret = "z22FJONPWbFoLaRe6mjFSAvg5ipWrhRAx75v7tRvT00Pb"


   #authentification
   auth = tweepy.OAuth1UserHandler(
               consumer_key,
               consumer_secret,
               access_token,
               access_token_secret
               )

   api = tweepy.API(auth)
   return api

@pytest.fixture
def username():
   return "watercolor355"

@pytest.fixture
def watercolor355_followers(api, username):
   user_info = api.get_user(screen_name = username)
   return user_info.followers_count

@pytest.fixture
def watercolor355_friends(api, username):
   user_info = api.get_user(screen_name = username)
   return user_info.friends_count

@pytest.fixture
def friends_users(api):
   return tweepy.Cursor(api.get_friends, screen_name = username, count = 100).pages(4)

@pytest.fixture
def followers_users(api):
   return tweepy.Cursor(api.get_followers, screen_name = username, count = 100).pages(4)

@pytest.fixture
def friends_usernames(api):
   temp = tweepy.Cursor(api.get_friends, screen_name = username, count = 100).pages(4)
   return usernames_list(temp)



@pytest.fixture
def followers_usernames(api):
   temp = tweepy.Cursor(api.get_followers, screen_name = username, count = 100).pages(4)
   return usernames_list(temp)





def test_users_pages(api, username, watercolor355_followers, watercolor355_friends):
   watercolor355_pages = max(watercolor355_followers, watercolor355_friends) // 100 + 1
   num_pages = users_pages(username, api)
   assert num_pages == watercolor355_pages


def test_usernames_list(friends_users, followers_users, watercolor355_friends, watercolor355_followers):
   friends_hashset = usernames_list(friends_users)
   followers_hashset = usernames_list(followers_users)

   assert len(friends_hashset) == int(watercolor355_friends)
   assert len(followers_hashset) == int(watercolor355_followers)


#manual test, can change at any time
def test_classify_friends(friends_usernames, followers_usernames):
   res = classify_friends(friends_usernames, followers_usernames)

   assert len(res[0]) == 112
   assert len(res[1]) == 23











