# import the module
import tweepy
import sys

def users_pages(username, api):
   '''
   takes in a username in form of a string and API
   returns pages of profiles in form of tweepy.cursor.CursorIterator
   '''
   user_info = api.get_user(screen_name = username)
   num_pages = max(user_info.friends_count, user_info.followers_count) // 100 + 1
   return num_pages

def usernames_list(pages):
   '''
   takes in tweepy.cursor.CursorIterator (pages of users)
   returns a hashset of usernames
   '''
   usernames = set()
   for page in pages:
      for user in page:
         usernames.add(user.screen_name)
   return usernames

def classify_friends(friends, followers):
   '''
   takes in two lists (friends, followers)
   returns list in format [1, 2] where
      - 1: users who follow you back
      - 2: users who do not follow you back
   '''
   follows_back = []
   does_not_follow_back = []
   for friend in friends:
      if friend in followers:
         follows_back.append(friend)
      else:
         does_not_follow_back.append(friend)
   return [follows_back, does_not_follow_back]



def display_results(results):
   '''
   takes in results in form of list of size 2
      - index 0 is follows back, index 1 is does not follow back
   displays who follows back and who does not
   '''

   print("FOLLOWS ME BACK")
   for username in results[0]:
      print(username)

   print("\nDOES NOT FOLLOW ME BACK")
   for username in results[1]:
      print(username)



if __name__ == '__main__':
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

   #user we are evaluating
   if len(sys.argv) == 2:
      username = sys.argv[1]
   else:
      username = "watercolor355"

   num_pages = users_pages(username, api)
   users_friends = tweepy.Cursor(api.get_friends, screen_name = username, count = 100).pages(num_pages)
   users_followers = tweepy.Cursor(api.get_followers, screen_name = username, count = 100).pages(num_pages)

   username_friends = usernames_list(users_friends)
   username_followers = usernames_list(users_followers)

   results = classify_friends(username_friends, username_followers)

   display_results(results)



