import instaloader

# Get instance
L = instaloader.Instaloader()

username = 'dxvidnguyen'
password = 'iamawesome'

#login
L.login(username, password)

#profile
profile = instaloader.Profile.from_username(L.context, username)

'''
followees = [igprofile.username for igprofile in profile.get_followees()] #user follows these profiles
followers = [igprofile.username for igprofile in profile.get_followers()] #user is followed by these profiles
'''

followees = [str(igprofile).split()[1] for igprofile in profile.get_followees()] #user follows these profiles
followers = [str(igprofile).split()[1] for igprofile in profile.get_followers()] #user is followed by these profiles

not_mutual = []
mutual = []

for user in followees:
   if user in followers:
      mutual.append(user)
   else:
      not_mutual.append(user)

print('FOLLOWING me back')
print(mutual)
print("NOT FOLLOWING ME BACK")
print(not_mutual)




