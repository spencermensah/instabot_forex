#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI

api = InstagramAPI("sudoperspective", "redaroly")

def sendDM(api,user_id,message):
    # api.searchUsername(username)
    # response = api.LastJson
    # user_id = response['user']['pk']
    mediaId = '1469246128228859784_1520786701' #i dont know what this is but was on sourse code
    recipients = [user_id]
    api.direct_message(message, user_id)

def getTotalFollowers(api, username):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """
    api.searchUsername(username)
    response = api.LastJson
    user_id = response['user']['pk']

    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers

def getTotalFollowing(api, username):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """
    api.searchUsername(username)
    response = api.LastJson
    user_id = response['user']['pk']

    following = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowings(user_id, maxid=next_max_id)
        following.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return following

if (api.login()):
    #usersList = ["lewis_boughtflower","sofiaxsharp_","spencermensah"]
    # usersList = ["spencermensah"]
    #
    # for names in usersList:
    #     sendDM(api,names)

    followers = getTotalFollowing(api, "pechee.__")

    message = "hey xx"

    for follower in followers:
        userId = follower['pk']
        sendDM(api,userId,message)
        print(follower['username'])

    # usersList = ["spencermensah","lewis_boughtflower"]
    #
    # for names in usersList:
    #     sendDM(api,names,message)

else:
    print("Can't login!")
